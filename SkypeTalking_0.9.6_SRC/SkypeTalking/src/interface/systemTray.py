#    interface/systemTray.py
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

from platform_utils import paths
import about
import communication
import interface
import locations
import os
import preferences
import updater
import versionInfo
import wx

class TBIcon(wx.TaskBarIcon):
	"""The SkypeTalking Notification Area icon object."""

	def __init__(self, parent):
		super(TBIcon, self).__init__()
		icon=wx.Icon(locations.appLocation(versionInfo.name+".ico"), wx.BITMAP_TYPE_ICO)
		self.SetIcon(icon, "%s"%versionInfo.name)
		self.Menu=wx.Menu()
		ToolsMenu=wx.Menu()
		import contactsManager
		ContactsManId=wx.NewId()
		ContactsManOption=wx.MenuItem(ToolsMenu, ContactsManId, _("&Contacts Manager..."), _("Open Contacts Manager"))
		ToolsMenu.AppendItem(ContactsManOption)
		wx.EVT_MENU(self.Menu, ContactsManId, lambda evt: contactsManager.open("ofSkypeTalking"))
		SMSSendId=wx.NewId()
		SMSSendOption=wx.MenuItem(ToolsMenu, SMSSendId, _("&Send SMS Wizard..."), _("Start SMS Send Wizard"))
		ToolsMenu.AppendItem(SMSSendOption)
		wx.EVT_MENU(self.Menu, SMSSendId, communication.sms.smsSend)
		PreferencesId=wx.NewId()
		PreferencesOption=wx.MenuItem(ToolsMenu, PreferencesId, _("&Preferences..."), _("Open Preferences Dialog"))
		ToolsMenu.AppendItem(PreferencesOption)
		wx.EVT_MENU(self.Menu, PreferencesId, lambda evt: preferences.open())
		self.Menu.AppendMenu(wx.ID_ANY, _("&Tools"), ToolsMenu)
		HelpMenu=wx.Menu()
		DocId=wx.NewId()
		DocOption=wx.MenuItem(HelpMenu, DocId, _("&User Guide"), _("Read User Guide"))
		HelpMenu.AppendItem(DocOption)
		wx.EVT_MENU(self.Menu, DocId, lambda evt: os.startfile(locations.getDocFilePath("readme.txt")))
		WNId=wx.NewId()
		WNOption=wx.MenuItem(HelpMenu, WNId, _("&What's New"), _("Read What's New"))
		HelpMenu.AppendItem(WNOption)
		wx.EVT_MENU(self.Menu, WNId, lambda evt: os.startfile(locations.getDocFilePath("whatsnew.txt")))
		CTId=wx.NewId()
		CTOption=wx.MenuItem(HelpMenu, CTId, _("&Contributors"), _("View Contributors List"))
		HelpMenu.AppendItem(CTOption)
		wx.EVT_MENU(self.Menu, CTId, lambda evt: os.startfile(locations.getDocFilePath("contributors.txt", False)))
		LicenseId=wx.NewId()
		LicenseOption=wx.MenuItem(HelpMenu, LicenseId, _("&License"), _("View the license"))
		HelpMenu.AppendItem(LicenseOption)
		wx.EVT_MENU(self.Menu, LicenseId, lambda evt: os.startfile(locations.getDocFilePath("license.txt", False)))
		WebId=wx.NewId()
		WebOption=wx.MenuItem(HelpMenu, WebId, _("%s on the &Web")%versionInfo.name, _("Launch project Web Site in default browser"))
		HelpMenu.AppendItem(WebOption)
		wx.EVT_MENU(self.Menu, WebId, lambda evt: wx.LaunchDefaultBrowser(unicode("http://skypetalking.googlecode.com/")))
		UpdateId=wx.NewId()
		UpdateOption=wx.MenuItem(HelpMenu, UpdateId, _("Check for &updates..."), _("Check for the latest application updates"))
		HelpMenu.AppendItem(UpdateOption)
		wx.EVT_MENU(self.Menu, UpdateId, lambda evt: updater.checkForUpdates())
		AboutId=wx.NewId()
		AboutOption=wx.MenuItem(HelpMenu, AboutId, _("&About %s...")%versionInfo.name, _("About %s")%versionInfo.name)
		HelpMenu.AppendItem(AboutOption)
		wx.EVT_MENU(self.Menu, AboutId, lambda evt: about.open())
		self.Menu.AppendMenu(wx.ID_ANY, _("&Help"), HelpMenu)
		ExitId=wx.NewId()
		ExitOption=wx.MenuItem(self.Menu, ExitId, _("E&xit"), _("Exit %s")%versionInfo.name)
		self.Menu.AppendItem(ExitOption)
		wx.EVT_MENU(self.Menu, ExitId, lambda evt: interface.exit())
		self.Bind(wx.EVT_TASKBAR_RIGHT_DOWN, self.onActivate)

	def Destroy(self):
		self.Menu.Destroy()
		super(TBIcon, self).Destroy()

	def onActivate(self, evt):
		self.PopupMenu(self.Menu)
