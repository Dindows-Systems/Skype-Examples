from log import logger
logging=logger.getChild('core.config')
import confspecs
import locations
import versionInfo
from UserDict import UserDict
from configobj import ConfigObj, ParseError
from validate import Validator, VdtValueError
import os

configFile=locations.dataFilesLocation(versionInfo.name+".ini")
confspec=ConfigObj(confspecs.defaults, list_values=False, encoding="UTF-8")
confspec.newlines="\r\n"
conf=None

class ConfigurationResetException(Exception):
	pass

class Configuration(UserDict):

	def __init__(self, file=None, spec=None, *args, **kwargs):
		self.file=file
		self.spec=spec
		self.validator=Validator()
		self.setup_config(file=file, spec=spec)
		self.validated=self.config.validate(self.validator, copy=True)
		if self.validated:
			self.write()
		UserDict.__init__(self, self.config)

	def setup_config(self, file, spec):
 #The default way -- load from a file
		try:
			self.config=ConfigObj(infile=file, configspec=spec, create_empty=True, stringify=True)
		except ParseError:
			os.remove(file)
			self.config=ConfigObj(infile=file, configspec=spec, create_empty=True, stringify=True)
			raise ConfigurationResetException

	def __getitem__(self, *args, **kwargs):
		return dict(self.config).__getitem__(*args, **kwargs)

	def __setitem__(self, *args, **kwargs):
		self.config.__setitem__(*args, **kwargs)
		UserDict.__setitem__(self, *args, **kwargs)

	def write(self):
		if hasattr(self.config, 'write'):
			self.config.write()

def initialize():
	global conf
	try:
		conf=Configuration(configFile, confspec)
	except ConfigurationResetException:
		logging.warn("Unable to load configuration file. Loading default configuration instead.")
