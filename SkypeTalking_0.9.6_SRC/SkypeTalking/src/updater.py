#    updater.py
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
logging=logger.getChild('core.updates')
from transfer_dialogs import DownloadDialog
import config
import globalVars
import interface
import launcher
import locations
import os
import output
import urllib2
import versionInfo
import wx

"""
This is the SkypeTalking updater. It will download the latest version of SkypeTalking from a web site automatically or by request.
"""

###Globals
latestVersion=None
currentVersion=versionInfo.version[0]
fileName=""
automatic=False
downloadDLG=None
###EndGlobals

def getOnlineVersion(type):
	"""Queries the latest version number which is available on SkypeTalking web site. The type parameter requires either "setup" or "portable" string."""
	global latestVersion
	try:
		requestPage=urllib2.urlopen('http://code.google.com/p/skypetalking/downloads/list#')
		pageContent=requestPage.read()
	except:
		logging.exception("Error accessing request page.")
		displayUpdateStatusMessage(0)
	if type=="setup":
		try:
			latestVersion=pageContent.split("_Setup.exe")[0].split("SkypeTalking_")[1].split("_")[0]
			return latestVersion
		except: displayUpdateStatusMessage(1)
	elif type=="portable":
		try:
			latestVersion=pageContent.split("_Portable.exe")[0].split("SkypeTalking_")[1].split("_")[0]
			return latestVersion
		except: displayUpdateStatusMessage(1)
	else:
		return

def compareVersions(online, running):
	"""Compares the installed version number with the version available on the web site."""
	if running<online:
		askForUpdate()
	elif running>=online:
		displayUpdateStatusMessage(4)

def askForUpdate():
	confirm=wx.MessageDialog(globalVars.Frame, _("Your version: %s. Latest version: %s. Do you wish to download the latest version of %s?")%(currentVersion, latestVersion, versionInfo.name), versionInfo.name+" - "+_("New version available"), wx.YES_NO|wx.YES_DEFAULT|wx.ICON_QUESTION)
	globalVars.Frame.DisplayDialog(confirm)
	answer=confirm.ShowModal()
	if answer==wx.ID_YES:
		globalVars.Frame.CloseDialog(confirm)
		downloadUpdate()
		return
	else:
		output.speak(_("Update cancelled."))
		globalVars.Frame.CloseDialog(confirm)
		return

def downloadUpdate():
	global fileName, downloadDLG
	updDir=locations.dataFilesLocation(u"updates")
	if not os.path.exists(updDir):
		logging.debug("Creating the update directory %s."%updDir)
		try:
			os.mkdir(updDir)
		except:
			logging.exception("Error creating the update directory.")
			displayUpdateStatusMessage(3)
	output.speak(_("Accessing download URL... Please wait..."), True)
	if config.conf["updates"]["downloadType"]==1:
		downloadLink="http://skypetalking.googlecode.com/files/SkypeTalking_"+latestVersion+"_Portable.exe"
		fileName=os.path.join(locations.dataFilesLocation(), u"updates", u"SkypeTalking_"+latestVersion+"_Portable.exe")
	else:
		downloadLink="http://skypetalking.googlecode.com/files/SkypeTalking_"+latestVersion+"_Setup.exe"
		fileName=os.path.join(locations.dataFilesLocation(), u"updates", u"SkypeTalking_"+latestVersion+"_Setup.exe")
	try:
		updURL=urllib2.urlopen(downloadLink)
	except:
		logging.exception("Update URL could not be accessed.")
		displayUpdateStatusMessage(2)
		return
	try:
		downloadDLG=DownloadDialog(parent=globalVars.Frame, title=_("Downloading update... Please wait..."), url=downloadLink, filename=unicode(fileName), completed_callback=runUpdate)
		globalVars.Frame.DisplayDialog(downloadDLG)
		downloadDLG.perform_threaded()
	except:
		logging.exception("Couldn't download update file.")
		displayUpdateStatusMessage(3)

def runUpdate():
	globalVars.Frame.CloseDialog(downloadDLG)
	if fileName.endswith("Setup.exe"):
		info=_("Update ready to install! Choose Ok to exit %s and launch the update installation program.")%versionInfo.name
	else:
		info=_("Update ready! Choose Ok to continue.")
	msg=wx.MessageDialog(globalVars.Frame, info, _("Download completed"), wx.OK|wx.ICON_INFORMATION)
	globalVars.Frame.DisplayDialog(msg)
	answer=msg.ShowModal()
	if answer==wx.ID_OK:
		globalVars.Frame.CloseDialog(msg)
		logging.debug("Closing the application and starting the update.")
		try:
			interface.shutdown(False,True,False)
			wx.CallAfter(launcher.startNewProcess, fileName)
		except:
			logging.exception("Unable to launch the update process.")

def displayUpdateStatusMessage(case):
	msg={}
	if automatic:
		return
	msg[0]=(_("Unable to get online version number, probably due to a lost connection or network maintenance. Please check your connection or try again later."), _("Update error"), wx.ICON_ERROR)
	msg[1]=(_("Unable to find online version number. It may be due to a website temporarily unavailable or it's content being modified. Please try again later."), _("Update error"), wx.ICON_ERROR)
	msg[2]=(_("Couldn't access download URL. Please try again later."), _("Update error"), wx.ICON_ERROR)
	msg[3]=(_("Download failed!"), _("Update error"), wx.ICON_ERROR)
	msg[4]=(_("Your version of %s is up-to-date. Updating is not necessary. Current version: %s. Online version: %s.")%(versionInfo.name, currentVersion, latestVersion), versionInfo.name, wx.ICON_INFORMATION)
	d=wx.MessageDialog(globalVars.Frame, msg[case][0], msg[case][1], msg[case][2])
	globalVars.Frame.DisplayDialog(d)
	if d.ShowModal()==wx.ID_OK:
		globalVars.Frame.CloseDialog(d)
		return

def checkForUpdates():
	if not automatic:
		output.speak(_("Checking for updates... Please wait..."))
	if config.conf["updates"]["downloadType"]==1:
		compareVersions(getOnlineVersion("portable"), currentVersion)
	else:
		compareVersions(getOnlineVersion("setup"), currentVersion)

def autoUpdate():
	global automatic
	if config.conf["updates"]["autoCheckForUpdates"]==True:
		automatic=True
		checkForUpdates()
		automatic=False
	else:
		pass
