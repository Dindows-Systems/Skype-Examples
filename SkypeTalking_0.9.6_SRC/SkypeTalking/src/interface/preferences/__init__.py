#    interface/preferences/__init__.py
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

from log import logger
logging=logger.getChild('interface.preferences')
from gui_components.sized import SizedDialog
from i18n_utils import core
from platform_utils.autostart import windows
import categories
import config
import globalVars
import i18n
import interface
import locations
import output
import versionInfo
import wx

def open():
	preferencesDLG=preferencesDialog(parent=globalVars.Frame, title=versionInfo.name+" - "+_("Preferences"))
	globalVars.Frame.DisplayDialog(preferencesDLG)

class preferencesDialog(SizedDialog):

	def __init__(self, *args, **kwargs):
		self.needsRestart=False
		super(preferencesDialog, self).__init__(*args, **kwargs)
		self.Categories=wx.Treebook(self.pane, -1, style=wx.BK_DEFAULT)
		self.GeneralPage=categories.generalCategory(self.Categories)
		self.Categories.AddPage(self.GeneralPage, _("General"))
		self.OutputPage=categories.outputCategory(self.Categories)
		self.Categories.AddPage(self.OutputPage, _("Output"))
		self.AlertsPage=categories.alertsCategory(self.Categories)
		self.Categories.AddPage(self.AlertsPage, _("Alerts"))
		self.VerbosityPage=categories.verbosityCategory(self.Categories)
		self.Categories.AddPage(self.VerbosityPage, _("Verbosity"))
		self.AdvancedPage=categories.advancedCategory(self.Categories)
		self.Categories.AddPage(self.AdvancedPage, _("Advanced"))
		self.UpdatesPage=categories.updatesCategory(self.Categories)
		self.Categories.AddPage(self.UpdatesPage, _("Updates"))
		self.ContactsManagerPage=categories.contactsManagerCategory(self.Categories)
		self.Categories.AddPage(self.ContactsManagerPage, _("Contacts Manager"))
		self.hotKeysPage=categories.hotKeysCategory(self.Categories)
		self.Categories.AddPage(self.hotKeysPage, _("Hot keys"))
		self.Categories.GetTreeCtrl().SetFocus()
		wx.FutureCall(-1, self.AdjustTreebookSize)
		self.finish_setup(set_focus=False)

	def create_buttons(self):
		ButtonSizer=self.CreateStdDialogButtonSizer(wx.OK|wx.CANCEL|wx.APPLY)
		self.SetEscapeId(wx.ID_CANCEL)
		self.SetButtonSizer(ButtonSizer)
		self.GetSizer().Hide(ButtonSizer)
		self.Bind(wx.EVT_BUTTON, lambda evt: self.saveSettings(), id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.CancelSettings, id=wx.ID_CANCEL)
		self.Bind(wx.EVT_BUTTON, lambda evt: self.saveSettings(doExit=False), id=wx.ID_APPLY)

	def AdjustTreebookSize(self):
		self.Categories.GetTreeCtrl().InvalidateBestSize()
		self.Categories.SendSizeEvent()

	def saveSettings(self, doExit=True):
		self.GeneralPage.GetValues()
		self.OutputPage.GetValues()
		self.AlertsPage.GetValues()
		self.VerbosityPage.GetValues()
		self.UpdatesPage.GetValues()
		self.ContactsManagerPage.GetValues()
		self.AdvancedPage.GetValues()
		self.changeLanguage()
		globalVars.Hotkey.unregisterHotkeys()
		config.conf.write()
		globalVars.Hotkey.registerHotkeys()
		output.initialize()
		windows.setAutoStart(versionInfo.name, config.conf["general"]["startAppWithWindows"])
		if doExit:
			output.speak(_("Settings saved."))
			globalVars.Frame.CloseDialog(self)
			if self.needsRestart:
				self.restart()
		else:
			output.speak(_("Settings applied."))

	def CancelSettings(self, evt):
		output.speak(_("Settings canceled."))
		globalVars.Frame.CloseDialog(self)

	def changeLanguage(self):
		newLanguage=i18n.langFromLangDisplayName(self.GeneralPage.languageChoice.GetValue())
		if newLanguage!=self.GeneralPage.oldLanguage:
			try:
				core.set_active_language(versionInfo.name, locations.catalogFilesLocation(), newLanguage)
				self.needsRestart=True
			except:
				logging.error("Language setting error.")
				wx.MessageDialog(self,_("Error in %s language file")%newLanguage,_("Language Error"),wx.OK|wx.ICON_WARNING).ShowModal()
				self.needsRestart=False
				return
		config.conf["general"]["language"]=newLanguage

	def restart(self):
		canRestart=False
		w=wx.MessageDialog(self, _("For the new language to fully take affect, I must now restart %s. Click OK to continue, or Cancel to restart later manually.")%versionInfo.name, versionInfo.name+" - "+_("Preferences"), wx.OK|wx.CANCEL|wx.ICON_WARNING)
		a=w.ShowModal()
		if a==wx.ID_OK:
			canRestart=True
		elif a==wx.ID_CANCEL:
			canRestart=False
			return
		if canRestart:
			wx.CallLater(2000, interface.shutdown, False, True, True)
