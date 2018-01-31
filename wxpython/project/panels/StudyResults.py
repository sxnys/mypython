# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/19 18:40'


''' 主要研究成果面板
'''

import wx
from extra import JsonIO


class TabPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.tabName = u'主要研究成果'

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

        self.instructText = u'着重阐述近5年来在国防科技领域取得的代表性研究成果，如在国防基础研究领域取得重大发现，在工程研究\n领域突破重大技术瓶颈，在重要型号研制中攻克关键技术难题，或转化应用生产重大军事效益。（2000字内）'
        self.instruct = wx.StaticText(self, label=self.instructText)
        self.instruct.SetFont(instructFont)

        ''' 文本编辑
        '''
        self.grid = wx.GridBagSizer(hgap=0, vgap=0)
        self.studyResultsEdit = wx.TextCtrl(self, size=(1000, 400), style=wx.TE_MULTILINE | wx.VSCROLL)
        self.studyResultsEdit.SetFont(editFont)
        self.grid.Add(self.studyResultsEdit, pos = (0, 0), span=(10, 10), flag=wx.EXPAND)
        self.editObject.append(self.studyResultsEdit)

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
        if self.studyResultsEdit.GetValue().strip() == '':
            dlg = wx.MessageDialog(self, u'请确保内容已填写！', u'提示', wx.OK)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()
            return

        map(lambda x: x.SetEditable(False), self.editObject)
        self.isConfirm = True
        JsonIO.isConfirm[2] = self.isConfirm
        JsonIO.research_result = self.studyResultsEdit.GetValue()

    def OnEdit(self, event):
        map(lambda x: x.SetEditable(True), self.editObject)
        self.isConfirm = False
        JsonIO.isConfirm[2] = self.isConfirm