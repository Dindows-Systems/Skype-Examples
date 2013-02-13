import subprocess, _subprocess
import sys

SU=subprocess.STARTUPINFO()
SU.dwFlags |= _subprocess.STARTF_USESHOWWINDOW
SU.wShowWindow = _subprocess.SW_HIDE

def restartProcess():
	"""Starts a new instance of the application."""
	if hasattr(sys, 'frozen'):
		subprocess.Popen(unicode(sys.executable), shell=False, startupinfo=SU)
	else:
		subprocess.Popen([unicode(sys.executable), unicode(subprocess.list2cmdline(sys.argv))], shell=False, startupinfo=SU)

def startNewProcess(exeName):
	"""Starts a new process, requires the name or a full path to the process exe file."""
	return subprocess.Popen(unicode(exeName), shell=False, startupinfo=SU)
