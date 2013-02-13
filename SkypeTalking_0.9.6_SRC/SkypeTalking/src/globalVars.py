#    globalVars.py
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
This module stores global variables that are used by all other parts of the program.
"""

from platform_utils.autostart.windows import is_installed

_firstguirun=True #determine if a GUI window was open for the first time since SkypeTalking was started
installed=is_installed('SkypeTalking_is1')
keyDescriber=False
ignoreSkypeEvents=False
evtType=0
reviewMode=0
lastEvent=None
lastChatMessage=None
call=None
callStatusEvent=None
userStatusEvent=None
fileTransferEvent=None
transferringFile=None
userEvent=None
lastSmsSent=None
chatMonitor = None
voicemail=None
voicemailEvent=None