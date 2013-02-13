#    interface/commands.py
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

import about
import communication
import config
import contactsManager
import events
import globalVars
import interface
import output
import preferences
import updater
import versionInfo
import wx

class interfaceCommands(object):
	def ShowPreferences(self, keypress):
		preferences.open()
	ShowPreferences.__doc__=_("Allows access to SkypeTalking Preferences Dialog where you can configure application behavior, or change your SkypeTalking language and speech output.")

	def OpenContactsManager(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			contactsManager.open('ofSkypeTalking')
		else:
			contactsManager.open('SkypeOriginal')
	OpenContactsManager.__doc__=_("Opens the Contacts Manager for viewing and managing your Skype contacts on the easy way. If pressed twice, the original Skype contact list will be displayed.")

	def DisplayAboutDialog(self, keypress):
		about.open()
	DisplayAboutDialog.__doc__=_("Displays some basic information about SkypeTalking application, such as current version, copyright details and program web site.")

	def QuitSkypeTalking(self, keypress):
		interface.exit()
	QuitSkypeTalking.__doc__=_("Quits SkypeTalking application.")

	def StopSpeech(self, keypress):
		output.Silence()
	StopSpeech.__doc__=_("Silences speech if your speech output is set to SAPI5.")

	def IgnoreSkypeEventsToggle(self, keypress):
		if not globalVars.ignoreSkypeEvents:
			globalVars.ignoreSkypeEvents=True
			state=_("on")
		else:
			globalVars.ignoreSkypeEvents=False
			state=_("off")
		output.speak(_("Ignore Skype events %s.")%state,1)
	IgnoreSkypeEventsToggle.__doc__=_("Toggles ignoring of all Skype events. If turned on, SkypeTalking will ignore all Skype events and will not speak nor record them.")

	def KeyDescriberToggle(self, keypress):
		if not globalVars.keyDescriber:
			globalVars.keyDescriber=True
			state=_("on")
		else:
			globalVars.keyDescriber=False
			state=_("off")
		output.speak(_("Key describer %s.")%state,1)
	KeyDescriberToggle.__doc__=_("Toggles on or off key describer. When turned on, it will describe a command associated with SkypeTalking keystroke being pressed.")

	def ChangeCurrentStatus(self, keypress):
		communication.status.changeStatus()
	ChangeCurrentStatus.__doc__=_("Change the Skype online status for the current user on the fly.")

	def CheckForUpdates(self, keypress):
		updater.checkForUpdates()
	CheckForUpdates.__doc__=_("Checks for new versions or updates of SkypeTalking application.")

	def ReportOrChangeMoodText(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.reportMoodText()
		else:
			communication.misc.changeMoodText(self)
	ReportOrChangeMoodText.__doc__=_("Reports the current user Mood Text. If pressed twice, calls a function to change your Mood Text.")

	def CurrentUserStatusOrCreditBalance(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.status.reportUserStatus()
		else:
			communication.misc.reportCreditBalance()
	CurrentUserStatusOrCreditBalance.__doc__=_("Reports the current user online status. If pressed twice, calls a function to report the Skype credit balance for the current user.")

	def SkypeVersionInfo(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.SkypeVersionInfo()
		else:
			communication.misc.APIWrapperVersionInfo()
	SkypeVersionInfo.__doc__=_("Reports the currently running version of Skype. If pressed twice, calls a function to report an API Wrapper version, which is mainly useful for developers.")

	def RepeatLastEvent(self, keypress):
		communication.misc.repeatLastEvent()
	RepeatLastEvent.__doc__=_("Repeats the last Skype event that happened during the SkypeTalking session.")

	def ReportFileTransferStatus(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.getFileTransferStatus()
		else:
			communication.misc.getActiveFileTransfers()
	ReportFileTransferStatus.__doc__=_("Reports the status of the last incoming or outgoing file transfer. If pressed twice, allows you to choose one of the active file transfers to monitor.")

	def ReportCallDuration(self, keypress):
		communication.misc.reportCallDuration()
	ReportCallDuration.__doc__=_("Reports duration of an active call in hours/minutes/seconds.")

	def ReportCallStatus(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.getCallStatus()
		else:
			communication.misc.makeCallDialog()
	ReportCallStatus.__doc__=_("Reports the status of an active call. If pressed twice, will open a dialog box allowing you to call someone by entering the Skype name of a user, or multiple users separated by commas to create a conference.")

	def SMSSendWizard(self, keypress):
		communication.sms.smsSend()
	SMSSendWizard.__doc__=_("Launches a wizard for sending SMS messages on the easy way via SkypeTalking.")

	def NextEvent(self, keypress):
		events.navigate()
	NextEvent.__doc__=_("Go to next event in the events history buffer.")

	def PreviousEvent(self, keypress):
		events.navigate(dirBackwards=True)
	PreviousEvent.__doc__=_("Go to previous event in the events history buffer.")

	def EventTypeSelection(self, keypress):
		if globalVars.evtType==0:
			globalVars.evtType=1
			output.speak(_("calls"))
		elif globalVars.evtType==1:
			globalVars.evtType=2
			output.speak(_("messages"))
		elif globalVars.evtType==2:
			globalVars.evtType=3
			output.speak(_("file transfers"))
		elif globalVars.evtType==3:
			globalVars.evtType=4
			output.speak(_("user actions"))
		elif globalVars.evtType==4:
			globalVars.evtType=5
			output.speak(_("voicemail"))
		elif globalVars.evtType==5:
			globalVars.evtType=0
			output.speak(_("status changes"))
	EventTypeSelection.__doc__=_("Selects the event type to view in the events history buffer between status changes, calls, messages, file transfers, or user actions.")

	def SelectChatMonitor1(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.selectChatMonitor('select', 0)
		else:
			communication.misc.selectChatMonitor('open', 0)
	SelectChatMonitor1.__doc__=_("Selects chat monitor. If pressed twice, opens a chat window of the chat currently being monitored.")

	def SelectChatMonitor2(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.selectChatMonitor('select', 1)
		else:
			communication.misc.selectChatMonitor('open', 1)
	SelectChatMonitor2.__doc__=_("Selects chat monitor. If pressed twice, opens a chat window of the chat currently being monitored.")

	def SelectChatMonitor3(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.selectChatMonitor('select', 2)
		else:
			communication.misc.selectChatMonitor('open', 2)
	SelectChatMonitor3.__doc__=_("Selects chat monitor. If pressed twice, opens a chat window of the chat currently being monitored.")

	def SelectChatMonitor4(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.selectChatMonitor('select', 3)
		else:
			communication.misc.selectChatMonitor('open', 3)
	SelectChatMonitor4.__doc__=_("Selects chat monitor. If pressed twice, opens a chat window of the chat currently being monitored.")

	def SelectChatMonitor5(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.selectChatMonitor('select', 4)
		else:
			communication.misc.selectChatMonitor('open', 4)
	SelectChatMonitor5.__doc__=_("Selects chat monitor. If pressed twice, opens a chat window of the chat currently being monitored.")

	def SelectChatMonitor6(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.selectChatMonitor('select', 5)
		else:
			communication.misc.selectChatMonitor('open', 5)
	SelectChatMonitor6.__doc__=_("Selects chat monitor. If pressed twice, opens a chat window of the chat currently being monitored.")

	def SelectChatMonitor7(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.selectChatMonitor('select', 6)
		else:
			communication.misc.selectChatMonitor('open', 6)
	SelectChatMonitor7.__doc__=_("Selects chat monitor. If pressed twice, opens a chat window of the chat currently being monitored.")

	def SelectChatMonitor8(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.selectChatMonitor('select', 7)
		else:
			communication.misc.selectChatMonitor('open', 7)
	SelectChatMonitor8.__doc__=_("Selects chat monitor. If pressed twice, opens a chat window of the chat currently being monitored.")

	def SelectChatMonitor9(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.selectChatMonitor('select', 8)
		else:
			communication.misc.selectChatMonitor('open', 8)
	SelectChatMonitor9.__doc__=_("Selects chat monitor. If pressed twice, opens a chat window of the chat currently being monitored.")

	def SelectChatMonitor10(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.selectChatMonitor('select', 9)
		else:
			communication.misc.selectChatMonitor('open', 9)
	SelectChatMonitor10.__doc__=_("Selects chat monitor. If pressed twice, opens a chat window of the chat currently being monitored.")

	def ReportCurrentChatMonitor(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.reportChatMonitor()
		else:
			communication.misc.openMonitoredChat()
	ReportCurrentChatMonitor.__doc__=_("Reports the current chat monitor. If pressed twice, opens the Skype chat window for the chat currently being monitored.")

	def ReviewItem1(self, keypress):
		n=0
		if globalVars.reviewMode==0:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.handleChatMessage('readMessage', n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.handleChatMessage('copyMessage', n)
			else:
				communication.misc.handleChatMessage('searchForAddresses', n)
		elif globalVars.reviewMode==1:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.aboutVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.playVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 2:
				communication.misc.deleteVoicemail(n)
	ReviewItem1.__doc__=_("Review one of the last 10 items depending on selected review mode. Press it twice or thrice to execute the 2nd or 3rd action for the item (if possible).")

	def ReviewItem2(self, keypress):
		n=1
		if globalVars.reviewMode==0:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.handleChatMessage('readMessage', n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.handleChatMessage('copyMessage', n)
			else:
				communication.misc.handleChatMessage('searchForAddresses', n)
		elif globalVars.reviewMode==1:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.aboutVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.playVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 2:
				communication.misc.deleteVoicemail(n)
	ReviewItem2.__doc__=_("Review one of the last 10 items depending on selected review mode. Press it twice or thrice to execute the 2nd or 3rd action for the item (if possible).")

	def ReviewItem3(self, keypress):
		n=2
		if globalVars.reviewMode==0:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.handleChatMessage('readMessage', n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.handleChatMessage('copyMessage', n)
			else:
				communication.misc.handleChatMessage('searchForAddresses', n)
		elif globalVars.reviewMode==1:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.aboutVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.playVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 2:
				communication.misc.deleteVoicemail(n)
	ReviewItem3.__doc__=_("Review one of the last 10 items depending on selected review mode. Press it twice or thrice to execute the 2nd or 3rd action for the item (if possible).")

	def ReviewItem4(self, keypress):
		n=3
		if globalVars.reviewMode==0:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.handleChatMessage('readMessage', n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.handleChatMessage('copyMessage', n)
			else:
				communication.misc.handleChatMessage('searchForAddresses', n)
		elif globalVars.reviewMode==1:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.aboutVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.playVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 2:
				communication.misc.deleteVoicemail(n)
	ReviewItem4.__doc__=_("Review one of the last 10 items depending on selected review mode. Press it twice or thrice to execute the 2nd or 3rd action for the item (if possible).")

	def ReviewItem5(self, keypress):
		n=4
		if globalVars.reviewMode==0:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.handleChatMessage('readMessage', n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.handleChatMessage('copyMessage', n)
			else:
				communication.misc.handleChatMessage('searchForAddresses', n)
		elif globalVars.reviewMode==1:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.aboutVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.playVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 2:
				communication.misc.deleteVoicemail(n)
	ReviewItem5.__doc__=_("Review one of the last 10 items depending on selected review mode. Press it twice or thrice to execute the 2nd or 3rd action for the item (if possible).")

	def ReviewItem6(self, keypress):
		n=5
		if globalVars.reviewMode==0:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.handleChatMessage('readMessage', n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.handleChatMessage('copyMessage', n)
			else:
				communication.misc.handleChatMessage('searchForAddresses', n)
		elif globalVars.reviewMode==1:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.aboutVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.playVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 2:
				communication.misc.deleteVoicemail(n)
	ReviewItem6.__doc__=_("Review one of the last 10 items depending on selected review mode. Press it twice or thrice to execute the 2nd or 3rd action for the item (if possible).")

	def ReviewItem7(self, keypress):
		n=6
		if globalVars.reviewMode==0:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.handleChatMessage('readMessage', n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.handleChatMessage('copyMessage', n)
			else:
				communication.misc.handleChatMessage('searchForAddresses', n)
		elif globalVars.reviewMode==1:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.aboutVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.playVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 2:
				communication.misc.deleteVoicemail(n)
	ReviewItem7.__doc__=_("Review one of the last 10 items depending on selected review mode. Press it twice or thrice to execute the 2nd or 3rd action for the item (if possible).")

	def ReviewItem8(self, keypress):
		n=7
		if globalVars.reviewMode==0:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.handleChatMessage('readMessage', n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.handleChatMessage('copyMessage', n)
			else:
				communication.misc.handleChatMessage('searchForAddresses', n)
		elif globalVars.reviewMode==1:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.aboutVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.playVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 2:
				communication.misc.deleteVoicemail(n)
	ReviewItem8.__doc__=_("Review one of the last 10 items depending on selected review mode. Press it twice or thrice to execute the 2nd or 3rd action for the item (if possible).")

	def ReviewItem9(self, keypress):
		n=8
		if globalVars.reviewMode==0:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.handleChatMessage('readMessage', n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.handleChatMessage('copyMessage', n)
			else:
				communication.misc.handleChatMessage('searchForAddresses', n)
		elif globalVars.reviewMode==1:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.aboutVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.playVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 2:
				communication.misc.deleteVoicemail(n)
	ReviewItem9.__doc__=_("Review one of the last 10 items depending on selected review mode. Press it twice or thrice to execute the 2nd or 3rd action for the item (if possible).")

	def ReviewItem10(self, keypress):
		n=9
		if globalVars.reviewMode==0:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.handleChatMessage('readMessage', n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.handleChatMessage('copyMessage', n)
			else:
				communication.misc.handleChatMessage('searchForAddresses', n)
		elif globalVars.reviewMode==1:
			if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
				communication.misc.aboutVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
				communication.misc.playVoicemail(n)
			elif globalVars.Hotkey.getLastCommandRepeatCount() == 2:
				communication.misc.deleteVoicemail(n)
	ReviewItem10.__doc__=_("Review one of the last 10 items depending on selected review mode. Press it twice or thrice to execute the 2nd or 3rd action for the item (if possible).")

	def MessageVoicemailModeToggle(self, keypress):
		if globalVars.reviewMode==0:
			globalVars.reviewMode=1
			output.speak(_("Voicemail mode"))
		elif globalVars.reviewMode==1:
			globalVars.reviewMode=0
			output.speak(_("Message mode"))
	MessageVoicemailModeToggle.__doc__=_("Toggles between Message mode or Voicemail mode.")

	def RepeatLastChatMessage(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.repeatLastChatMessage('repeatOnly')
		else:
			communication.misc.repeatLastChatMessage("activateChatMonitorAndWindow")
	RepeatLastChatMessage.__doc__=_("Repeats the last incoming or outgoing chat message. If pressed twice, opens the Skype chat window associated with that message and sets chat monitor to it.")

	def AnswerHoldOrResumeCall(self, keypress):
		communication.misc.handleCall('answerHoldResume')
	AnswerHoldOrResumeCall.__doc__=_("Answers the call, or toggles between hold and resume for calls in progress.")

	def AnswerCallAndJoinToConference(self, keypress):
		communication.misc.handleCall('join')
	AnswerCallAndJoinToConference.__doc__=_("Answers the call and joins it to a conference (if on a conference call).")

	def Hangup(self, keypress):
		communication.misc.handleCall('finish')
	Hangup.__doc__=_("Ends the call or stops recording voicemail.")

	def MuteOrUnmuteMicrophone(self, keypress):
		communication.misc.handleCall('silentMic')
	MuteOrUnmuteMicrophone.__doc__=_("Mutes or unmutes microphone depending on it's current state.")

	def ReportIOStatus(self, keypress):
		communication.misc.GetDeviceStatus()
	ReportIOStatus.__doc__=_("Reports currently used input/output devices.")

	def ReportVoicemailStatus(self, keypress):
		if globalVars.Hotkey.getLastCommandRepeatCount() == 0:
			communication.misc.handleVoicemail('getStatus')
		elif globalVars.Hotkey.getLastCommandRepeatCount() == 1:
			communication.misc.handleVoicemail('open')
		elif globalVars.Hotkey.getLastCommandRepeatCount() == 2:
			communication.misc.handleVoicemail('delete')
	ReportVoicemailStatus.__doc__=_("Reports the status of the last voicemail. If pressed twice, opens and plays the voicemail. If pressed thrice, deletes the voicemail.")
