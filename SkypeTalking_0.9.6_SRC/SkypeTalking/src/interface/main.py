#    interface/main.py
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

import config
import globalVars
import hotkey
import systemTray
import wx

class mainInterface(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(mainInterface, self).__init__(size=(1,1), style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.MINIMIZE_BOX | wx.FRAME_NO_TASKBAR, *args, **kwargs)
		self.Center()
		self.Hide()
		if config.conf["general"]["showSysTrayIcon"]:
			self.sysTrayIcon=systemTray.TBIcon(self)
		if not config.conf.has_key('hotkeys'):
			config.conf['hotkeys']={}
		import commands
		globalVars.Hotkey=hotkey.HotkeySupport(self, commands.interfaceCommands(), config.conf['hotkeys'])

	def DisplayDialog(self, dlg):
		self.Raise()
		if globalVars._firstguirun:
			dlg.Show(True)
			dlg.Hide()
		dlg.Show(True)
		globalVars._firstguirun=False

	def CloseDialog(self, dlg):
		self.Hide()
		dlg.Destroy()

	def Destroy(self):
		try: self.sysTrayIcon.Destroy()
		except: pass
		super(mainInterface, self).Destroy()
