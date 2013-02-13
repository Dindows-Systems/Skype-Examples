#    communication/files.py
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
logging=logger.getChild('communication.files')
import config
import events
import globalVars
import output
import Skype4Py
import time

def OnFileTransfer(file, status):
	globalVars.transferringFile=file
	checkFileTransfer()

def checkFileTransfer(announce=True, inProgress=False):
	f=globalVars.transferringFile
	file, user=f.FileName.decode("mbcs"), f.PartnerDisplayName
	if f.Type==Skype4Py.fileTransferTypeIncoming:
		ftMessage=_("Receiving file %s from %s. ")%(file,user)
	elif f.Type==Skype4Py.fileTransferTypeOutgoing:
		ftMessage=_("Sending file %s to %s. ")%(file,user)
	else:
		ftMessage=_("File transfer %s, file %s. ")%(file,user)
	if f.Status==Skype4Py.fileTransferStatusNew:
		events.registerNewEvent(events.EVT_FILES, _("New file transfer: ")+ftMessage, announce, True, inProgress)
	if f.Status==Skype4Py.fileTransferStatusConnecting:
		events.registerNewEvent(events.EVT_FILES, ftMessage+_("Connecting..."), announce, True, inProgress)
	if f.Status==Skype4Py.fileTransferStatusTransferring:
		events.registerNewEvent(events.EVT_FILES, ftMessage+_("Transferring..."), announce, True, inProgress)
	if f.Status==Skype4Py.fileTransferStatusTransferringOverRelay:
		events.registerNewEvent(events.EVT_FILES, ftMessage+_("Transferring over relay..."), announce, True, inProgress)
	if f.Status==Skype4Py.fileTransferStatusWaitingForAccept:
		events.registerNewEvent(events.EVT_FILES, ftMessage+_("Waiting for accept..."), announce, True, inProgress)
	if f.Status==Skype4Py.fileTransferStatusPaused:
		events.registerNewEvent(events.EVT_FILES, ftMessage+_("Paused."), announce, True, inProgress)
	if f.Status==Skype4Py.fileTransferStatusRemotelyPaused:
		events.registerNewEvent(events.EVT_FILES, ftMessage+_("Paused remotely."), announce, True, inProgress)
	if f.Status==Skype4Py.fileTransferStatusCancelled:
		events.registerNewEvent(events.EVT_FILES, ftMessage+_("Cancelled!"), announce, True, inProgress)
	if f.Status==Skype4Py.fileTransferStatusCompleted:
		events.registerNewEvent(events.EVT_FILES, ftMessage+_("Finished!"), announce, True, inProgress)
	if f.Status==Skype4Py.fileTransferStatusFailed:
		events.registerNewEvent(events.EVT_FILES, ftMessage+_("File transfer failed."), announce, True, inProgress)
	if f.FailureReason==Skype4Py.fileTransferFailureReasonSenderNotAuthorized:
		output.speak(_("Sender not authorized."))
	if f.FailureReason==Skype4Py.fileTransferFailureReasonRemotelyCancelled:
		output.speak(_("Remotely cancelled."))
	if f.FailureReason==Skype4Py.fileTransferFailureReasonFailedRead:
		output.speak(_("Failed read."))
	if f.FailureReason==Skype4Py.fileTransferFailureReasonFailedRemoteRead:
		output.speak(_("Failed remote read."))
	if f.FailureReason==Skype4Py.fileTransferFailureReasonFailedWrite:
		output.speak(_("Failed write."))
	if f.FailureReason==Skype4Py.fileTransferFailureReasonFailedRemoteWrite:
		output.speak(_("Failed remote write."))
	if f.FailureReason==Skype4Py.fileTransferFailureReasonRemoteDoesNotSupportFT:
		output.speak(_("Remote does not support file transfer."))
	if f.FailureReason==Skype4Py.fileTransferFailureReasonRemoteOfflineTooLong:
		output.speak(_("Remote offline too long."))

def getFileSize():
	file=globalVars.transferringFile
	if file:
		return output.speak(_("Size: %.1f Mb")%((file.FileSize/1024.0)/1024.0))

def getFileTransferSpeed():
	file=globalVars.transferringFile
	if file:
		return output.speak(_("Transferred: %.1f Mb, Speed: %.1f kb/s")%((file.BytesTransferred/1024.0)/1024.0, file.BytesPerSecond/1024.0))

def getFileTransferProgress():
	file=globalVars.transferringFile
	try:
		progress=(float(file.BytesTransferred)/file.FileSize)*100
		return output.speak(_("Progress: %6.2f")%(progress)+"%")
	except ZeroDivisionError:
		return

def getFileTransferTimeLeft():
	finishTime=globalVars.transferringFile.FinishTime
	if finishTime:
		finishTime=int(finishTime-time.time())
		minutes,seconds=divmod(finishTime, 60)
		hours,minutes=divmod(minutes, 60)
		return output.speak(_("Time left: %d hours, %d minutes and %d seconds")%(hours, minutes, seconds))
