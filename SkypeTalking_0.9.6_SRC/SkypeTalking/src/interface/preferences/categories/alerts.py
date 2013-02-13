#    interface/preferences/categories/alerts.py
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

class alertsCategory(BaseCategory):

	def __init__(self, *args, **kwargs):
		super(alertsCategory, self).__init__(*args, **kwargs)
		self._first=self.userChangedMoodTextCheckBox=wx.CheckBox(parent=self, label=_("User changed his/her Mood &Text"))
		self.chatMessageReceivedCheckBox=wx.CheckBox(parent=self, label=_("Chat message &received"))
		self.chatMessageSentCheckBox=wx.CheckBox(parent=self, label=_("Chat message &sent"))
		self.onlineStatusUnknownCheckBox=wx.CheckBox(parent=self, label=_("Online status &unknown"))
		self.onlineStatusOfflineCheckBox=wx.CheckBox(parent=self, label=_("Online status O&ffline"))
		self.onlineStatusOnlineCheckBox=wx.CheckBox(parent=self, label=_("Online status &Online"))
		self.onlineStatusAwayCheckBox=wx.CheckBox(parent=self, label=_("Online status &Away"))
		self.onlineStatusNotAvailableCheckBox=wx.CheckBox(parent=self, label=_("Online status &Not Available"))
		self.onlineStatusDoNotDisturbCheckBox=wx.CheckBox(parent=self, label=_("Online status &Do Not Disturb"))
		self.onlineStatusInvisibleCheckBox=wx.CheckBox(parent=self, label=_("Online status &Invisible"))
		self.onlineStatusSkypeOutCheckBox=wx.CheckBox(parent=self, label=_("Online status &SkypeOut"))
		self.onlineStatusSkypeMeCheckBox=wx.CheckBox(parent=self, label=_("Online status &Skype Me!"))
		self.setValues()
		self.finishSetup()

	def setValues(self):
		self.userChangedMoodTextCheckBox.SetValue(config.conf["alerts"]["userChangedMoodText"])
		self.chatMessageReceivedCheckBox.SetValue(config.conf["alerts"]["chatMessageReceived"])
		self.chatMessageSentCheckBox.SetValue(config.conf["alerts"]["chatMessageSent"])
		self.onlineStatusUnknownCheckBox.SetValue(config.conf["alerts"]["onlineStatusUnknown"])
		self.onlineStatusOfflineCheckBox.SetValue(config.conf["alerts"]["onlineStatusOffline"])
		self.onlineStatusOnlineCheckBox.SetValue(config.conf["alerts"]["onlineStatusOnline"])
		self.onlineStatusAwayCheckBox.SetValue(config.conf["alerts"]["onlineStatusAway"])
		self.onlineStatusNotAvailableCheckBox.SetValue(config.conf["alerts"]["onlineStatusNotAvailable"])
		self.onlineStatusDoNotDisturbCheckBox.SetValue(config.conf["alerts"]["onlineStatusDoNotDisturb"])
		self.onlineStatusInvisibleCheckBox.SetValue(config.conf["alerts"]["onlineStatusInvisible"])
		self.onlineStatusSkypeOutCheckBox.SetValue(config.conf["alerts"]["onlineStatusSkypeOut"])
		self.onlineStatusSkypeMeCheckBox.SetValue(config.conf["alerts"]["onlineStatusSkypeMe"])

	def GetValues(self):
		config.conf["alerts"]["userChangedMoodText"]=self.userChangedMoodTextCheckBox.GetValue()
		config.conf["alerts"]["chatMessageReceived"]=self.chatMessageReceivedCheckBox.GetValue()
		config.conf["alerts"]["chatMessageSent"]=self.chatMessageSentCheckBox.GetValue()
		config.conf["alerts"]["onlineStatusUnknown"]=self.onlineStatusUnknownCheckBox.GetValue()
		config.conf["alerts"]["onlineStatusOffline"]=self.onlineStatusOfflineCheckBox.GetValue()
		config.conf["alerts"]["onlineStatusOnline"]=self.onlineStatusOnlineCheckBox.GetValue()
		config.conf["alerts"]["onlineStatusAway"]=self.onlineStatusAwayCheckBox.GetValue()
		config.conf["alerts"]["onlineStatusNotAvailable"]=self.onlineStatusNotAvailableCheckBox.GetValue()
		config.conf["alerts"]["onlineStatusDoNotDisturb"]=self.onlineStatusDoNotDisturbCheckBox.GetValue()
		config.conf["alerts"]["onlineStatusInvisible"]=self.onlineStatusInvisibleCheckBox.GetValue()
		config.conf["alerts"]["onlineStatusSkypeOut"]=self.onlineStatusSkypeOutCheckBox.GetValue()
		config.conf["alerts"]["onlineStatusSkypeMe"]=self.onlineStatusSkypeMeCheckBox.GetValue()
