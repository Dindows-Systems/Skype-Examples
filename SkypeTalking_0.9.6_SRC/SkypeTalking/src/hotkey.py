from log import logger
logging=logger.getChild('core.hotkey')
from ctypes import windll
from copy import deepcopy
import globalVars
import output
import time
import win32api
import win32con #for the VK keycodes
import wx

class HotkeySupport(object):

	def __init__(self, parent, interface, keymap):
		self.parent=parent
		self.interface=interface
		self._lastCommandTime=0
		self._lastCommandCount=0
		self._lastCommandExecuted=None
		self.keymap=keymap
		self.updateDict(self.keymap, keymap)
		new=self.standardizeAllKeystrokes(self.keymap)
		self.keymap.clear()
		self.keymap.update(new)
		logging.debug("Keyboard: Final loaded keymap: %r" % (self.keymap))
		self.replacementMods={}
		self.replacementKeys={"pageup":win32con.VK_PRIOR, "pagedown":win32con.VK_NEXT}
		self.keys={}
		self.defaultKeys=[]
		for i in dir(win32con):
			if i.startswith("VK_"):
				key=i[3:].lower()
				self.replacementKeys[key]=eval("win32con."+i)
				self.defaultKeys.append(i)
			elif i.startswith("MOD_"):
				key=i[4:].lower()
				self.replacementMods[key]=eval("win32con."+i)
		wx.CallAfter(self.registerHotkeys)

	def registerHotkeys(self):
		for func in self.keymap.keys():
			try:
				[mods, key]=self.parseKey(func)
			except:
				logging.exception("Keyboard: No keys returned by ParseKey, ignoring function %s"%func)
				return
			try:
				self.registerHotkey(modifiers=mods, key=key, func=func)
			except:
				logging.exception("Keyboard: Unable to register key %s with modifiers %s and function %s"%(key, mods, func))
				return
		logging.debug("Keyboard: Successfully registered %d keys."%len(self.keys))

	def registerHotkey(self, modifiers=[], key=None, func=None):
		keyId=wx.NewId()
		try:
			self.parent.RegisterHotKey(keyId, modifiers, key)
		except:
			logging.exception("Keyboard: Unable to register hotkey %s with modifiers %s" % (key, modifiers))
			return
		try:
			self.parent.Bind(wx.EVT_HOTKEY, lambda evt: self.processHotkey(evt, keyId), id=keyId)
		except:
			logging.exception("Keyboard: Unable to bind to processHotkey.")
			return
		self.keys[keyId]=func

	def unregisterHotkeys(self):
		cur=len(self.keys)
		logging.debug("Keyboard: Attempting to unregister %d keys."%cur)
		for id in self.keys.keys():
			try:
				self.unregisterHotkey(keyId=id)
			except:
				logging.exception("Keyboard: could not unregister key.")
		logging.debug("Keyboard: unregistered %d keys. Remaining: %r"%(cur-len(self.keys), self.keys))

	def unregisterHotkey(self, keyId=None):
		answer=self.parent.UnregisterHotKey(keyId)
		try:
			what=self.parent.Unbind(wx.EVT_HOTKEY, id=keyId)
		except:
			logging.exception("Keyboard: Could not unbind key %r"%keyId)
		del(self.keys[keyId])

	def parseKey(self, func):
		working=self.keymap[func];
		if not working:
			logging.warning("Keyboard: Unable to parse hotkey for %s"%func)
			return
		working=working.split("+")
		for index, item in enumerate(working[0:-1]):
			if self.replacementMods.has_key(item):
				working[index]=self.replacementMods[item]
		if self.replacementKeys.has_key(working[-1]):
			working[-1]=self.replacementKeys[working[-1]]
		elif len(working[-1])==1:
			if working[-1].isalnum(): working[-1]=ord(str(working[-1]).upper())
			else: working[-1]=win32api.VkKeyScan(str(working[-1]))
		mods=0
		for i in working[:-1]:
			mods=mods|i
		return [mods, working[-1]]

	def processHotkey(self, evt, id):
		output.Silence() #Do not allow echoing of SkypeTalking keystrokes
		func=self.keys[id]
		if globalVars.keyDescriber:
			if func == "KeyDescriberToggle":
				wx.CallAfter(self.executeCommand, func)
			else:
				output.speak(self.keyDescription(func))
		else:
			try:
				commandTime=time.time()
				if (commandTime - self._lastCommandTime) <=0.5 and self._lastCommandExecuted == func:
					self._lastCommandCount+=1
				else:
					self._lastCommandCount=0
				self._lastCommandTime=commandTime
				wx.CallAfter(self.executeCommand, func)
			except:
				logging.exception("Keyboard: Problem initiated by hotkey %s"%evt.m_keyCode)
		evt.Skip()

	def keyDescription(self, func):
		try:
			doc=getattr(self.interface, func).__doc__
			return doc
		except:
			return _("No description")

	def standardizeKey(self, key):
		working=key.split('+')
		working=[i.lower() for i in working]
		answer=[]
		if "control" in working:
			answer.append("control")
		if "win" in working:
			answer.append("win")
		if "alt" in working:
			answer.append("alt")
		if "shift" in working:
			answer.append("shift")
		if working[-1] not in answer:
			answer.append(working[-1])
		return answer

	def standardizeAllKeystrokes(self, keymap):
		full={}
		for i in keymap:
			answer=""
			new=self.standardizeKey(keymap[i])
			for (c, j) in enumerate(new):
				if c < len(new)-1:
					answer="%s%s+" % (answer, j)
				else:
					answer="%s%s" % (answer, j)
			full[i]=answer
		return full

	def executeCommand(self, func):
		try:
			getattr(self.interface, func)(self._lastCommandCount)
			self._lastCommandExecuted=func
		except:
			logging.exception("Keyboard: Error executing function %r bound to key %r" % (func, self.parseKey(func)))

	def getLastCommandRepeatCount(self):
		if (time.time() - self._lastCommandTime)>0.5:
			return 0
		else:
			return self._lastCommandCount

	def updateDict(self, dict1, dict2):
		for key in dict2.keys():
			if key not in dict1.keys():
				dict1[key]=deepcopy(dict2[key])
			elif key in dict1.keys() and hasattr(dict1[key], 'keys') and hasattr(dict2[key], 'keys'):
				self.update_dict(dict1[key], dict2[key])
