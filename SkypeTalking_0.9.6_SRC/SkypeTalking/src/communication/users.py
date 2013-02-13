#    communication/users.py
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
logging=logger.getChild('communication.users')
import config
import extras
import events
import globalVars
import output
import Skype4Py

def OnAuthRequest(user):
	if not user.IsAuthorized:
		events.registerNewEvent(events.EVT_USERS, _("User %s %s requests authorization. Intro text: %s")%(user.FullName, user.Handle, user.ReceivedAuthRequest), True)
	elif user.IsAuthorized:
		events.registerNewEvent(events.EVT_USERS, _("You are now friend with %s %s.")%(user.FullName, user.Handle), True)
	elif user.IsBlocked:
		events.registerNewEvent(events.EVT_USERS, _("User %s %s is blocked.")%(user.FullName, user.Handle), True)

def OnUserMood(user, MoodText):
	userName=extras.getPrintableUserName(user.DisplayName, user.FullName, user.Handle)
	if len(user.MoodText)==0:
		events.registerNewEvent(events.EVT_USERS, _("%s removed his/her Mood Text")%userName, config.conf["alerts"]["userChangedMoodText"])
	else:
		events.registerNewEvent(events.EVT_USERS, _("%s changed his/her Mood Text to %s")%(userName, user.MoodText), config.conf["alerts"]["userChangedMoodText"])
