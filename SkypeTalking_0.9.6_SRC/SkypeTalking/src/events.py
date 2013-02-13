#    events.py
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

"""
This module contains functions and variables for working with Skype events. It also keeps the event history.
"""

from log import logger
logging=logger.getChild('core.events')
from datetime import datetime
from extras import getPrettyDate
import config
import globalVars
import output
import tones

#event type constants
EVT_STATUSCHANGES=0
EVT_CALLS=1
EVT_MESSAGES=2
EVT_FILES=3
EVT_USERS=4
EVT_VOICEMAIL=5

###Globals
events=[]
lstStatusChanges=[]
lstCalls=[]
lstMessages=[]
lstFileTransfers=[]
lstUserActions=[]
lstVoicemail=[]
currentEvent=None
###EndGlobals

def registerNewEvent(EVTType, EVTText, announce=True, interrupt=False, monitoring=False):
	"""
Register a new event to be announced/recorded by SkypeTalking.
Parameters:
@evtText: A text that should be spoken and remembered when the event happens.
@announce: Speaks the event at the moment when it happens if set to True.
@interrupt: Will interrupt previous SkypeTalking message if set to True, which is useful for statuses that may change very quickly, such as file transfer statuses and call statuses.
@monitoring: If set to False, the event will not be saved to history buffer, and will not be spoken by RepeatLastEvent command. Leave it set to False unless you are monitoring events such as active file Transfers, active calls, or users pending authorization.
"""
	global lstStatusChanges, lstCalls, lstMessages, lstFileTransfers, lstUserActions, lstVoicemail
	evtDatetime=datetime.now()
	try:
		if announce and not globalVars.ignoreSkypeEvents:
			if config.conf["verbosity"]["saySkypeAlertMessage"]==0:
				output.speak(_("Skype alert"), interrupt)
				output.speak(EVTText)
			elif config.conf["verbosity"]["saySkypeAlertMessage"]==1:
				output.speak(EVTText, interrupt)
				output.speak(_("Skype alert"))
			elif config.conf["verbosity"]["saySkypeAlertMessage"]==2:
				output.speak(EVTText, interrupt)
		if EVTType==EVT_STATUSCHANGES:
			globalVars.userStatusEvent=EVTText
			if not monitoring:
				lstStatusChanges.append((evtDatetime, globalVars.userStatusEvent))
		elif EVTType==EVT_MESSAGES:
			globalVars.lastChatMessage=EVTText
			if not monitoring:
				lstMessages.append((evtDatetime, globalVars.lastChatMessage))
		elif EVTType==EVT_CALLS:
			globalVars.callStatusEvent=EVTText
			if not monitoring:
				lstCalls.append((evtDatetime, globalVars.callStatusEvent))
		elif EVTType==EVT_FILES:
			globalVars.fileTransferEvent=EVTText
			if not monitoring:
				lstFileTransfers.append((evtDatetime, globalVars.fileTransferEvent))
		elif EVTType==EVT_USERS:
			globalVars.userEvent=EVTText
			if not monitoring:
				lstUserActions.append((evtDatetime, globalVars.userEvent))
		elif EVTType==EVT_VOICEMAIL:
			globalVars.voicemailEvent=EVTText
			if not monitoring:
				lstVoicemail.append((evtDatetime, globalVars.voicemailEvent))
		if not monitoring:
			globalVars.lastEvent=EVTText
	except:
		logging.exception("Events: Event registration failed.")

def allEvents(event):
	global events, currentEvent
	if globalVars.evtType==0:
		events=[x for x in lstStatusChanges]
	elif globalVars.evtType==1:
		events=[x for x in lstCalls]
	elif globalVars.evtType==2:
		events=[x for x in lstMessages]
	elif globalVars.evtType==3:
		events=[x for x in lstFileTransfers]
	elif globalVars.evtType==4:
		events=[x for x in lstUserActions]
	elif globalVars.evtType==5:
		events=[x for x in lstVoicemail]
	if event < 0 and len(events)>0:
		tones.makeDefaultBeep()
		event=len(events)-1
	elif event >= len(events):
		tones.makeDefaultBeep()
		event = 0
	try:
		if event == events.index(currentEvent):
			return currentEvent
	except:
		pass
	currentEvent = events[event]
	return currentEvent

def getIndex(event=None):
	global events
	if not event:
		event=currentEvent
	try:
		res=events.index(event)
	except:
		res=0
	return res

def navigate(dirBackwards=False):
	"""
Navigates the event history.
Parameters:
@dirBackwards: Moves in opposite direction if set to True.
"""
	try:
		if dirBackwards:
			allEvents(getIndex()-1)
		else:
			allEvents(getIndex()+1)
		when=getPrettyDate(currentEvent[0])
		time=currentEvent[0].strftime('%H:%M:%S')
		if when:
			output.speak(_("%s (%s at %s)")%(currentEvent[1], when, time), True)
		else:
			output.speak(_("%s (just now at %s)")%(currentEvent[1], time), True)
	except:
		output.speak(_("No new events yet for this event type."))
