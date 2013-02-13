import logging
from logging.handlers import RotatingFileHandler
import locations
import versionInfo

APP_LOG_FILE = versionInfo.name+'.log'
ERROR_LOG_FILE = "error.log"
MESSAGE_FORMAT = "%(asctime)s %(name)s %(levelname)s: %(message)s"
DATE_FORMAT = "%a %b %d, %Y %H:%M:%S"

formatter = logging.Formatter(MESSAGE_FORMAT, datefmt=DATE_FORMAT)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#handlers
app_handler = RotatingFileHandler(locations.dataFilesLocation(APP_LOG_FILE), maxBytes=1000000)
app_handler.setFormatter(formatter)
app_handler.setLevel(logging.DEBUG)
logger.addHandler(app_handler)
error_handler = logging.FileHandler(locations.dataFilesLocation(ERROR_LOG_FILE))
error_handler.setFormatter(formatter)
error_handler.setLevel(logging.ERROR)
logger.addHandler(error_handler)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
