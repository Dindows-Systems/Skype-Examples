#    interface/preferences/categories/baseCategory.py
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

import wx
import wx.lib.sized_controls as sc

class BaseCategory(sc.SizedPanel):
	"""Each preferences category should inherit from this class."""

	def __init__(self, parentTreebook, *args, **kwargs):
		self.parentTreebook=parentTreebook
		super(BaseCategory, self).__init__(parentTreebook, *args, **kwargs)
		self.SetSizerType("vertical")

	def finishSetup(self):
		self._first.Bind(wx.EVT_NAVIGATION_KEY, self.onForwardNavigation)
		self.Bind(wx.EVT_NAVIGATION_KEY, self.onBackwardNavigation)
		ButtonPanel = sc.SizedPanel(self, -1)
		ButtonPanel.SetSizerType("horizontal")
		self.ButtonOK=wx.Button(ButtonPanel, wx.ID_OK)
		self.ButtonCANCEL=wx.Button(ButtonPanel, wx.ID_CANCEL)
		self.ButtonAPPLY=wx.Button(ButtonPanel, wx.ID_APPLY)
		self.ButtonAPPLY.Bind(wx.EVT_SET_FOCUS, self.onFocus)
		self._ApplyWasPrevious = False

	def onForwardNavigation(self, evt):
		if evt.GetDirection() and self._ApplyWasPrevious:
			self._ApplyWasPrevious = False
			self.parentTreebook.GetTreeCtrl().SetFocus()
		else:
			self._ApplyWasPrevious = False
			evt.Skip()

	def onBackwardNavigation(self, evt):
		if not evt.GetDirection() and self._first.HasFocus():
			self.parentTreebook.GetTreeCtrl().SetFocus()
		else:
			evt.Skip()

	def onFocus(self, evt):
		self._ApplyWasPrevious = True
		evt.Skip()
