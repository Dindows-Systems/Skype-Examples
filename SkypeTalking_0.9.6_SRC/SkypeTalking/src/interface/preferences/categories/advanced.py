#    interface/preferences/categories/advanced.py
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

from baseCategory import BaseCategory
import config
import wx

class advancedCategory(BaseCategory):

	def __init__(self, *args, **kwargs):
		super(advancedCategory, self).__init__(*args, **kwargs)
		wx.StaticText(parent=self, label=_("Number of &connection retries before giving up:"))
		self._first=self.connectionRetriesSpinBox=wx.SpinCtrl(self)
		self.connectionRetriesSpinBox.SetRange(0, 100)
		self.connectionRetriesSpinBox.SetSizerProps(expand=True)
		self.startSkypeMinimizedCheckBox=wx.CheckBox(parent=self, label=_("Start Skype &minimized"))
		self.noSplashScreenCheckBox=wx.CheckBox(parent=self, label=_("No &splash screen when starting Skype"))
		self.setValues()
		self.finishSetup()

	def setValues(self):
		self.connectionRetriesSpinBox.SetValue(config.conf["advanced"]["connectionRetries"])
		self.startSkypeMinimizedCheckBox.SetValue(config.conf["advanced"]["startSkypeMinimized"])
		self.noSplashScreenCheckBox.SetValue(config.conf["advanced"]["noSplashScreen"])

	def GetValues(self):
		config.conf["advanced"]["connectionRetries"]=self.connectionRetriesSpinBox.GetValue()
		config.conf["advanced"]["startSkypeMinimized"]=self.startSkypeMinimizedCheckBox.GetValue()
		config.conf["advanced"]["noSplashScreen"]=self.noSplashScreenCheckBox.GetValue()
