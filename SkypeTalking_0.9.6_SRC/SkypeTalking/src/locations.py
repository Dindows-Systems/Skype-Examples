"""
This module is used to retrieve application-dependent paths, such as path to the application executable, data files, catalog and documentation files.
"""

from platform_utils import paths
from platform_utils.paths import merge_paths
import globalVars
import versionInfo
import os
import sys

@merge_paths
def appLocation():
	return paths.app_path()

@merge_paths
def dataFilesLocation():
	dataPathExists=os.path.exists(paths.app_data_path(versionInfo.name))
	if globalVars.installed:
		paths.prepare_app_data_path(versionInfo.name)
	if not globalVars.installed and dataPathExists or globalVars.installed and dataPathExists:
		return paths.app_data_path(versionInfo.name)
	else:
		return paths.app_path()

@merge_paths
def catalogFilesLocation():
	return appLocation(u"locale")

def getDocFilePath(fileName, localized=True):
	import config
	if not getDocFilePath.rootPath:
		if hasattr(sys, "frozen"):
			getDocFilePath.rootPath = appLocation(u"help")
		else:
			getDocFilePath.rootPath = os.path.abspath(os.path.join("..", u"help"))
	if localized:
		lang=config.conf["general"]["language"]
		tryLangs = [lang]
		if "_" in lang:
			tryLangs.append(lang.split("_")[0])
		tryLangs.append("en")
		fileName, fileExt = os.path.splitext(fileName)
		for tryLang in tryLangs:
			tryDir = os.path.join(getDocFilePath.rootPath, tryLang)
			if not os.path.isdir(tryDir):
				continue
			for tryExt in ("html", "txt"):
				tryPath = os.path.join(tryDir, "%s.%s" % (fileName, tryExt))
				if os.path.isfile(tryPath):
					return tryPath
	else:
		if not hasattr(sys, "frozen") and fileName in ("license.txt", "contributors.txt"):
			return os.path.join(paths.app_path(), "..", fileName)
		else:
			return os.path.join(getDocFilePath.rootPath, "..", fileName)
getDocFilePath.rootPath = None
