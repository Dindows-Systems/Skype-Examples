#    communication/main.py
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
logging=logger.getChild('communication.main')
import calls, messages, files, status, sms, users, voicemail
import config
import extras
import globalVars
import interface
import output
import Skype4Py
import time
import updater
import versionInfo
import wx

def OnAttach(status):
	globalVars.attachStatus=status
	if status == Skype4Py.apiAttachPendingAuthorization:
		output.speak(_("Waiting for authorization..."), True)
	if status == Skype4Py.apiAttachRefused:
		output.speak(_("Authorization refused."))
		retryConnection()
	if status == Skype4Py.apiAttachAvailable:
		globalVars.Skype.Attach()
	if status == Skype4Py.apiAttachNotAvailable:
		output.speak(_("Error, API not available."))
		retryConnection()
	if status == Skype4Py.apiAttachSuccess:
		try:
			userName=extras.getPrintableUserName(globalVars.Skype.CurrentUser.DisplayName, globalVars.Skype.CurrentUser.FullName, globalVars.Skype.CurrentUser.Handle)
		except Skype4Py.errors.SkypeAPIError:
			retryConnection()
		output.speak(_("%s is ready. Currently logged on user is %s.")%(versionInfo.name, userName), True)
		try:
			globalVars.call=globalVars.Skype.ActiveCalls[-1]
		except IndexError: pass
		try:
			globalVars.transferringFile=globalVars.Skype.ActiveFileTransfers[-1]
		except IndexError: pass
		try:
			globalVars.voicemail=globalVars.Skype.Voicemails[-1]
		except IndexError: pass
		wx.CallAfter(updater.autoUpdate)

def retryConnection():
	"""Tries to establish a Connection to Skype for configured amount of retries."""
	retries=config.conf['advanced']['connectionRetries']
	for retry in range(retries):
		currentConnectionRetry=retry+1
		output.speak(_("Error! Skype attach timeout. Making retry %d of %d for 5 seconds.")%(currentConnectionRetry, retries))
		time.sleep(5.000)
		try:
			globalVars.Skype.Attach()
			break
		except Skype4Py.errors.SkypeAPIError:
			if currentConnectionRetry>retries:
				output.speak(_("Error! Skype attach timeout. Please restart the application and try again. Exiting."))
				interface.shutdown(silent=True)
			else:
				continue

def initialize():
	#Register event handlers
	globalVars.Skype.RegisterEventHandler('AttachmentStatus', OnAttach)
	globalVars.Skype.RegisterEventHandler('CallStatus', calls.OnCall)
	globalVars.Skype.RegisterEventHandler('FileTransferStatusChanged', files.OnFileTransfer)
	globalVars.Skype.RegisterEventHandler('MessageStatus', messages.OnMessage)
	globalVars.Skype.RegisterEventHandler('SmsMessageStatusChanged', sms.OnSmsStatus)
	globalVars.Skype.RegisterEventHandler('UserAuthorizationRequestReceived', users.OnAuthRequest)
	globalVars.Skype.RegisterEventHandler('UserMood', users.OnUserMood)
	globalVars.Skype.RegisterEventHandler('VoicemailStatus', voicemail.OnVoicemail)
	globalVars.Skype.RegisterEventHandler('OnlineStatus', status.OnOnlineStatus)
	#Set friendly name and start the client application if needed
	globalVars.Skype.FriendlyName="%s %s"%(versionInfo.name, versionInfo.version[0])
	if not globalVars.Skype.Client.IsRunning and config.conf['general']['autoStartSkype']==True:
		try:
			globalVars.Skype.Client.Start(Minimized=config.conf['advanced']['startSkypeMinimized'], Nosplash=config.conf['advanced']['noSplashScreen'])
		except:
			logging.exception("Error starting Skype client.")
	#Try attaching the Skype client
	try:
		globalVars.Skype.Attach()
		while globalVars.Skype.AttachmentStatus==Skype4Py.apiAttachUnknown:
			globalVars.Skype.Attach()
	except Skype4Py.errors.SkypeAPIError:
		retryConnection()
