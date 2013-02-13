from log import logger
logging = logger.getChild("core.i18n")
import config
import globalVars
from i18n_utils import core
import locations
import versionInfo

def initialize():
	logging.info("Initializing the i18n subsystem.")
	core.set_active_language(versionInfo.name, locations.catalogFilesLocation(), config.conf['general']['language'])

def getAvailableLanguages():
	return core.available_languages(locations.catalogFilesLocation(), versionInfo.name)

def getLangDisplayName(lang):
	return lang['language']

def getAvailableLangDisplayNames():
	langs=getAvailableLanguages()
	return [getLangDisplayName(langs[i]) for i in langs]

def langFromLangDisplayName(language):
	langs=getAvailableLanguages()
	for i in langs:
		if langs[i]['language'] == language:
			return i
