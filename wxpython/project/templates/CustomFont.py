# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/21 19:28'


''' 自定义的界面各种字体
'''

import wx

class Font(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
    labelFont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
    titleFont = wx.Font(24, wx.MODERN, wx.NORMAL, wx.BOLD)
    instructFont = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
    guideFont = wx.Font(18, wx.MODERN, wx.NORMAL, wx.BOLD)
    editFont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)

