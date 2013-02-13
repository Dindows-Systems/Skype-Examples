from log import logger
logging=logger.getChild('core.output')
from accessible_output import braille, speech
import config

speaker=brailler=None

def speak(text, interrupt=0):
	global speaker
	if not speaker:
		initialize()
	speaker.say(text,interrupt);
	try:
		if config.conf['output']['enableBrailleOutput']==True:
			Braille(text)
	except TypeError: #The configuration isn't setup
		pass

def Silence():
	global speaker
	if not speaker:
		initialize()
	if config.conf['output']['speechOutput']==1:
		speaker.say("",3);
	else:
		speaker.silence()

def Braille(text, *args, **kwargs):
	#Braille the given text to the display.
	global brailler
	if not config.conf['output']['enableBrailleOutput']:
		return
	if not brailler:
		initialize()
	brailler.braille(text, *args, **kwargs)

def initialize():
	global speaker, brailler
	logging.debug("Initializing output subsystem.")
	try:
		speaker=speech.Speaker()
		brailler=braille.Brailler()
	except:
		return logging.exception("Output: Error during initialization.")
	try:
		if config.conf['output']['speechOutput']==1:
			speaker=speech.Speaker(speech.outputs.Sapi5(rate=config.conf['output']['sapi5SpeechRate'], volume=config.conf['output']['sapi5Volume']))
	except:
		logging.exception("Unable to set sapi speech properties from configuration")
