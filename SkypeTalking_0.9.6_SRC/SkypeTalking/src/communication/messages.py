#    communication/messages.py
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
logging=logger.getChild('communication.messages')
from platform_utils import clipboard
import events
import extras
import globalVars
import config
import output
import re
import Skype4Py
import time
import webbrowser

def OnMessage(message, status):
	if status==Skype4Py.cmsSending:
		output.speak(_("Sending..."))
	elif status==Skype4Py.cmsReceived:
		if config.conf['alerts']['chatMessageReceived'] and not globalVars.ignoreSkypeEvents:
			speakChatMessage(message)
		events.registerNewEvent(events.EVT_MESSAGES, _("Instant message from %s: %s")%(message.FromDisplayName, message.Body), announce=False)
	elif status==Skype4Py.cmsSent and message.Type != Skype4Py.cmeEmoted:
		if config.conf['alerts']['chatMessageSent'] and not globalVars.ignoreSkypeEvents:
			speakChatMessage(message, interrupt=True)
		events.registerNewEvent(events.EVT_MESSAGES, _("Instant message from %s: %s")%(message.FromDisplayName, message.Body), announce=False)
	elif status==Skype4Py.cmsSent and message.Type == Skype4Py.cmeEmoted:
		events.registerNewEvent(events.EVT_MESSAGES, _("SMS message by %s: %s")%(message.FromDisplayName, message.Body), announce=True)
	if status  in (Skype4Py.cmsReceived,  Skype4Py.cmsSent) and message.Type != Skype4Py.cmeEmoted: 
		globalVars.chatMonitor = message.Chat
	globalVars.lastChatMessage=message

def speakChatMessage(m, repeated=False, interrupt=False):
	if not m:
		return
	when=extras.getPrettyDate(m.Datetime)
	time=m.Datetime.strftime('%H:%M:%S')
	if config.conf['verbosity']['speakMessageTime'] and config.conf['verbosity']['speakContactNameWithMessage']:
		if repeated:
			if not when:
				output.speak(_("at %s, %s said: %s")%(time, m.FromDisplayName, m.Body), interrupt)
			else:
				output.speak(_("%s at %s, %s said: %s")%(when, time, m.FromDisplayName, m.Body), interrupt)
		else:
			if not when:
				output.speak(_("at %s, %s says: %s")%(time, m.FromDisplayName, m.Body), interrupt)
			else:
				output.speak(_("%s at %s, %s says: %s")%(when, time, m.FromDisplayName, m.Body), interrupt)
	elif config.conf['verbosity']['speakMessageTime'] and not config.conf['verbosity']['speakContactNameWithMessage']:
		if not when:
			output.speak(_("at %s: %s")%(time, m.Body), interrupt)
		else:
			output.speak(_("%s at %s: %s")%(when, time, m.Body), interrupt)
	elif not config.conf['verbosity']['speakMessageTime'] and config.conf['verbosity']['speakContactNameWithMessage']:
		if repeated:
			output.speak(_("%s said: %s")%(m.FromDisplayName, m.Body), interrupt)
		else:
			output.speak(_("%s says: %s")%(m.FromDisplayName, m.Body), interrupt)
	elif not config.conf['verbosity']['speakMessageTime'] and not config.conf['verbosity']['speakContactNameWithMessage']:
		output.speak(m.Body, interrupt)
	if m.Status==Skype4Py.cmsSending:
		output.speak(_("Message not delivered yet."))

def messageToClipboard(m):
	if not m:
		return
	try:
		clipboard.Copy(m.Body)
		output.speak(_("Message copied to clipboard."))
	except:
		output.speak(_("copy failed"))

def searchForURL(m):
	if not m:
		return
	urlPattern=re.compile(r"(^|[ \t\r\n])((ftp|http|https|gopher|mailto|news|nntp|telnet|wais|file|prospero|aim|webcal|www\.):?(([A-Za-z0-9$_.+!*(),;/?:@&~=-])|%[A-Fa-f0-9]{2}){2,}(#([a-zA-Z0-9][a-zA-Z0-9$_.+!*(),;/?:@&~=%-]*))?([A-Za-z0-9$_+!*();/?:~-]))")
	result=urlPattern.search(m.Body)
	if result:
		try:
			output.speak(_("opening URL"))
			webbrowser.open_new_tab(unicode(result.group().strip()))
		except:
				output.speak(_("Failed to open this URL."))
	else:
		output.speak(_("url not found"))
