#    interface/smsDialog.py
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
import globalVars
import output
import Skype4Py
import tones
import wx
import wx.lib.sized_controls as sc

class smsDialog(SizedDialog):

	def __init__(self, *args, **kwargs):
		super(smsDialog, self).__init__(*args, **kwargs)
		self.messageEdit=self.labeled_control(_("Message text:"), wx.TextCtrl, style=wx.TE_MULTILINE, size=(500, 100))
		self.messageEdit.SetMaxLength(616)
		self.messageEdit.Bind(wx.EVT_KEY_DOWN, self.OnChar)
		self.messageEdit.Bind(wx.EVT_TEXT, self.updateMessageBody)
		self.finish_setup()
		globalVars.Frame.DisplayDialog(self)

	def create_buttons(self):
		ButtonPanel = sc.SizedPanel(self.pane, -1)
		ButtonPanel.SetSizerType("horizontal")
		self.ButtonSend=wx.Button(ButtonPanel, id=wx.ID_OK, label=_("&Send"))
		self.Bind(wx.EVT_BUTTON, self.onSendButton, self.ButtonSend)
		self.ButtonCancel=wx.Button(ButtonPanel, id=wx.ID_CANCEL)
		self.Bind(wx.EVT_BUTTON, self.onCancelButtonClick, self.ButtonCancel)

	def onSendButton(self, evt):
		try:
			globalVars.currentSms.Send() 
			globalVars.Frame.CloseDialog(self)
		except Skype4Py.SkypeError as (errno, strerr):
			output.speak(_("SMS sending failed."))

	def onCancelButtonClick(self, evt):
		globalVars.currentSms.Delete()
		globalVars.Frame.CloseDialog(self)

	def OnChar(self, evt):
		evt.Skip()
		if evt.GetKeyCode()==wx.WXK_F2:  
			if globalVars.currentSms.Chunks.Count: 
				output.speak(_("SMS %d, %d characters left, Current price %s.")%(globalVars.currentSms.Chunks.Count,globalVars.currentSms.Chunks[-1].CharactersLeft,globalVars.currentSms.PriceToText))
			else:
				output.speak(_("Empty"))

	def updateMessageBody(self, evt):
		globalVars.currentSms.Body = self.messageEdit.GetValue()
		if globalVars.currentSms.Chunks.Count:
			if globalVars.currentSms.Chunks[-1].CharactersLeft == 0: tones.makeWarningBeep()
