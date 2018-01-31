# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/19 18:42'


''' 拟展开的研究工作及其军事意义面板
'''

import wx
from extra import JsonIO


class TabPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.tabName = u'拟展开的研究工作'

        self.editObject = list()
        self.isConfirm = False

        self.vSizer = wx.BoxSizer(wx.VERTICAL)

        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        titleFont = wx.Font(24, wx.MODERN, wx.NORMAL, wx.BOLD)
        instructFont = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
        editFont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.SetFont(font)

        self.title = wx.StaticText(self, label=self.tabName)
        self.title.SetFont(titleFont)

        self.instructText = u'着重阐述拟展开的研究工作的创新构思，主要研究方向和初步研究方案，及其军事意义和应用前景。（2000字内）'
        self.instruct = wx.StaticText(self, label=self.instructText)
        self.instruct.SetFont(instructFont)

        ''' 文本编辑
        '''
        self.grid = wx.GridBagSizer(hgap=0, vgap=0)
        self.studyingEdit = wx.TextCtrl(self, size=(1000, 400), style=wx.TE_MULTILINE | wx.VSCROLL)
        self.studyingEdit.SetFont(editFont)
        self.grid.Add(self.studyingEdit, pos=(0, 0), span=(10, 10), flag=wx.EXPAND)
        self.editObject.append(self.studyingEdit)

        '''按钮
        '''
        self.confirmButton = wx.Button(self, label=u'保存')
        self.editButton = wx.Button(self, label=u'编辑')
        self.confirmButton.SetFont(editFont)
        self.editButton.SetFont(editFont)
        self.Bind(wx.EVT_BUTTON, self.OnConfirm, self.confirmButton)
        self.Bind(wx.EVT_BUTTON, self.OnEdit, self.editButton)
        self.hSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hSizer1.Add(self.confirmButton, 0, wx.ALIGN_CENTER)
        self.hSizer1.Add(wx.StaticText(self, size=(100, -1)), 0, wx.ALIGN_CENTER)
        self.hSizer1.Add(self.editButton, 0, wx.ALIGN_CENTER)

        '''整体布局
        '''
        self.vSizer.Add((0, 0), 1)
        self.vSizer.Add(self.title, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(self.instruct, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(self.grid, 6, wx.ALIGN_CENTER)
        self.vSizer.Add(self.hSizer1, 1, wx.ALIGN_CENTER)

        self.SetSizerAndFit(self.vSizer)

    def getTabName(self):
        return self.tabName

    def OnConfirm(self, event):
        if self.studyingEdit.GetValue().strip() == '':
            dlg = wx.MessageDialog(self, u'请确保内容已填写！', u'提示', wx.OK)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()
            return

        map(lambda x: x.SetEditable(False), self.editObject)
        self.isConfirm = True
        JsonIO.isConfirm[3] = self.isConfirm
        JsonIO.work_and_significance = self.studyingEdit.GetValue()

    def OnEdit(self, event):
        map(lambda x: x.SetEditable(True), self.editObject)
        self.isConfirm = False
        JsonIO.isConfirm[3] = self.isConfirm