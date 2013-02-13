#    communication/voicemail.py
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

import globalVars
import events
import output
import Skype4Py

def OnVoicemail(mail, status):
	globalVars.voicemail=mail
	checkVoicemail()

def checkVoicemail(announce=True, inProgress=False):
	v=globalVars.voicemail
	if v.Type==Skype4Py.vmtIncoming:
		vmMessage=_("Voicemail from %s. ")%v.PartnerDisplayName
	elif v.Type==Skype4Py.vmtOutgoing:
		vmMessage=_("Voicemail to %s. ")%v.PartnerDisplayName
	elif v.Type==Skype4Py.vmtDefaultGreeting:
		vmMessage=_("Default greeting voicemail. ")
	elif v.Type==Skype4Py.vmtCustomGreeting:
		vmMessage=_("Custom greeting voicemail. ")
	elif v.Type==Skype4Py.vmtUnknown:
		vmMessage=_("Unknown voicemail type. ")
	if v.Status==Skype4Py.vmsUnknown:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Status unknown."), announce, True, inProgress)
	elif v.Status==Skype4Py.vmsNotDownloaded:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Not downloaded."), announce, True, inProgress)
	elif v.Status==Skype4Py.vmsDownloading:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Downloading..."), announce, True, inProgress)
	elif v.Status==Skype4Py.vmsUnplayed:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Not played, duration %d seconds.")%v.Duration, announce, True, inProgress)
	elif v.Status==Skype4Py.vmsBuffering:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Buffering..."), announce, True, inProgress)
	elif v.Status==Skype4Py.vmsPlaying:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Playing..."), announce, True, inProgress)
	elif v.Status==Skype4Py.vmsPlayed:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Played, duration %d seconds.")%v.Duration, announce, True, inProgress)
	elif v.Status==Skype4Py.vmsBlank:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Blank voicemail."), announce, True, inProgress)
	elif v.Status==Skype4Py.vmsRecording:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Recording..."), announce, True, inProgress)
	elif v.Status==Skype4Py.vmsRecorded:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Recorded."), announce, True, inProgress)
	elif v.Status==Skype4Py.vmsUploading:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Uploading..."), announce, True, inProgress)
	elif v.Status==Skype4Py.vmsUploaded:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Uploaded."), announce, True, inProgress)
	elif v.Status==Skype4Py.vmsDeleting:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Deleting..."), announce, True, inProgress)
	elif v.Status==Skype4Py.vmsFailed:
		events.registerNewEvent(events.EVT_VOICEMAIL, vmMessage+_("Voicemail error."), announce, True, inProgress)
	if v.FailureReason==Skype4Py.vmrNoError:
		output.speak(_("No error."))
	elif v.FailureReason==Skype4Py.vmrMiscError:
		output.speak(_("Miscellaneous error."))
	elif v.FailureReason==Skype4Py.vmrConnectError:
		output.speak(_("Couldn't connect."))
	elif v.FailureReason==Skype4Py.vmrNoPrivilege:
		output.speak(_("No voicemail privilege."))
	elif v.FailureReason==Skype4Py.vmrNoVoicemail:
		output.speak(_("No such voicemail."))
	elif v.FailureReason==Skype4Py.vmrFileReadError:
		output.speak(_("Couldn't read a file."))
	elif v.FailureReason==Skype4Py.vmrFileWriteError:
		output.speak(_("Couldn't write a file."))
	elif v.FailureReason==Skype4Py.vmrRecordingError:
		output.speak(_("Couldn't record voicemail."))
	elif v.FailureReason==Skype4Py.vmrPlaybackError:
		output.speak(_("Couldn't play voicemail."))
