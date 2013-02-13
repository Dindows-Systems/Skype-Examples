#    interface/about.py
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

from gui_components.sized import SizedDialog
import config
import globalVars
import locations
import os
import updater
import versionInfo
import wx
import wx.lib.sized_controls as sc

def open():
	aboutDLG=aboutDialog(parent=globalVars.Frame, title=_("About %s")%versionInfo.name)
	globalVars.Frame.DisplayDialog(aboutDLG)

class aboutDialog(SizedDialog):

	def __init__(self, *args, **kwargs):
		super(aboutDialog, self).__init__(*args, **kwargs)
		InfoPanel=sc.SizedPanel(self.pane, -1)
		wx.StaticText(InfoPanel, label=self.aboutText())
		self.SetEscapeId(wx.ID_CLOSE)
		self.finish_setup(set_focus=False)

	def create_buttons(self):
		ButtonPanel = sc.SizedPanel(self.pane, -1)
		ButtonPanel.SetSizerType("horizontal")
		self.CloseBTN=wx.Button(ButtonPanel, id=wx.ID_CLOSE)
		self.CloseBTN.SetFocus()
		self.CloseBTN.SetDefault()
		self.Bind(wx.EVT_BUTTON, lambda evt: globalVars.Frame.CloseDialog(self), self.CloseBTN)
		self.WebSiteBTN=wx.Button(ButtonPanel, label=_("Project &Web site"))
		self.Bind(wx.EVT_BUTTON, lambda evt: wx.LaunchDefaultBrowser(unicode("http://skypetalking.googlecode.com/")), self.WebSiteBTN)
		self.LicenseBTN=wx.Button(ButtonPanel, label=_("&License online"))
		self.Bind(wx.EVT_BUTTON, lambda evt: wx.LaunchDefaultBrowser(unicode("http://www.gnu.org/licenses/old-licenses/gpl-2.0.html")), self.LicenseBTN)
		self.ContribBTN=wx.Button(ButtonPanel, label=_("C&ontributors"))
		self.Bind(wx.EVT_BUTTON, lambda evt: os.startfile(locations.getDocFilePath("contributors.txt", False)), self.ContribBTN)
		self.DocBTN=wx.Button(ButtonPanel, label=_("User &Guide"))
		self.Bind(wx.EVT_BUTTON, lambda evt: os.startfile(locations.getDocFilePath("readme.txt")), self.DocBTN)
		self.WhatsnewBTN=wx.Button(ButtonPanel, label=_("&What's New"))
		self.Bind(wx.EVT_BUTTON, lambda evt: os.startfile(locations.getDocFilePath("whatsnew.txt")), self.WhatsnewBTN)
		self.UpdatesBTN=wx.Button(ButtonPanel, label=_("Check for &updates..."))
		self.Bind(wx.EVT_BUTTON, lambda evt: updater.checkForUpdates(), self.UpdatesBTN)

	def aboutText(self):
		text=_("""
%s %s
Copyright %s Hrvoje Katic / SkypeTalking Contributors
Project URL: %s
This software is distributed under the terms of the GNU General Public License version 2.
For more information, please click View License Online Button or view the file license.txt included with this software.
""")%(versionInfo.name, versionInfo.version[0], versionInfo.copyright, versionInfo.url)
		return text
