#    communication/misc.py
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
logging=logger.getChild('communication.misc')
from datetime import datetime
import calls
import files
import messages
import voicemail
import config
import extras
import globalVars
import output
import Skype4Py
import versionInfo
import wx

def SkypeVersionInfo(*args, **kwargs):
	output.speak(_("Skype client version %s")%globalVars.Skype.Version)

def APIWrapperVersionInfo(*args, **kwargs):
	output.speak(_("API wrapper version %s")%globalVars.Skype.ApiWrapperVersion)

def repeatLastEvent(*args, **kwargs):
	if not globalVars.lastEvent:
		output.speak(_("No new events since you've launched %s.")%versionInfo.name)
	else:
		output.speak(globalVars.lastEvent)

def repeatLastChatMessage(action, *args, **kwargs):
	if not globalVars.lastChatMessage:
		output.speak(_("No new messages since you've launched %s.")%versionInfo.name)
		return
	elif action=="repeatOnly":
		messages.speakChatMessage(globalVars.lastChatMessage, True)
	elif action == "activateChatMonitorAndWindow":
		globalVars.lastChatMessage.Chat.OpenWindow()
		globalVars.chatMonitor = globalVars.lastChatMessage.Chat

def getFileTransferStatus(*args, **kwargs):
	file=globalVars.transferringFile
	if file:
		files.checkFileTransfer(False, True)
	if not globalVars.fileTransferEvent:
		output.speak(_("There are no new file transfers yet."))
	else:
		output.speak(globalVars.fileTransferEvent)
	if file and file.Status in (Skype4Py.fileTransferStatusTransferring, Skype4Py.fileTransferStatusTransferringOverRelay, Skype4Py.fileTransferStatusPaused, Skype4Py.fileTransferStatusRemotelyPaused):
		files.getFileSize()
		files.getFileTransferProgress()
		files.getFileTransferSpeed()
		files.getFileTransferTimeLeft()

def getActiveFileTransfers(*args, **kwargs):
	AFT=globalVars.Skype.ActiveFileTransfers
	if len(AFT)==0:
		return output.speak(_("No active file transfers."))
	lstActiveFileTransfersDisplay=[]
	for f in AFT:
		lstActiveFileTransfersDisplay.append(_("%s, file %s")%(f.PartnerDisplayName, f.FileName.decode("mbcs")))
	activeFileTransfersDLG=wx.SingleChoiceDialog(globalVars.Frame, _("Select file sender/receiver"), _("Active File Transfers"), choices=lstActiveFileTransfersDisplay)
	globalVars.Frame.DisplayDialog(activeFileTransfersDLG)
	activeFileTransfersDLG.SetSelection(0)
	answer=activeFileTransfersDLG.ShowModal()
	if answer==wx.ID_OK:
		globalVars.transferringFile=AFT[activeFileTransfersDLG.GetSelection()]
		globalVars.Frame.CloseDialog(activeFileTransfersDLG)
		files.checkFileTransfer(False, True)
	else:
		globalVars.Frame.CloseDialog(activeFileTransfersDLG)

def reportCreditBalance(*args, **kwargs):
	output.speak(_("Your Skype Credit Balance is %s")%globalVars.Skype.CurrentUserProfile.BalanceToText)

def selectChatMonitor(action, number):
	if globalVars.Skype.ActiveChats:
		if number>=globalVars.Skype.ActiveChats.Count: output.speak(_("No chat Monitor at this position, the first is at position %s.")%(globalVars.Skype.ActiveChats.Count))
		elif action == "select":
			globalVars.chatMonitor=globalVars.Skype.ActiveChats.Item(number)
			if globalVars.chatMonitor.Type != Skype4Py.chatTypeMultiChat:
				output.speak(_("Monitoring chat with %s")%(globalVars.chatMonitor.DialogPartner))	
			else:
				output.speak(_("Monitoring chat with %s")%" ".join([("" if member==globalVars.Skype.CurrentUser else  ((member.FullName or member.Handle)  if member != globalVars.chatMonitor.Members[-1] else _('and')+' '+(member.FullName or member.Handle))) for member in globalVars.chatMonitor.Members]))
		elif action == "open":
			globalVars.Skype.ActiveChats.Item(number).OpenWindow()
	else:
		output.speak(_("no active chats"))

def openMonitoredChat(*args, **kwargs):
	if globalVars.chatMonitor:
		globalVars.chatMonitor.OpenWindow() 
	else:
		output.speak(_("no active chat monitor"))

