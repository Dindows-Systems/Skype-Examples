#    interface/contactsManager/profileViewer.py
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

from gui_components.sized import SizedDialog
import extras
import wx
import wx.lib.sized_controls as sc

class ProfileViewerDialog(SizedDialog):

	def __init__(self, contact, *args, **kwargs):
		userName=extras.getPrintableUserName(contact.DisplayName, contact.FullName, contact.Handle)
		super(ProfileViewerDialog, self).__init__(*args, **kwargs)
		self.SetTitle(_("Profile Viewer for %s (%s)")%(userName, contact.Handle))
		self.SkypeName=self.labeled_control(_("Skype name:"), wx.TextCtrl, value=contact.Handle, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.FullName:
			self.FullName=self.labeled_control(_("Full name:"), wx.TextCtrl, value=contact.FullName, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.MoodText:
			self.MoodText=self.labeled_control(_("Mood:"), wx.TextCtrl, value=contact.MoodText, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.Birthday:
			self.Birthday=self.labeled_control(_("Birth date:"), wx.TextCtrl, value=contact.Birthday.strftime("%A, %d %B %Y"), style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.Sex and contact.Sex!="UNKNOWN":
			if contact.Sex=="MALE": gender=_("Male")
			elif contact.Sex=="FEMALE": gender=_("Female")
			self.Gender=self.labeled_control(_("Gender:"), wx.TextCtrl, value=gender, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.Language and contact.LanguageCode:
			language="%s (%s)"%(contact.Language, contact.LanguageCode)
			self.Language=self.labeled_control(_("Language:"), wx.TextCtrl, value=language, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.City or contact.Province or contact.Country:
			location="%s, %s, %s (%s)"%(contact.City, contact.Province, contact.Country, contact.CountryCode)
			self.Location=self.labeled_control(_("Location:"), wx.TextCtrl, value=location, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.PhoneHome:
			self.HomePhone=self.labeled_control(_("Home phone:"), wx.TextCtrl, value=contact.PhoneHome, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.PhoneOffice:
			self.OfficePhone=self.labeled_control(_("Office phone:"), wx.TextCtrl, value=contact.PhoneOffice, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.PhoneMobile:
			self.MobilePhone=self.labeled_control(_("Mobile phone:"), wx.TextCtrl, value=contact.PhoneMobile, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.Homepage:
			self.HomePage=self.labeled_control(_("Home page:"), wx.TextCtrl, value=contact.Homepage, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.About:
			self.AboutMe=self.labeled_control(_("About me:"), wx.TextCtrl, value=contact.About, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		if contact.NumberOfAuthBuddies!=0:
			numberOfContacts="%d"%contact.NumberOfAuthBuddies
			self.NumberOfContacts=self.labeled_control(_("Number of contacts:"), wx.TextCtrl, value=numberOfContacts, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
		OtherInfoList=[]
		if not contact.IsAuthorized:
			OtherInfoList.append(_("This user is not authorized to contact me.\n"))
		if contact.IsBlocked:
			OtherInfoList.append(_("This user is blocked.\n"))
		if not contact.HasCallEquipment:
			OtherInfoList.append(_("This user doesn't have a call equipment.\n"))
		if contact.IsCallForwardActive:
			OtherInfoList.append(_("This user has call forwarding activated.\n"))
		if contact.IsVideoCapable:
			OtherInfoList.append(_("This user has a camera.\n"))
		if contact.IsVoicemailCapable:
			OtherInfoList.append(_("This user can send and receive Voice Mail.\n"))
		if len(OtherInfoList)!=0:
			self.OtherInfo=self.labeled_control(_("Other information:"), wx.TextCtrl, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, -1))
			for line in OtherInfoList: self.OtherInfo.WriteText(line)
			self.OtherInfo.SetInsertionPoint(0)
		self.SetEscapeId(wx.ID_CLOSE)
		self.finish_setup()

	def create_buttons(self):
		ButtonPanel = sc.SizedPanel(self.pane, -1)
		ButtonPanel.SetSizerType("horizontal")
		self.CloseBTN=wx.Button(ButtonPanel, id=wx.ID_CLOSE)
		self.CloseBTN.SetDefault()
		self.Bind(wx.EVT_BUTTON, lambda evt: self.Destroy(), self.CloseBTN)
