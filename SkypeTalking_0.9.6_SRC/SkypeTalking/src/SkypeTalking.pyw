#    SkypeTalking.pyw
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

from platform_utils import blackhole
from log import logger as logging
import argparse
import communication
import config
import gettext
import globalVars
import interface
import i18n
import locations
import locale
import log
import output
import os
import sys
import versionInfo
import thread
import wx

"""
This is the SkypeTalking launcher. It initializes all required core components in order for the application to start successfully and then starts the application.
"""

#Command Line Arguments
parser=argparse.ArgumentParser()
parser.add_argument('-l', '--language', action='store', type=str, dest='language', help='specify a language to use with SkypeTalking')
args = parser.parse_args()

class SkypeTalkingApp(wx.App):

	def OnInit(self):
		self.name = versionInfo.name+" - %s"%wx.GetUserId()
		try:
			config.initialize()
		except:
			wx.MessageBox("Could not write config file. The application may not be started. Please contact development team for help.", "Error", wx.ICON_ERROR|wx.OK)
			return False
		if args.language:
			try:
				config.conf["general"]["language"]=args.language
				config.conf.write()
			except:
				logging.exception("Error setting language %s."%options['language'])
		try:
			i18n.initialize()
		except:
			logging.exception("Couldn't initialize i18n support.")
			wx.MessageBox("Could not set application language. The application may not be started. Please contact development team for help.", "Error", wx.ICON_ERROR|wx.OK)
			return False
		self.instance=wx.SingleInstanceChecker(self.name)
		if self.instance.IsAnotherRunning():
			wx.MessageBox(_("Application already running."), versionInfo.name, wx.ICON_WARNING|wx.OK)
			return False
		try:
			output.initialize()
			output.speak(_("Connecting to Skype..."))
		except:
			wx.MessageBox(_("Failed to initialize output subsystem. The application may not be started. Please contact development team for help."), _("Error"), wx.ICON_ERROR|wx.OK)
			return False
		self.SetAssertMode(wx.PYAPP_ASSERT_SUPPRESS)
		self.Bind(wx.EVT_QUERY_END_SESSION, lambda evt: None)
		self.Bind(wx.EVT_END_SESSION, self.onEndSession)
		return True

	def onEndSession(self, evt):
		logging.warn("Windows session ending, closing the application.")
		return interface.shutdown(ShutdownSkype=False, silent=True)

def main():
	wxLog=locations.dataFilesLocation('wx.log')
	try: os.remove(wxLog)
	except os.error: pass
	#Extra log messages
	logging.info("Windows version info: %r"%sys.getwindowsversion())
	logging.info("Python version info: %r"%sys.version_info)
	logging.info("Using %s version %s."%(versionInfo.name, versionInfo.version[0]))
	globalVars.App=SkypeTalkingApp(redirect=True, useBestVisual=True, filename=wxLog)
	wx.Log_SetActiveTarget(wx.LogStderr())
	wx.Log_SetTraceMask(wx.TraceMessages)
	#wxPython localization setup
	wxLocale=wx.Locale()
	lang=config.conf['general']['language']
	if '_' in lang:
		wxLang=lang.split('_')[0]
	else:
		wxLang=lang
	wxLocale.AddCatalogLookupPathPrefix(locations.catalogFilesLocation())
	try:
		wxLocale.Init(lang, wxLang)
	except:
		pass
	logging.info("Initializing GUI.")
	globalVars.Frame=interface.mainInterface(None, wx.ID_ANY, "SkypeTalking")
	wx.GetApp().SetTopWindow(globalVars.Frame)
	logging.info("Initializing API wrapper.")
	thread.start_new_thread(communication.main.initialize,())
	globalVars.App.MainLoop()

if __name__=="__main__":
	try:
		main()
	except:
		logging.exception("Application startup failure.")