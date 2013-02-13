#    interface/contactsManager/__init__.py
#    A part of SkypeTalking application source code
#    Copyright (C) 2010 Hrvoje Katic/SkypeTalking Contributors
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from log import logger
logging=logger.getChild('interface.contactsManager')
from datetime import datetime
from gui_components.sized import SizedDialog
from threading import Thread
from profileViewer import ProfileViewerDialog
import config
import extras
import globalVars
import output
import os
import Skype4Py
import sys
import versionInfo
import wx
import wx.lib.sized_controls as sc
from wx.lib.mixins.listctrl import CheckListCtrlMixin

### Global Variables
ButtonCall=None
ButtonChat=None
ButtonProfile=None
### End Global Variables

def open(action, *args, **kwargs):
	contactsManager=contactsManagerWindow(parent=globalVars.Frame, title=versionInfo.name+" - "+_("Contacts Manager"))
	if action == 'ofSkypeTalking':
		globalVars.Frame.DisplayDialog(contactsManager)
	elif action == 'SkypeOriginal':
		globalVars.Skype.Client.OpenContactsTab()
		for child in globalVars.Frame.GetChildren():
			wx.CallAfter(child.Destroy)

class contacts(Thread):
	"""A Thread which loads list of contacts and their basic information."""

	available=[]
	lstOnlineStatus=[Skype4Py.olsAway,Skype4Py.olsDoNotDisturb,Skype4Py.olsInvisible,Skype4Py.olsNotAvailable,Skype4Py.olsOffline,Skype4Py.olsOnline,Skype4Py.olsSkypeMe,Skype4Py.olsSkypeOut,Skype4Py.olsUnknown]
	lstOnlineStatusMessages=[_('Away'), _('Do not disturb'), _('Invisible'),_('Not available'), _('Offline'), _('Online'), _('Skype Me'),_('Skype Out'), _('Unknown')]
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		contactsOnline=[]
		contactsOffline=[]
		try:
			for friend in globalVars.Skype.Friends:
				(contactsOffline if friend.OnlineStatus==Skype4Py.olsOffline or friend.OnlineStatus==Skype4Py.olsInvisible else contactsOnline).append(friend)
				contactsOnline.sort(cmp=lambda x,y: cmp((x.DisplayName or x.FullName or x.Handle).lower(), (y.DisplayName or y.FullName or y.Handle).lower()))
				if config.conf["contactsmanager"]["showOfflineContacts"]==True:
					contactsOffline.sort(cmp=lambda x,y: cmp((x.DisplayName or x.FullName or x.Handle).lower(), (y.DisplayName or y.FullName or y.Handle).lower()))
					contacts.available=contactsOnline+contactsOffline
				else:
					contacts.available=contactsOnline
		except:
			logging.exception("Unable to obtain contacts information.")

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin):
	checkedItemsDict={}

	def __init__(self, parent):
		wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT|wx.LC_SINGLE_SEL)
		CheckListCtrlMixin.__init__(self)
		self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated)

	def OnItemActivated(self, evt):
		self.ToggleItem(evt.m_itemIndex)

	def OnCheckItem(self, index, flag):
		if flag:
			CheckListCtrl.checkedItemsDict[index]=self.GetItem(index, 1).GetText()
			output.speak(_("Checked"))
		else:
			del CheckListCtrl.checkedItemsDict[index]
			output.speak(_("Unchecked"))
		if len(CheckListCtrl.checkedItemsDict)>1:
			if ButtonCall: ButtonCall.SetLabel(_("&Create Conference"))
			if ButtonChat: ButtonChat.SetLabel(_("Create multi c&hat"))
			if ButtonProfile: ButtonProfile.Enable(False)
		else: 
			if ButtonCall: ButtonCall.SetLabel(_("&Call"))
			if ButtonChat: ButtonChat.SetLabel(_("C&hat"))
			if ButtonProfile: ButtonProfile.Enable(True)

def loadContactList():
	logging.debug("Loading contact list.")
	try:
		contactsThread=contacts()
		contactsThread.daemon=True
		contactsThread.start()
		contactsThread.join()
	except:
		logging.exception("Unable to start contact load thread.")

