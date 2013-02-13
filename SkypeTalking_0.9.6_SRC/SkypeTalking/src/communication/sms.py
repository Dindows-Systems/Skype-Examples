#    communication/sms.py
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

from interface import smsDialog
import globalVars
import output
import versionInfo
import Skype4Py
import wx

def OnSmsStatus(self,status):
	lstSmsStatus = [Skype4Py.smsMessageStatusComposing, Skype4Py.smsMessageStatusDelivered, Skype4Py.smsMessageStatusFailed, Skype4Py.smsMessageStatusRead, Skype4Py.smsMessageStatusReceived, Skype4Py.smsMessageStatusSendingToServer, Skype4Py.smsMessageStatusSentToServer, Skype4Py.smsMessageStatusSomeTargetsFailed,Skype4Py.smsMessageStatusUnknown] 
	lstSmsStatusMessages= [_('Composing'), _('Delivered'), _('Sending Failed'), _('SMS read'), _('SMS received'), _('Sending to server'), _('Sent to server'), _('Unable to deliver to some numbers.'), _('Unknown')]
	output.speak("%s"%lstSmsStatusMessages[lstSmsStatus.index(status)])
	if status == Skype4Py.smsMessageStatusDelivered: 
		output.speak(_("You've paid %s")%globalVars.lastSmsSent.PriceToText)
		output.speak(_("Your Skype Credit Balance is %s")%globalVars.Skype.CurrentUserProfile.BalanceToText)

def smsSend(*args, **kwargs):
	dlg=wx.TextEntryDialog(globalVars.Frame, _("Enter Phone Number or numbers separated by semicolons:"), versionInfo.name+" - "+_("New SMS Wizard"))
	dlg.FindWindowById(3000).Bind(wx.EVT_KEY_DOWN, OnKeyDown)
	globalVars.Frame.DisplayDialog(dlg)
	s=dlg.ShowModal()
	while True and s != wx.ID_CANCEL:
		targets = ["+"+x.strip().replace("+","") for x in dlg.GetValue().split(";")]
		try:
			globalVars.currentSms = globalVars.Skype.CreateSms(Skype4Py.smsMessageTypeOutgoing, *targets)
			smsDialog.smsDialog(parent=globalVars.Frame, title=versionInfo.name+" - "+_("New SMS Wizard: from %s to %s")%(globalVars.currentSms.ReplyToNumber,"; ".join([x for x in globalVars.currentSms.TargetNumbers])))    
			break	
		except:
			output.speak(_("Invalid number. Please check your input and try again."))
			s=dlg.ShowModal()
			dlg.FindWindowById(3000).SetFocus()	
	globalVars.Frame.CloseDialog(dlg)

def OnKeyDown(evt):
		allowedKeys=tuple(range(48,58))+tuple(range(324,333))+(8,127,32,43,44,306,308)+tuple(range(312,3180))
		if evt.GetKeyCode()  in allowedKeys: evt.Skip()