def reportChatMonitor(*args, **kwargs):
	if globalVars.chatMonitor:
		if globalVars.chatMonitor.Type != Skype4Py.chatTypeMultiChat:
			output.speak(_("monitor on chat with %s")%(globalVars.chatMonitor.DialogPartner))
		else:
			output.speak(_("monitor on chat with %s")%" ".join([("" if member==globalVars.Skype.CurrentUser else  ((member.FullName or member.Handle)  if member != globalVars.chatMonitor.Members[-1] else _('and')+' '+(member.FullName or member.Handle))) for member in globalVars.chatMonitor.Members]))
	else:
		output.speak(_("no active chat monitor"))

def handleChatMessage(task, numberOfMessage = 0,*args):
	lastTenCusMessages = None 
	if globalVars.chatMonitor: lastTenCusMessages=globalVars.chatMonitor.Messages
	if not lastTenCusMessages:
		output.speak(_("No new messages since %s loaded or no chat Monitor selected yet.")%versionInfo.name)
		return
	elif numberOfMessage>=len(lastTenCusMessages):
		output.speak(_("no message at this position. The first is at position %d")%(len(lastTenCusMessages)))
		return
	if task=='readMessage':
		try:
			messages.speakChatMessage(lastTenCusMessages[numberOfMessage], True)
		except:
			pass
	elif task=='copyMessage':
		messages.messageToClipboard(lastTenCusMessages[numberOfMessage])
	elif task=='searchForAddresses':
		messages.searchForURL(lastTenCusMessages[numberOfMessage])

def reportMoodText(*args, **kwargs):
	if not globalVars.Skype.CurrentUser.MoodText: output.speak(_("No mood text set. Press this command twice to set one."))
	else: output.speak(_("The current mood text is: %s.")%(globalVars.Skype.CurrentUser.MoodText))

def changeMoodText(self,*args):
	currentMoodText=globalVars.Skype.CurrentUser.MoodText
	moodTextDLG=wx.TextEntryDialog(globalVars.Frame, _("Enter your new mood text:"), versionInfo.name+_(" - Change Mood Text"))
	if currentMoodText: moodTextDLG.SetValue(currentMoodText)
	globalVars.Frame.DisplayDialog(moodTextDLG)
	moodTextDLG.ShowModal()
	if moodTextDLG.GetValue and moodTextDLG.GetValue()!=currentMoodText:
		globalVars.Skype.CurrentUserProfile._SetMoodText(moodTextDLG.GetValue())
		if not config.conf["alerts"]["userChangedMoodText"]:
			output.speak(_("%s has changed his/her mood text to: %s")%(globalVars.Skype.CurrentUser.FullName, moodTextDLG.GetValue()), True)
	globalVars.Frame.CloseDialog(moodTextDLG)

def handleCall(action, *args):
	if globalVars.Skype.ActiveCalls.Count:
		call=globalVars.Skype.ActiveCalls[-1]
	else:
		call=None
	if action == 'finish':
		try:
			globalVars.voicemail.StopRecording()
		except:
			pass
		try:
			call.Finish()
		except:
			output.speak(_("no active call"))
	elif action == 'silentMic':
		if not globalVars.call:
			return output.speak(_("Not on call."))
		elif globalVars.call.InputDevice() == {}:
			try:
				globalVars.call.InputDevice(Skype4Py.callIoDeviceTypeSoundcard, 'Default')
				output.speak(_("Microphone unmuted"))
			except:
				output.speak(_("Not on call."))
		else:
			try:
				globalVars.call.InputDevice(Skype4Py.callIoDeviceTypeSoundcard, None)
				output.speak(_("Microphone muted"))
			except:
				output.speak(_("Not on call."))
	elif action == 'answerHoldResume':
		if call and call.Status == Skype4Py.clsRinging:
			call.Answer()
		elif call and call.Status == Skype4Py.clsInProgress:
			call.Hold()
			output.speak(_("call on hold "))
		elif call and call.Status == "LOCALHOLD":
			call.Resume()
			output.speak(_("call resumed"))
		else:
			output.speak(_("No incoming or active call."))
	elif action == 'join':
		if globalVars.Skype.ActiveCalls.Count<1:
			return output.speak(_("Not on call."))
		elif globalVars.Skype.ActiveCalls.Count>1:
			globalVars.Skype.ActiveCalls[0].Join(globalVars.Skype.ActiveCalls[1].Id)
			output.speak(_("%s has joined the current call.")%globalVars.Skype.ActiveCalls[0].PartnerDisplayName, True)
		else:
			output.speak(_("only one active call"))

def reportCallDuration(*args):
	if globalVars.Skype.ActiveCalls.Count:
		output.speak(calls.duration2str(globalVars.Skype.ActiveCalls[-1].Duration))
	else:
		output.speak(_("no active call"))

