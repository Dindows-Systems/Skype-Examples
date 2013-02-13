#    interface/preferences/categories/updates.py
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
import versionInfo
import wx

class updatesCategory(BaseCategory):

	def __init__(self, *args, **kwargs):
		super(updatesCategory, self).__init__(*args, **kwargs)
		self._first=self.autoCheckForUpdatesCheckBox=wx.CheckBox(parent=self, label=_("&Automatically check for %s updates")%versionInfo.name)
		wx.StaticText(parent=self, label=_("&Download Type:"))
		self.downloadTypeChoice=wx.ComboBox(parent=self, choices=[_("Installer"), _("Portable Archive")], style=wx.CB_READONLY)
		self.downloadTypeChoice.SetSizerProps(expand=True)
		self.setValues()
		self.finishSetup()

	def setValues(self):
		self.autoCheckForUpdatesCheckBox.SetValue(config.conf["updates"]["autoCheckForUpdates"])
		self.downloadTypeChoice.SetSelection(config.conf["updates"]["downloadType"])

	def GetValues(self):
		config.conf["updates"]["autoCheckForUpdates"]=self.autoCheckForUpdatesCheckBox.GetValue()
		config.conf["updates"]["downloadType"]=self.downloadTypeChoice.GetSelection()
