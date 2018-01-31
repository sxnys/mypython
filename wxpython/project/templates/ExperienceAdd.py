# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/21 17:26'


'''个人经历方面的信息（学习经历、工作经历、承担国防相关代表性项目情况）添加的模板类
'''

import os
import wx
import wx.grid
from extra import JsonIO
import base64


class TabPanel(wx.Panel):
    def __init__(self, parent, tabName, instructText, numLimit, editInfo, colSize, childOrder = 1, hasAttach=False):
        wx.Panel.__init__(self, parent)
        self.tabName = tabName

        self.childOrder = childOrder       # 标记是第几个子类

        self.editObject = list()
        self.isConfirm = False

        self.hasAttach = hasAttach
        self.attaches = []      # 附件

        self.info = {}  # 临时存储表格某一行数据

        self.editInfo = editInfo
        self.numLimit = numLimit

        self.vSizer = wx.BoxSizer(wx.VERTICAL)
        # self.grid = wx.GridBagSizer(hgap=0, vgap=0)

        self.font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.titleFont = wx.Font(24, wx.MODERN, wx.NORMAL, wx.BOLD)
        self.instructFont = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
        self.editFont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.editLinkFont = wx.Font(12, wx.MODERN, wx.NORMAL, wx.BOLD)
        self.SetFont(self.font)

        self.title = wx.StaticText(self, label=self.tabName)
        self.title.SetFont(self.titleFont)

        self.instructText = instructText
        self.instruct = wx.StaticText(self, label=self.instructText)
        self.instruct.SetFont(self.instructFont)

        '''处理表格
        '''
        self.panel = wx.Panel(self)
        self.infoLabelNum = len(editInfo)
        self.infoGrid = wx.grid.Grid(self)
        self.infoGrid.AutoSizeColumns()
        self.infoGrid.AutoSizeRows()
        self.gridRow = 0
        self.gridCol = self.infoLabelNum
        self.infoGrid.CreateGrid(self.gridRow, self.gridCol + 2)
        for col in xrange(self.gridCol):
            self.infoGrid.SetColLabelValue(col, editInfo[col])
            self.infoGrid.SetColSize(col, colSize[col])
        # self.infoGrid.SetDefaultColSize(250)
        self.infoGrid.SetDefaultRowSize(30)
        self.infoGrid.SetDefaultCellFont(self.editFont)
        self.infoGrid.SetDefaultCellAlignment(wx.CENTRE, wx.CENTRE)
        # self.infoGrid.ClipVertGridLines(True)
        self.infoGrid.SetDefaultCellOverflow(False)

        # 设置编辑操作的列
        self.infoGrid.SetColLabelValue(self.gridCol, u'操作1')
        self.infoGrid.SetColSize(self.gridCol, 40)
        # 设置删除操作的列
        self.infoGrid.SetColLabelValue(self.gridCol + 1, u'操作2')
        self.infoGrid.SetColSize(self.gridCol + 1, 40)
        self.infoGrid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.OnGridOperation)

        self.infoGrid.EnableEditing(False)
        # print self.infoGrid.GetDefaultCellAlignment()

        '''按钮
        '''
        self.addButton = wx.Button(self, label=u'添加')
        self.confirmButton = wx.Button(self, label=u'保存')
        self.editButton = wx.Button(self, label=u'编辑')
        self.addButton.SetFont(self.editFont)
        self.confirmButton.SetFont(self.editFont)
        self.editButton.SetFont(self.editFont)
        self.Bind(wx.EVT_BUTTON, self.OnAdd, self.addButton)
        self.Bind(wx.EVT_BUTTON, self.OnConfirm, self.confirmButton)
        self.Bind(wx.EVT_BUTTON, self.OnEdit, self.editButton)
        self.hSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hSizer1.Add(self.addButton, 0, wx.ALIGN_CENTER)
        self.hSizer1.Add(wx.StaticText(self, size=(100, -1)), 0, wx.ALIGN_CENTER)
        self.hSizer1.Add(self.confirmButton, 0, wx.ALIGN_CENTER)
        self.hSizer1.Add(wx.StaticText(self, size=(100, -1)), 0, wx.ALIGN_CENTER)
        self.hSizer1.Add(self.editButton, 0, wx.ALIGN_CENTER)

        '''整体布局
        '''
        self.vSizer.Add((0, 0), 1)
        self.vSizer.Add(self.title, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(self.instruct, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(self.infoGrid, 6, wx.ALIGN_CENTER)
        self.vSizer.Add(self.hSizer1, 1, wx.ALIGN_CENTER)

        self.SetSizerAndFit(self.vSizer)

    def getTabName(self):
        return self.tabName

    def addResult(self, addDialog):
        # print self.hasAttach
        if addDialog.ShowModal() == wx.ID_OK:
            self.info = addDialog.getInfo()
            self.infoGrid.AppendRows()
            for i in xrange(self.gridCol):
                self.infoGrid.SetCellValue(self.gridRow, i, unicode(self.info[self.editInfo[i]]) )
                # 设置自适应和对齐方式
                # self.infoGrid.AutoSizeColumn(i)
                self.infoGrid.AutoSizeRow(self.gridRow)
                # self.infoGrid.AutoSize()
                self.infoGrid.SetCellAlignment(align=wx.ALIGN_CENTRE, row=self.gridRow, col=i)

            self.infoGrid.SetCellValue(self.gridRow, self.gridCol, u'修改')
            self.infoGrid.SetCellValue(self.gridRow, self.gridCol + 1, u'删除')
            self.infoGrid.SetCellFont(self.gridRow, self.gridCol, self.editLinkFont)
            self.infoGrid.SetCellFont(self.gridRow, self.gridCol + 1, self.editLinkFont)
            self.infoGrid.SetCellAlignment(align=wx.ALIGN_CENTRE, row=self.gridRow, col=self.gridCol)
            self.infoGrid.SetCellAlignment(align=wx.ALIGN_CENTRE, row=self.gridRow, col=self.gridCol+1)

            self.gridRow += 1
            # 附件添加
            self.attaches.append(self.info['attach'])

    def OnAdd(self, event):
        if self.isConfirm:
            pass
        elif self.gridRow == self.numLimit:
            dlg = wx.MessageDialog(self, u'最多添加' + str(self.numLimit) + u'项！', u'提示', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            # 添加弹窗
            addDialog = AddDialog(self, u'添加' + self.tabName, self.editInfo, hasAttach=self.hasAttach)
            self.addResult(addDialog)

    def addToJsonDict(self):
        pass

    def OnConfirm(self, event):
        if self.gridRow == 0:
            dlg = wx.MessageDialog(self, u'请确保至少添加一条记录！', u'提示', wx.OK)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()
            return
        self.infoGrid.Disable()
        self.isConfirm = True
        JsonIO.isConfirm[3 + self.childOrder] = self.isConfirm
        self.addToJsonDict()

    def OnEdit(self, event):
        self.infoGrid.Enable()
        self.isConfirm = False
        JsonIO.isConfirm[3 + self.childOrder] = self.isConfirm

    def operationResult(self, row, col, Dialog):
        # 如果点击的是编辑操作那一列
        if col == self.gridCol:
            # 设置传入弹窗的info值
            for i in xrange(self.gridCol):
                self.info[self.editInfo[i]] = self.infoGrid.GetCellValue(row, i)

            # 传附件信息
            self.info['attach'] = self.attaches[row]

            # print self.hasAttach
            editDialog = Dialog(self, u'编辑第' + str(row + 1) + u'个' + self.tabName, self.editInfo, hasAttach=self.hasAttach)
            editDialog.setInfo(self.info)
            if editDialog.ShowModal() == wx.ID_OK:
                self.info = editDialog.getInfo()
                for i in xrange(self.gridCol):
                    self.infoGrid.SetCellValue(row, i, unicode(self.info[self.editInfo[i]]) )
                    self.infoGrid.AutoSizeRow(row)
                # 重新设置对应的附件信息
                self.attaches[row] = self.info['attach']
        # 如果点击的是删除操作那一列
        elif col == self.gridCol + 1:
            self.infoGrid.DeleteRows(pos=row, numRows=1)
            self.gridRow -= 1
            # 相应的附件也删除
            self.attaches.pop(row)
        else:
            pass

    def OnGridOperation(self, event):
        row = event.GetRow()
        col = event.GetCol()
        self.operationResult(row, col, AddDialog)
        # # 如果点击的是编辑操作那一列
        # if col == self.gridCol:
        #     # 设置传入弹窗的info值
        #     for i in xrange(self.gridCol):
        #         self.info[self.editInfo[i]] = self.infoGrid.GetCellValue(row, i)
        #     editDialog = AddDialog(self, u'编辑第' + str(row + 1) + u'个' + self.tabName, self.editInfo)
        #     editDialog.setInfo(self.info)
        #     if editDialog.ShowModal() == wx.ID_OK:
        #         self.info = editDialog.getInfo()
        #         for i in xrange(self.gridCol):
        #             self.infoGrid.SetCellValue(row, i, self.info[self.editInfo[i]])
        # # 如果点击的是删除操作那一列
        # elif col == self.gridCol + 1:
        #     self.infoGrid.DeleteRows(pos=row, numRows=1)
        #     self.gridRow -= 1
        # else:
        #     pass


''' 添加弹窗
'''
class AddDialog(wx.Dialog):
    def __init__(self, parent, title, editInfo, size=(600, 400), row=0, editType=None, hasAttach=False):
        super(AddDialog, self).__init__(parent, title=title, size=size)
        self.panel = wx.Panel(self)

        self.yearList = map(lambda x: str(x) + u'年', reversed(xrange(1960, 2018)))
        self.editFont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)

        self.info = {'label': {}, 'data': {}}
        self.hSizer = list()
        self.vSizer = wx.BoxSizer(wx.VERTICAL)

        self.attach = {'exist': hasAttach, 'name': '', 'resource': ''}

        self.editInfo = editInfo
        self.infoNum = len(editInfo)

        self.editType = editType

        # for i in xrange(self.infoNum):
        #     labelName = editInfo[i]
        #     print labelName
        #     self.info['label'][labelName] = wx.StaticText(self.panel, label=labelName+u'：', size=(120, -1))
        #     self.info['data'][labelName] = wx.TextCtrl(self.panel, size=(240, -1), style=wx.TE_CENTER)
        #     self.info['data'][labelName].SetFont(self.editFont)
        #     hSizer = wx.BoxSizer(wx.HORIZONTAL)
        #     hSizer.Add(self.info['label'][labelName], 0, wx.ALIGN_CENTER)
        #     hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)
        #     self.hSizer.append(hSizer)
        #     # self.vSizer.Add(hSizer, 1, wx.ALIGN_CENTER)
        self.defineLabelAndInput()

        if hasAttach:
            self.attach['exist'] = True
            self.chooseButton = wx.Button(self.panel, wx.ID_OPEN, label = u'选择附件', size = (60, 20))
            self.chooseButton.Bind(wx.EVT_BUTTON, self.OnAttach)
            self.attachName = wx.StaticText(self.panel)
            hSizer = wx.BoxSizer(wx.HORIZONTAL)
            hSizer.Add(self.chooseButton, 0, wx.ALIGN_CENTER)
            hSizer.Add((10, 10), 0, wx.ALIGN_CENTER)
            hSizer.Add(self.attachName, 0, wx.ALIGN_CENTER)
            # self.hSizer.append(hSizer)

            vSizer =wx.BoxSizer(wx.VERTICAL)
            vSizer.Add((0, 0), 1, wx.ALIGN_CENTER)
            attachInstruct = wx.StaticText(self.panel, label=u'（大小不超过5M，仅PDF文件）')
            vSizer.Add(hSizer, 0, wx.ALIGN_CENTER)
            vSizer.Add(attachInstruct, 0, wx.ALIGN_CENTER)
            self.hSizer.append(vSizer)


        self.confirmButton = wx.Button(self.panel, wx.ID_OK, label=u'保存', size=(70, 30))
        self.cancelButton = wx.Button(self.panel, wx.ID_CANCEL, label=u'取消', size=(70, 30))
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        hSizer.Add(self.confirmButton, 0, wx.ALIGN_CENTER)
        hSizer.Add(wx.StaticText(self.panel, size=(100, -1)), 0, wx.ALIGN_CENTER)
        hSizer.Add(self.cancelButton, 0, wx.ALIGN_CENTER)
        self.hSizer.append(hSizer)

        self.vSizer.Add((0, 0), 1, wx.ALIGN_CENTER)
        for sizer in self.hSizer:
            self.vSizer.Add(sizer, 2, wx.ALIGN_CENTER)
        self.vSizer.Add((0, 0), 1, wx.ALIGN_CENTER)

        self.panel.SetSizerAndFit(self.vSizer)

    def defineLabelAndInput(self):
        for i in xrange(self.infoNum):
            labelName = self.editInfo[i]
            # print labelName
            self.info['label'][labelName] = wx.StaticText(self.panel, label=labelName + u'：', size=(120, -1))
            if labelName == u'本人承担任务':      # 在承担国防相关代表性项目情况中这里要求为文本域
                self.info['data'][labelName] = wx.TextCtrl(self.panel, size=(240, -1), style=wx.TE_MULTILINE)
            else:
                self.info['data'][labelName] = wx.TextCtrl(self.panel, size=(240, -1), style=wx.TE_CENTER)
            # self.info['data'][labelName].SetFont(self.editFont)
            hSizer = wx.BoxSizer(wx.HORIZONTAL)
            hSizer.Add(self.info['label'][labelName], 0, wx.ALIGN_CENTER)
            hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)
            self.hSizer.append(hSizer)

    # 返回填写信息
    def getInfo(self):
        info = {}
        for editInfo in self.editInfo:
            labelName = editInfo
            info[labelName] = self.info['data'][labelName].GetValue()
        # 添加附件信息
        # info['attach']['name'] = self.attach['name']
        # info['attach']['resource'] = self.attach['resource']
        info['attach'] = self.attach
        return info

    # 设置填写信息
    def setInfo(self, info):
        for editInfo in self.editInfo:
            labelName = editInfo
            self.info['data'][labelName].SetValue(info[labelName])
        # 设置附件信息
        # self.attach['name'] = info['attach']['name']
        # self.attach['resource'] = info['attach']['resource']
        self.attach = info['attach']
        self.attachName.SetLabel(self.attach['name'])   # 显示附件名

    # 处理选择附件
    def OnAttach(self, event):
        # wildcard = "Text Files (*.txt)|*.txt|Doc Files (*.doc)|*.doc|Docx Files (*.docx)|*.docx|" \
        #            "Pdf Files (*.pdf)|*.pdf|JPG Files (*.jpg)|*.jpg|JEPG Files (*.jepg)|*.jepg|All Files (*.*)|*.*"

        wildcard = u'PDF 文件 (*.pdf)|*.pdf'

        cwd = os.getcwd()
        dlg = wx.FileDialog(self, u'添加附件', cwd, "", wildcard=wildcard, style=wx.ID_OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            self.attach['name'] = dlg.GetPath().split('\\')[-1]     # 获取附件文件名
            self.attachName.SetLabel(self.attach['name'])

            with open(dlg.GetPath(), 'rb') as f:    # 获取附件的二进制文件
                data = base64.b64encode(f.read())
                self.attach['resource'] = data

        os.chdir(cwd)   # 因为选择文件的时候可能会改变工作环境，把它再重置回来
        dlg.Destroy()