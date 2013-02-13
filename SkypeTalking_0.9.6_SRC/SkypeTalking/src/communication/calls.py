#    communication/calls.py
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
logging=logger.getChild('communication.calls')
import events
import globalVars
import output
import Skype4Py

def OnCall(call, status):
	globalVars.call=call
	checkCall()

def checkCall(announce=True, inProgress=False):
	c=globalVars.call
	if c.Status==Skype4Py.clsRinging and c.Type==Skype4Py.cltIncomingP2P:
		events.registerNewEvent(events.EVT_CALLS, _("Call from %s")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsRinging and c.Type==Skype4Py.cltOutgoingP2P:
		events.registerNewEvent(events.EVT_CALLS, _("Calling %s")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsRinging and c.Type==Skype4Py.cltIncomingPSTN:
		events.registerNewEvent(events.EVT_CALLS, _("Phone call from %s")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsRinging and c.Type==Skype4Py.cltOutgoingPSTN:
		events.registerNewEvent(events.EVT_CALLS, _("Phone call to %s")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsFinished:
		events.registerNewEvent(events.EVT_CALLS, _("Call with %s finished, duration %s.")%(c.PartnerDisplayName, duration2str(c.Duration)), announce, True, inProgress)
		call = None
	elif c.Status==Skype4Py.clsRouting:
		events.registerNewEvent(events.EVT_CALLS, _("Calling %s, routing...")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsFailed:
		events.registerNewEvent(events.EVT_CALLS, _("Sorry, call with %s failed")%c.PartnerDisplayName, announce, True, inProgress)
		callerName = None
	elif c.Status==Skype4Py.clsInProgress:
		events.registerNewEvent(events.EVT_CALLS, _("Call with %s in progress")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsOnHold:
		events.registerNewEvent(events.EVT_CALLS, _("Call with %s on hold")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsMissed:
		events.registerNewEvent(events.EVT_CALLS, _("Missed call from %s")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsRefused:
		events.registerNewEvent(events.EVT_CALLS, _("Call refused"), announce, True, inProgress)
	elif c.Status==Skype4Py.clsBusy:
		events.registerNewEvent(events.EVT_CALLS, _("Call with %s, busy")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsCancelled:
		events.registerNewEvent(events.EVT_CALLS, _("Call with %s, cancelled")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsLocalHold:
		events.registerNewEvent(events.EVT_CALLS, _("Call with %s on local hold")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsRemoteHold:
		events.registerNewEvent(events.EVT_CALLS, _("Call with %s on remote hold")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsTransferring:
		events.registerNewEvent(events.EVT_CALLS, _("Transferring call to %s")%c.PartnerDisplayName, announce, True, inProgress)
	elif c.Status==Skype4Py.clsTransferred:
		events.registerNewEvent(events.EVT_CALLS, _("Call transferred to %s")%c.PartnerDisplayName, announce, True, inProgress)
	if c.FailureReason==Skype4Py.cfrUnknown:
		output.speak(_("Reason unknown"))
	elif c.FailureReason==Skype4Py.cfrMiscError:
		output.speak(_("Misc error"))
	elif c.FailureReason==Skype4Py.cfrUserDoesNotExist:
		output.speak(_("User does not exist"))
	elif c.FailureReason==Skype4Py.cfrUserIsOffline:
		output.speak(_("User is offline"))
	elif c.FailureReason==Skype4Py.cfrNoProxyFound:
		output.speak(_("No Proxy found"))
	elif c.FailureReason==Skype4Py.cfrSessionTerminated:
		output.speak(_("Session terminated"))
	elif c.FailureReason==Skype4Py.cfrNoCommonCodec:
		output.speak(_("No common codec"))
	elif c.FailureReason==Skype4Py.cfrSoundIOError:
		output.speak(_("Sound input/output error"))
	elif c.FailureReason==Skype4Py.cfrRemoteDeviceError:
		output.speak(_("Remote device error"))
	elif c.FailureReason==Skype4Py.cfrBlockedByRecipient:
		output.speak(_("You are blocked by recipient"))
	elif c.FailureReason==Skype4Py.cfrRecipientNotFriend:
		output.speak(_("The recipient is not in your contact list"))
	elif c.FailureReason==Skype4Py.cfrNotAuthorizedByRecipient:
		output.speak(_("You are not authorized by recipient"))
	elif c.FailureReason==Skype4Py.cfrSoundRecordingError:
		output.speak(_("Sound recording error"))

def duration2str(duration):
	from time import gmtime
	(hours,minutes,seconds) = gmtime(0+duration)[3:6]
	text=u''
	if hours: text=text+("%d %s"%(hours,(_('hour '),_('hours '))[(hours  > 1)])) 
	if minutes: text=text+'%s '%('',_('and '))[(bool(hours and minutes) and not seconds)]+("%d %s"%(minutes,(_('minute '),_('minutes '))[(minutes  > 1)]))  
	if seconds: text=text+'%s '%('',_('and '))[(bool(hours or minutes))]+("%d %s"%(seconds,(_('second'),_('seconds'))[(seconds> 1)]))  
	return text