class contactsManagerWindow(SizedDialog):

	def __init__(self, *args, **kwargs):
		loadContactList()
		self.contacts=contacts.available
		super(contactsManagerWindow, self).__init__(*args, **kwargs)
		self.selected=None
		self.index=None
		self.ListContacts=self.labeled_control(label=_("&Contact List"), control=CheckListCtrl)
		self.ListContacts.InsertColumn(0, _("Contact"), format=wx.LIST_FORMAT_LEFT, width=120)
		self.ListContacts.InsertColumn(1, _("Skype Name"), format=wx.LIST_FORMAT_LEFT, width=120)
		self.ListContacts.InsertColumn(2, _("Status"), format=wx.LIST_FORMAT_LEFT, width=120)
		self.ListContacts.InsertColumn(3, _("Mood Text"), format=wx.LIST_FORMAT_RIGHT, width=800)
		self.ListContacts.InsertColumn(4, _("Last seen"), format=wx.LIST_FORMAT_RIGHT, width=120)
		if len(self.contacts) != 0:
			for num, contact in enumerate(self.contacts):
				index = self.ListContacts.InsertStringItem(sys.maxint, extras.getPrintableUserName(contact.DisplayName, contact.FullName, contact.Handle))
				self.ListContacts.SetStringItem(index, 1, contact.Handle)
				self.ListContacts.SetStringItem(index, 2, contacts.lstOnlineStatusMessages[contacts.lstOnlineStatus.index(contact.OnlineStatus)])
				self.ListContacts.SetStringItem(index, 3, contact.MoodText)
				if contact.OnlineStatus==Skype4Py.olsOffline or contact.OnlineStatus==Skype4Py.olsInvisible:
					self.ListContacts.SetStringItem(index, 4, _("%s at %s")%(extras.getPrettyDate(contact.LastOnlineDatetime), contact.LastOnlineDatetime.strftime('%H:%M:%S')))
			self.ListContacts.SetItemData(index, num)
			self.ListContacts.SetMinSize((900, 210))
			self.ListContacts.SetSizerProps(expand=True)
			self.ListContacts.Select(0)
		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.ListContacts)
		self.Bind(wx.EVT_CLOSE, lambda evt: self.unload())
		self.SetEscapeId(wx.ID_CLOSE)
		self.finish_setup()

	def create_buttons(self):
		ButtonPanel = sc.SizedPanel(self.pane, -1)
		ButtonPanel.SetSizerType("horizontal")
		global ButtonCall
		ButtonCall=wx.Button(ButtonPanel, label=_("&Call"))
		ButtonCall.SetDefault()
		self.Bind(wx.EVT_BUTTON, self.onCallButtonClick, ButtonCall)
		global ButtonChat
		ButtonChat=wx.Button(ButtonPanel, label=_("C&hat"))
		self.Bind(wx.EVT_BUTTON, self.onChatButtonClick, ButtonChat)
		global ButtonProfile
		ButtonProfile=wx.Button(ButtonPanel, label=_("View &Profile..."))
		self.Bind(wx.EVT_BUTTON, self.onViewProfileButtonClick, ButtonProfile)
		ButtonClose=wx.Button(ButtonPanel, id=wx.ID_CLOSE)
		self.Bind(wx.EVT_BUTTON, self.onCloseButtonClick, ButtonClose)
		if len(self.contacts) == 0:
			ButtonCall.Hide()
			ButtonChat.Hide()
			ButtonProfile.Hide()

	def OnItemSelected(self, evt):
		self.index=evt.m_itemIndex
		self.selected=self.ListContacts.GetItem(evt.m_itemIndex, 1).GetText()
		if self.ListContacts.IsChecked(evt.m_itemIndex):
			output.speak(_("Checked"))

	def onCallButtonClick(self, evt):
		if len(CheckListCtrl.checkedItemsDict)>0:
			contacts=CheckListCtrl.checkedItemsDict.values()
		elif self.selected:
			contacts=[self.selected]
		if contacts:
			try:
				globalVars.Skype.PlaceCall(*contacts)
			except:
				pass
			self.unload()

	def onChatButtonClick(self, evt):
		if len(CheckListCtrl.checkedItemsDict)>0:
			contacts=CheckListCtrl.checkedItemsDict.values()
		else:
			contacts=[self.selected]
		if contacts:
			try:
				globalVars.Skype.CreateChatWith(*contacts).OpenWindow()
			except:
				pass
			self.unload()

	def onViewProfileButtonClick(self, evt):
		PV=ProfileViewerDialog(parent=self, contact=self.contacts[self.index])
		PV.Show()

	def onCloseButtonClick(self, evt):
		self.unload()

	def unload(self):
		if CheckListCtrl.checkedItemsDict:
			for x in CheckListCtrl.checkedItemsDict.keys():
				del CheckListCtrl.checkedItemsDict[x]
		self.Destroy()
		globalVars.Frame.CloseDialog(self)
