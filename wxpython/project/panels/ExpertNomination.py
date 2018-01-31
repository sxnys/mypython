# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/26 15:58'

import wx
from extra import JsonIO


class TabPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.tabName = u'专家提名'

        self.editObject = list()
        self.isConfirm = True
        JsonIO.isConfirm[10] = True

        self.vSizer = wx.BoxSizer(wx.VERTICAL)

        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        titleFont = wx.Font(24, wx.MODERN, wx.NORMAL, wx.BOLD)
        titleFont2 = wx.Font(18, wx.MODERN, wx.NORMAL, wx.BOLD)
        instructFont = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
        editFont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.SetFont(font)

        self.title = wx.StaticText(self, label=self.tabName)
        self.title.SetFont(titleFont)

        self.instruct = wx.StaticText(self, label=u'当申报类型选择了专家提名，才需要填写本页信息！点击“编辑”进行填写！专家必须填写三位！')
        self.instruct.SetFont(instructFont)

        self.grid = wx.GridBagSizer(hgap=0, vgap=0)

        # 专家姓名
        self.expertName = []
        self.expertNameEdit = []
        # 专家工作单位
        self.expertDep = []
        self.expertDepEdit = []
        # 专家研究领域
        self.expertField = []
        self.expertFieldEdit = []

        for i in xrange(3):
            self.expertNum = wx.StaticText(self, label=u'专家' + str(i + 1))
            self.expertNum.SetFont(titleFont2)
            self.grid.Add(self.expertNum, pos=(0, 3 * i), span=(1, 2), flag = wx.ALIGN_CENTRE)
            self.grid.Add((-1, 50), pos=(1, 3 * i))

            self.expertName = wx.StaticText(self, label=u'专家姓名：')
            self.expertNameEdit = wx.TextCtrl(self, size=(200, -1), style = wx.TE_CENTER)
            self.expertNameEdit.SetFont(editFont)
            self.editObject.append(self.expertNameEdit)

            self.expertDep = wx.StaticText(self, label=u'工作单位：')
            self.expertDepEdit = wx.TextCtrl(self, size=(200, -1), style = wx.TE_CENTER)
            self.expertDepEdit.SetFont(editFont)
            self.editObject.append(self.expertDepEdit)

            self.expertField = wx.StaticText(self, label=u'研究领域：')
            self.expertFieldEdit = wx.TextCtrl(self, size=(200, -1), style = wx.TE_CENTER)
            self.expertFieldEdit.SetFont(editFont)
            self.editObject.append(self.expertFieldEdit)

            self.grid.Add(self.expertName, pos=(2, 3 * i))
            self.grid.Add(self.expertNameEdit, pos=(2, 3 * i + 1))

            self.grid.Add((-1, 30), pos=(3, 3 * i))

            self.grid.Add(self.expertDep, pos=(4, 3 * i))
            self.grid.Add(self.expertDepEdit, pos=(4, 3 * i + 1))

            self.grid.Add((-1, 30), pos=(5, 3 * i))

            self.grid.Add(self.expertField, pos=(6, 3 * i))
            self.grid.Add(self.expertFieldEdit, pos=(6, 3 * i + 1))

            if i < 2:
                self.grid.Add((150, -1), pos=(0, 3 * i + 2))

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
        self.vSizer.Add(self.grid, 3, wx.ALIGN_CENTER)
        self.vSizer.Add(self.hSizer1, 1, wx.ALIGN_CENTER)

        self.SetSizerAndFit(self.vSizer)

        map(lambda x: x.Disable(), self.editObject)

    def getTabName(self):
        return self.tabName

    def OnConfirm(self, event):
        if JsonIO.isConfirm[0] == False or JsonIO.cover['type'] == u'单位推荐' or JsonIO.cover['type'] == '':
            JsonIO.isConfirm[10] = True
            return

        isEditAll = reduce(lambda x, y: x and y, map(lambda x: x.GetValue().strip() != '', self.editObject) )
        if isEditAll == False:
            dlg = wx.MessageDialog(self, u'请确保所有信息均填写！', u'提示', wx.OK)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()
            return

        map(lambda x: x.Disable(), self.editObject)
        self.isConfirm = True
        JsonIO.isConfirm[10] = self.isConfirm

        for i in xrange(3):
            tmp = {}
            tmp['name'] = self.editObject[i * 3].GetValue()
            tmp['working_dep'] = self.editObject[i * 3 + 1].GetValue()
            tmp['filed'] = self.editObject[i * 3 + 2].GetValue()
            JsonIO.JsonDict['expert'].append(tmp)


    def OnEdit(self, event):
        if JsonIO.isConfirm[0] == False or JsonIO.cover['type'] == u'单位推荐' or JsonIO.cover['type'] == '':
            JsonIO.isConfirm[10] = True
            return
        map(lambda x: x.Enable(True), self.editObject)
        self.isConfirm = False
        JsonIO.isConfirm[10] = self.isConfirm