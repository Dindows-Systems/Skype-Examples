#    interface/__init__.py
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
logging=logger.getChild('core.interface')
from main import mainInterface
import config
import globalVars
import output
import sys
import versionInfo
import wx

def exit():
	exitConfirmed=False
	if not config.conf['general']['confirmExit']:
		exitConfirmed=True
	elif config.conf['general']['confirmExit']:
		confirm=wx.MessageDialog(None, _("Are you sure you want to exit %s? This will also unload Skype if you've configured such behavior.")%versionInfo.name, _("Confirm Exit"), wx.YES|wx.NO|wx.ICON_WARNING)
		globalVars.Frame.DisplayDialog(confirm)
		answer=confirm.ShowModal()
		if answer==wx.ID_YES:
			exitConfirmed=True
		else:
			exitConfirmed=False
			globalVars.Frame.CloseDialog(confirm)
			return
	if exitConfirmed:
		shutdown()

def shutdown(ShutdownSkype=True, silent=False, restart=False):
	exited=False
	import launcher
	if ShutdownSkype and config.conf['general']['autoStopSkype']==True:
		logging.debug("Shutting down Skype.")
		try:
			globalVars.Skype.Client.Shutdown()
		except:
			logging.exception("Error shutting down Skype client.")
	else:
		pass
	if not silent:
		output.speak(_("Goodbye!"), True)
	logging.debug("Closing all open windows.")
	try:
		for child in globalVars.Frame.GetChildren():
			wx.CallAfter(child.Destroy)
	except: logging.exception("Error, couldn't destroy open windows.")
	try: globalVars.Hotkey.unregisterHotkeys()
	except: logging.exception("Error unregistering hotkeys.")
	globalVars.Frame.Destroy()
	wx.GetApp().ExitMainLoop()
	exited=True
	if restart and exited:
		launcher.restartProcess()
