#    interface/preferences/categories/general.py
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
import globalVars
import i18n
import sys
import versionInfo
import wx

class generalCategory(BaseCategory):

	def __init__(self, *args, **kwargs):
		super(generalCategory, self).__init__(*args, **kwargs)
		wx.StaticText(parent=self, label=_("&Language:"))
		self._first=self.languageChoice=wx.ComboBox(parent=self, style=wx.CB_READONLY|wx.CB_SORT, choices=i18n.getAvailableLangDisplayNames())
		self.languageChoice.SetSizerProps(expand=True)
		try:
			self.oldLanguage=config.conf["general"]["language"]
			self.languageChoice.SetValue(i18n.getLangDisplayName(i18n.getAvailableLanguages()[self.oldLanguage]))
		except:
			pass
		self.startAppWithWindowsCheckBox=wx.CheckBox(parent=self, label=_("Start %s with &Windows")%versionInfo.name)
		if not globalVars.installed:
			self.startAppWithWindowsCheckBox.Show(False)
		self.autoStartSkypeCheckBox=wx.CheckBox(parent=self, label=_("Automatically &start Skype with %s")%versionInfo.name)
		self.autoStopSkypeCheckBox=wx.CheckBox(parent=self, label=_("Automatically &close Skype when %s exits")%versionInfo.name)
		self.confirmExitCheckBox=wx.CheckBox(parent=self, label=_("C&onfirm when exiting %s")%versionInfo.name)
		self.SysTrayIconCheckBox=wx.CheckBox(parent=self, label=_("Show %s icon on the &taskbar")%versionInfo.name)
		self.setValues()
		self.finishSetup()

	def setValues(self):
		self.startAppWithWindowsCheckBox.SetValue(config.conf["general"]["startAppWithWindows"])
		self.autoStartSkypeCheckBox.SetValue(config.conf["general"]["autoStartSkype"])
		self.autoStopSkypeCheckBox.SetValue(config.conf["general"]["autoStopSkype"])
		self.confirmExitCheckBox.SetValue(config.conf["general"]["confirmExit"])
		self.SysTrayIconCheckBox.SetValue(config.conf["general"]["showSysTrayIcon"])

	def GetValues(self):
		config.conf["general"]["startAppWithWindows"]=self.startAppWithWindowsCheckBox.GetValue()
		config.conf["general"]["autoStartSkype"]=self.autoStartSkypeCheckBox.GetValue()
		config.conf["general"]["autoStopSkype"]=self.autoStopSkypeCheckBox.GetValue()
		config.conf["general"]["confirmExit"]=self.confirmExitCheckBox.GetValue()
		config.conf["general"]["showSysTrayIcon"]=self.SysTrayIconCheckBox.GetValue()
