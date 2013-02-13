#    interface/preferences/categories/contactsManager.py
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

class contactsManagerCategory(BaseCategory):
	def __init__(self, *args, **kwargs):
		super(contactsManagerCategory, self).__init__(*args, **kwargs)
		self._first=self.showOfflineContactsCheckBox=wx.CheckBox(parent=self, label=_("Show &offline contacts"))
		self.setValues()
		self.finishSetup()

	def setValues(self):
		self.showOfflineContactsCheckBox.SetValue(config.conf["contactsmanager"]["showOfflineContacts"])

	def GetValues(self):
		config.conf["contactsmanager"]["showOfflineContacts"]=self.showOfflineContactsCheckBox.GetValue()
