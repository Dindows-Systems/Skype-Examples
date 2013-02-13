#    interface/preferences/categories/verbosity.py
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

class verbosityCategory(BaseCategory):

	def __init__(self, *args, **kwargs):
		super(verbosityCategory, self).__init__(*args, **kwargs)
		self._first=self.speakMessageTimeCheckBox=wx.CheckBox(parent=self, label=_("Speak message &time"))
		self.speakContactNameWithMessageCheckBox=wx.CheckBox(parent=self, label=_("Speak contact &name with message"))
		saySkypeAlertMessageChoices=(_("Before the alert"), _("After the alert"), _("Never"))
		self.saySkypeAlertMessageRadioBox=wx.RadioBox(parent=self, label=_('Say "Skype Alert" message'), choices=saySkypeAlertMessageChoices, style=wx.RA_SPECIFY_COLS)
		self.setValues()
		self.finishSetup()

	def setValues(self):
		self.speakMessageTimeCheckBox.SetValue(config.conf["verbosity"]["speakMessageTime"])
		self.speakContactNameWithMessageCheckBox.SetValue(config.conf["verbosity"]["speakContactNameWithMessage"])
		self.saySkypeAlertMessageRadioBox.SetSelection(config.conf["verbosity"]["saySkypeAlertMessage"])

	def GetValues(self):
		config.conf["verbosity"]["speakMessageTime"]=self.speakMessageTimeCheckBox.GetValue()
		config.conf["verbosity"]["speakContactNameWithMessage"]=self.speakContactNameWithMessageCheckBox.GetValue()
		config.conf["verbosity"]["saySkypeAlertMessage"]=self.saySkypeAlertMessageRadioBox.GetSelection()
