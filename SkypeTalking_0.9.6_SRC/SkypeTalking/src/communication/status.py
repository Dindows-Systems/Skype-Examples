#    communication/status.py
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
logging=logger.getChild('communication.status')
from collections import OrderedDict
import config
import events
import extras
import main
import globalVars
import output
import Skype4Py
import wx

def statusNames():
	statusDict=OrderedDict([
		(Skype4Py.cusOnline, _('Online')),
		(Skype4Py.cusAway, _('Away')),
		(Skype4Py.cusNotAvailable, _('Not Available')),
		(Skype4Py.cusDoNotDisturb, _('Do not disturb')),
		(Skype4Py.cusInvisible, _('Invisible')),
		(Skype4Py.cusSkypeMe, _('Skype Me')),
		(Skype4Py.cusOffline, _('Offline'))])
	return statusDict

def OnOnlineStatus(user, status):
	userName=extras.getPrintableUserName(user.DisplayName, user.FullName, user.Handle)
	if status==Skype4Py.olsUnknown:
		events.registerNewEvent(events.EVT_STATUSCHANGES, _("%s's status is unknown")%userName, announce=config.conf['alerts']['onlineStatusUnknown'])
	elif status==Skype4Py.olsOffline:
		events.registerNewEvent(events.EVT_STATUSCHANGES, _("%s went Offline")%userName, announce=config.conf['alerts']['onlineStatusOffline'])
	elif status==Skype4Py.olsOnline:
		events.registerNewEvent(events.EVT_STATUSCHANGES, _("%s is Online")%userName, announce=config.conf['alerts']['onlineStatusOnline'])
	elif status==Skype4Py.olsAway:
		events.registerNewEvent(events.EVT_STATUSCHANGES, _("%s is Away")%userName, announce=config.conf['alerts']['onlineStatusAway'])
	elif status==Skype4Py.olsNotAvailable:
		events.registerNewEvent(events.EVT_STATUSCHANGES, _("%s is Not Available")%userName, announce=config.conf['alerts']['onlineStatusNotAvailable'])
	elif status==Skype4Py.olsDoNotDisturb:
		events.registerNewEvent(events.EVT_STATUSCHANGES, _("%s is Do Not Disturb")%userName, announce=config.conf['alerts']['onlineStatusDoNotDisturb'])
	elif status==Skype4Py.olsInvisible:
		events.registerNewEvent(events.EVT_STATUSCHANGES, _("%s went offline")%userName, announce=config.conf['alerts']['onlineStatusInvisible'])
	elif status==Skype4Py.olsSkypeMe:
		events.registerNewEvent(events.EVT_STATUSCHANGES, _("%s is Skype Me")%userName, announce=config.conf['alerts']['onlineStatusSkypeMe'])
	elif status==Skype4Py.olsSkypeOut:
		events.registerNewEvent(events.EVT_STATUSCHANGES, _("%s is Skype Out")%userName, announce=config.conf['alerts']['onlineStatusSkypeOut'])

def changeStatus():
	changeStatusDLG=wx.SingleChoiceDialog(globalVars.Frame, _("Select status"), _("Change Status"), choices=statusNames().values())
	globalVars.Frame.DisplayDialog(changeStatusDLG)
	#Set selection to the current user status
	for num, status in enumerate(statusNames().keys()):
		if globalVars.Skype.CurrentUser.OnlineStatus==status:
			changeStatusDLG.SetSelection(num)
	answer=changeStatusDLG.ShowModal()
	if answer==wx.ID_OK:
		index=changeStatusDLG.GetSelection()
		globalVars.Frame.CloseDialog(changeStatusDLG)
		output.speak(_("Changing status to %s")%statusNames().values()[index], True)
		globalVars.Skype.ChangeUserStatus(statusNames().keys()[index])
	else:
		globalVars.Frame.CloseDialog(changeStatusDLG)

def reportUserStatus(*args, **kwargs):
	for this in statusNames().keys():
		if globalVars.Skype.CurrentUser.OnlineStatus==this:
			output.speak(_("Current online status is %s")%statusNames()[this])
