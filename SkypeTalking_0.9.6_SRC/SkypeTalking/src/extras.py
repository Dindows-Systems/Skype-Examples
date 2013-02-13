#    extras.py
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
Extra Utilities Module
"""

from log import logger
logging=logger.getChild('core.extras')
from datetime import datetime

def getPrintableUserName(DisplayName, FullName, Handle):
	"""
Returns the Skype user name printed on the same way like it's displayed in Skype Client application.
If the user has a display name, then display name will be printed.
If the user has no display name, then a full name will be printed.
If the user has no either display or full name, then a handle (Skype name) will be printed.
"""
	if len(DisplayName)==0:
		result=FullName
	else:
		result=DisplayName
	if len(result)==0:
		result=Handle
	if len(result)!=0:
		return result
	else:
		logging.exception("Unable to get printable user name.")
		return

def getPrettyDate(time=False):
	"""
Get a datetime object or a int() Epoch timestamp and return a pretty string like 'an hour ago', 'Yesterday', '3 months ago', 'just now', etc.
"""
	now=datetime.now()
	if type(time) is int:
		time=datetime.fromtimestamp(time)
	elif not time:
		time=now
	if time>now:
		diff=time-now
	else:
		diff=now-time
	secondDiff=diff.seconds
	dayDiff=diff.days
	if dayDiff<0:
		return ''
	if dayDiff==0:
		if secondDiff<10:
			return
		if secondDiff<60:
			return _("%d seconds ago")%secondDiff
		if secondDiff<120:
			return _("a minute ago")
		if secondDiff<3600:
			return _("%d minutes ago")%(secondDiff/60)
		if secondDiff < 7200:
			return _("an hour ago")
		if secondDiff<86400:
			return _("%d hours ago")%(secondDiff/3600)
	if dayDiff==1:
			return _("yesterday")
	if dayDiff<7:
		return _("%d days ago")%dayDiff
	if dayDiff<31:
		return _("%d weeks ago")%(dayDiff/7)
	if dayDiff<365:
		return _("%d months ago")%(dayDiff/30)
	return _("%d years ago")%(dayDiff/365)