def GetDeviceStatus():
	AudioIn=globalVars.Skype.Settings.AudioIn
	AudioOut=globalVars.Skype.Settings.AudioOut
	VideoIn=globalVars.Skype.Settings.VideoIn
	Ringer=globalVars.Skype.Settings.Ringer
	if not AudioIn: AudioIn=_("Not available")
	if not AudioOut: AudioOut=_("Not available")
	if not VideoIn: VideoIn=_("Not available")
	if not Ringer: Ringer=_("Not available")
	output.speak(_("Audio In: %s")%AudioIn)
	output.speak(_("Audio Out: %s")%AudioOut)
	output.speak(_("Video In: %s")%VideoIn)
	output.speak(_("Ringing device: %s")%Ringer)

def getCallStatus(*args, **kwargs):
	call=globalVars.call
	if call:
		calls.checkCall(False, True)
	if call and globalVars.call.InputDevice()=={}:
		output.speak(_("Microphone muted"))
	if not globalVars.callStatusEvent:
		return output.speak(_("There are no new calls or calls in progress. Press this command twice to call someone."))
	else:
		output.speak(globalVars.callStatusEvent)

def makeCallDialog(*args, **kwargs):
	makeCallDLG=wx.TextEntryDialog(globalVars.Frame, _("Enter user's Skype name or names separated by commas:"), versionInfo.name+_(" - make call"))
	globalVars.Frame.DisplayDialog(makeCallDLG)
	res=makeCallDLG.ShowModal()
	if res==wx.ID_OK and makeCallDLG.GetValue():
		if ',' in makeCallDLG.GetValue():
			callList=makeCallDLG.GetValue().split(',')
			globalVars.Skype.PlaceCall(*callList)
		elif ';' in makeCallDLG.GetValue():
			callList=dlg.GetValue().split(';')
			globalVars.Skype.PlaceCall(*callList)
		else:
			globalVars.Skype.PlaceCall(makeCallDLG.GetValue())
	globalVars.Frame.CloseDialog(makeCallDLG)

def handleVoicemail(action, *args):
	vm=globalVars.voicemail
	if vm:
		voicemail.checkVoicemail(False, True)
	if action == 'getStatus':
		if not globalVars.voicemailEvent:
			return output.speak(_("There are no voicemails."))
		else:
			return output.speak(globalVars.voicemailEvent)
	elif action == 'open':
		if vm:
			try:
				vm.Open()
			except:
				output.speak(_("Error, cannot open that voicemail."))
		else:
			return output.speak(_("No voicemail to play."))
	elif action == 'delete':
		if vm:
			try:
				vm.Delete()
				output.speak(_("Voicemail deleted."), True)
			except:
				output.speak(_("Error, voicemail cannot be deleted."), True)
		else:
			return output.speak(_("No voicemail to delete."))

def playVoicemail(number, *args, **kwargs):
	if not globalVars.Skype.Voicemails:
		return output.speak(_("There are no voicemails."))
	if number>=globalVars.Skype.Voicemails.Count:
		return output.speak(_("No voicemail at this position, the first is at position %s.")%(globalVars.Skype.Voicemails.Count))
	vm=globalVars.Skype.Voicemails[number]
	try:
		vm.Open()
	except:
		output.speak(_("Error, cannot open that voicemail."))

def deleteVoicemail(number, *args, **kwargs):
	if not globalVars.Skype.Voicemails:
		return output.speak(_("There are no voicemails."))
	if number>=globalVars.Skype.Voicemails.Count:
		return output.speak(_("No voicemail at this position, the first is at position %s.")%(globalVars.Skype.Voicemails.Count))
	vm=globalVars.Skype.Voicemails[number]
	try:
		vm.Delete()
		output.speak(_("Voicemail deleted."), True)
	except:
		output.speak(_("Error, voicemail cannot be deleted."), True)

def aboutVoicemail(number, *args, **kwargs):
	if not globalVars.Skype.Voicemails:
		return output.speak(_("There are no voicemails."))
	if number>=globalVars.Skype.Voicemails.Count:
		return output.speak(_("No voicemail at this position, the first is at position %s.")%(globalVars.Skype.Voicemails.Count))
	vm=globalVars.Skype.Voicemails[number]
	if vm.Type==Skype4Py.vmtIncoming:
		vmMessage=_("Voicemail from %s. ")%vm.PartnerDisplayName
	elif vm.Type==Skype4Py.vmtOutgoing:
		vmMessage=_("Voicemail to %s. ")%vm.PartnerDisplayName
	elif vm.Type==Skype4Py.vmtDefaultGreeting:
		vmMessage=_("Default greeting voicemail. ")
	elif vm.Type==Skype4Py.vmtCustomGreeting:
		vmMessage=_("Custom greeting voicemail. ")
	elif vm.Type==Skype4Py.vmtUnknown:
		vmMessage=_("Unknown voicemail type. ")
	if vm.Status==Skype4Py.vmsUnplayed:
		output.speak(vmMessage+_("Not played."))
	else:
		output.speak(vmMessage)
