from cStringIO import StringIO
defaults=StringIO("""#SkypeTalking Configuration File

#General settings, for controling general SkypeTalking behavior:
[general]
language=string(default="Windows")
startAppWithWindows=boolean(default=False)
autoStartSkype=boolean(default=True)
autoStopSkype=boolean(default=False)
confirmExit=boolean(default=True)
showSysTrayIcon=boolean(default=True)

#Settings for controling SkypeTalking speech/braille output:
[output]
speechOutput=integer(default=0)
sapi5SpeechRate=integer(default=1)
sapi5Volume=integer(default=100)
enableBrailleOutput=boolean(default=True)

#Settings for configuring the announcement of various Skype alerts:
[alerts]
userChangedMoodText=boolean(default=False)
chatMessageReceived=boolean(default=True)
chatMessageSent=boolean(default=True)
onlineStatusUnknown=boolean(default=True)
onlineStatusOffline=boolean(default=True)
onlineStatusOnline=boolean(default=True)
onlineStatusAway=boolean(default=True)
onlineStatusNotAvailable=boolean(default=True)
onlineStatusDoNotDisturb=boolean(default=True)
onlineStatusInvisible=boolean(default=True)
onlineStatusSkypeOut=boolean(default=True)
onlineStatusSkypeMe=boolean(default=True)

#SkypeTalking verbosity settings, for controling how SkypeTalking reads something:
[verbosity]
speakMessageTime=boolean(default=True)
speakContactNameWithMessage=boolean(default=True)
saySkypeAlertMessage=integer(default=0)

#SkypeTalking Updater Settings:
[updates]
autoCheckForUpdates=boolean(default=True)
downloadType=integer(default=0)

#Settings for built-in Contacts Manager:
[contactsmanager]
showOfflineContacts=boolean(default=False)

#Advanced settings:
#Caution, change these only if you're sure what you're doing!
[advanced]
connectionRetries=integer(default=5)
startSkypeMinimized=boolean(default=True)
noSplashScreen=boolean(default=True)

#Keyboard Shortcuts for SkypeTalking:
[hotkeys]
KeyDescriberToggle=string(default="control+alt+shift+k")
ShowPreferences=string(default="control+alt+shift+p")
OpenContactsManager=string(default="control+alt+shift+f11")
SMSSendWizard=string(default="control+alt+shift+s")
DisplayAboutDialog=string(default="control+alt+shift+a")
CheckForUpdates=string(default="control+alt+shift+u")
QuitSkypeTalking=string(default="control+alt+shift+q")
StopSpeech=string(default="control+alt+shift+space")
SkypeVersionInfo=string(default="control+alt+shift+v")
ReportOrChangeMoodText=string(default="control+alt+shift+m")
SelectChatMonitor1=string(default="control+alt+shift+f1")
SelectChatMonitor2=string(default="control+alt+shift+f2")
SelectChatMonitor3=string(default="control+alt+shift+f3")
SelectChatMonitor4=string(default="control+alt+shift+f4")
SelectChatMonitor5=string(default="control+alt+shift+f5")
SelectChatMonitor6=string(default="control+alt+shift+f6")
SelectChatMonitor7=string(default="control+alt+shift+f7")
SelectChatMonitor8=string(default="control+alt+shift+f8")
SelectChatMonitor9=string(default="control+alt+shift+f9")
SelectChatMonitor10=string(default="control+alt+shift+f10")
ReportCurrentChatMonitor=string(default="control+alt+shift+c")
ReviewItem1=string(default="control+alt+shift+1")
ReviewItem2=string(default="control+alt+shift+2")
ReviewItem3=string(default="control+alt+shift+3")
ReviewItem4=string(default="control+alt+shift+4")
ReviewItem5=string(default="control+alt+shift+5")
ReviewItem6=string(default="control+alt+shift+6")
ReviewItem7=string(default="control+alt+shift+7")
ReviewItem8=string(default="control+alt+shift+8")
ReviewItem9=string(default="control+alt+shift+9")
ReviewItem10=string(default="control+alt+shift+0")
MessageVoicemailModeToggle=string(default="control+alt+shift+z")
RepeatLastChatMessage=string(default="control+alt+shift+r")
NextEvent=string(default="control+alt+shift+.")
PreviousEvent=string(default="control+alt+shift+,")
EventTypeSelection=string(default="control+alt+shift+-")
RepeatLastEvent=string(default="control+alt+shift+e")
CurrentUserStatusOrCreditBalance=string(default="control+alt+shift+o")
ChangeCurrentStatus=string(default="control+alt+shift+back")
ReportFileTransferStatus=string(default="control+alt+shift+f")
AnswerHoldOrResumeCall=string(default="control+alt+shift+home")
AnswerCallAndJoinToConference=string(default="control+alt+shift+pageup")
Hangup=string(default="control+alt+shift+end")
MuteOrUnmuteMicrophone=string(default="control+alt+shift+pagedown")
ReportCallDuration=string(default="control+alt+shift+d")
ReportCallStatus=string(default="control+alt+shift+l")
ReportVoicemailStatus=string(default="control+alt+shift+w")
IgnoreSkypeEventsToggle=string(default="control+alt+shift+i")
ReportIOStatus=string(default="control+alt+shift+x")

#End Of File""")