#    interface/preferences/categories/hotKeys.py
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

from baseCategory import BaseCategory
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
from gui_components.sized import SizedDialog
import config
import sys
import wx

### Globals
KeystrokeList=None
selected=0
function=None
### EndGlobals

class KeystrokeListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):

	def __init__(self, parent):
		wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
		ListCtrlAutoWidthMixin.__init__(self)

class hotKeysCategory(BaseCategory):

	def __init__(self, *args, **kwargs):
		super(hotKeysCategory, self).__init__(*args, **kwargs)
		global KeystrokeList
		import interface.commands
		self.iCommands = interface.commands.interfaceCommands()
		wx.StaticText(parent=self, label=_("&Keystrokes"))
		self._first=KeystrokeList=KeystrokeListCtrl(self)
		KeystrokeList.InsertColumn(0, _("Function"))
		KeystrokeList.InsertColumn(1, _("Keystroke"))
		KeystrokeList.InsertColumn(2, _("Description"))
		for func, hotkey in sorted(config.conf['hotkeys'].iteritems()):
			index=KeystrokeList.InsertStringItem(sys.maxint, func)
			KeystrokeList.SetStringItem(index, 1, hotkey)
			try:
				doc=getattr(self.iCommands, func).__doc__
				KeystrokeList.SetStringItem(index, 2, doc)
			except:
				KeystrokeList.SetStringItem(index, 2, _("No description"))
		KeystrokeList.Select(0)
		KeystrokeList.SetMinSize((360, 160))
		KeystrokeList.SetSizerProps(expand=True)
		ChangeButton=wx.Button(parent=self, label=_("&Change..."))
		self.Bind(wx.EVT_BUTTON, self.onChangeButtonClicked, ChangeButton)
		self.finishSetup()

	def onChangeButtonClicked(self, evt):
		global selected
		selected=KeystrokeList.GetFirstSelected()
		text=KeystrokeList.GetItem(selected, 0).GetText()
		changeKeystrokeDialog(parent=self, title=_("Change keystroke for %s")%text)

class changeKeystrokeDialog(SizedDialog):

	def __init__(self, *args, **kwargs):
		super(changeKeystrokeDialog, self).__init__(*args, **kwargs)
		global function
		function=KeystrokeList.GetItem(selected, 0).GetText()
		OldKeystroke=config.conf["hotkeys"][function].split('+')
		self.Key=self.labeled_control(_("&Key:"), wx.TextCtrl)
		self.Key.SetSizerProps(expand=True)
		wx.StaticBox(parent=self.pane, label=_("Modifiers"))
		self.AltKeyCheckBox=wx.CheckBox(parent=self.pane, label="&Alt")
		self.WinKeyCheckBox=wx.CheckBox(parent=self.pane, label="&Win")
		self.CtrlKeyCheckBox=wx.CheckBox(parent=self.pane, label="&Control")
		self.ShiftKeyCheckBox=wx.CheckBox(parent=self.pane, label="&Shift")
		if 'alt'.lower() in OldKeystroke:
			self.AltKeyCheckBox.SetValue(True)
		if 'win'.lower() in OldKeystroke:
			self.WinKeyCheckBox.SetValue(True)
		if 'control'.lower() in OldKeystroke:
			self.CtrlKeyCheckBox.SetValue(True)
		if 'shift'.lower() in OldKeystroke:
			self.ShiftKeyCheckBox.SetValue(True)
		self.Key.SetValue(OldKeystroke[-1])
		self.finish_setup()
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Show()

	def onOk(self, evt):
		global KeystrokeList
		ModKeyDelimiter='+'
		ModKey=[]
		if self.CtrlKeyCheckBox.GetValue():
			ModKey.append("control")
		if self.AltKeyCheckBox.GetValue():
			ModKey.append("alt")
		if self.WinKeyCheckBox.GetValue():
			ModKey.append("win")
		if self.ShiftKeyCheckBox.GetValue():
			ModKey.append("shift")
		ModKey.append(self.Key.GetValue())
		NewKeystroke=ModKeyDelimiter.join(ModKey)
		if NewKeystroke in config.conf["hotkeys"].values():
			wx.MessageBox(_("%s keystroke already in use. Please try another one.")%NewKeystroke, _("Change Keystroke Error"), wx.OK|wx.ICON_ERROR)
			return
		config.conf["hotkeys"][function]=NewKeystroke
		KeystrokeList.SetStringItem(selected, 1, NewKeystroke)
		self.Destroy()
