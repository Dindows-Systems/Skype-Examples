#    interface/preferences/categories/output.py
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

class outputCategory(BaseCategory):

	def __init__(self, *args, **kwargs):
		super(outputCategory, self).__init__(*args, **kwargs)
		wx.StaticText(parent=self, label=_("Speech Output:"))
		self._first=self.speechOutputChoice=wx.ComboBox(parent=self, choices=[_("Auto detect"), _("SAPI5")], style=wx.CB_READONLY)
		self.speechOutputChoice.SetSizerProps(expand=True)
		wx.StaticText(parent=self, label=_("SAPI5 Speech Rate:"))
		self.sapi5SpeechRateText=wx.SpinCtrl(self)
		self.sapi5SpeechRateText.SetRange(1, 10)
		self.sapi5SpeechRateText.SetSizerProps(expand=True)
		wx.StaticText(parent=self, label=_("SAPI5 Volume:"))
		self.sapi5VolumeText=wx.SpinCtrl(self)
		self.sapi5VolumeText.SetRange(1, 100)
		self.sapi5VolumeText.SetSizerProps(expand=True)
		self.enableBrailleOutputCheckBox=wx.CheckBox(parent=self, label=_("Enable &braille output"))
		self.setValues()
		self.finishSetup()

	def setValues(self):
		self.speechOutputChoice.SetSelection(config.conf["output"]["speechOutput"])
		self.sapi5SpeechRateText.SetValue(config.conf["output"]["sapi5SpeechRate"])
		self.sapi5VolumeText.SetValue(config.conf["output"]["sapi5Volume"])
		self.enableBrailleOutputCheckBox.SetValue(config.conf["output"]["enableBrailleOutput"])

	def GetValues(self):
		config.conf["output"]["speechOutput"]=self.speechOutputChoice.GetSelection()
		config.conf["output"]["sapi5SpeechRate"]=self.sapi5SpeechRateText.GetValue()
		config.conf["output"]["sapi5Volume"]=self.sapi5VolumeText.GetValue()
		config.conf["output"]["enableBrailleOutput"]=self.enableBrailleOutputCheckBox.GetValue()
