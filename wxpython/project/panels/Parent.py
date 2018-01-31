# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/22 19:46'


import wx
from templates import ExperienceAdd
from extra import JsonIO


class TabPanel(ExperienceAdd.TabPanel):
    instructText = u'\t\t\t请务必填写已授权的发明专利或国防专利！\n请按顺序填写专利申报人（按原排序）；专利名称；申请年份、申请号；批准年份、专利号。\n并分别简述专利实施情况和申请人在专利发明和实施中的主要贡献（100字以内）。'
    def __init__(self, parent, tabName=u'发明专利、国防专利情况', instructText=instructText, numLimit=10, editInfo=[u'专利申报人（按原排序）', u'专利名称', u'申请年份', u'申请号', u'批准年份', u'专利号', u'主要贡献及专利实施情况'], colSize=[250, 250, 100, 250, 100, 250, 300], childOrder=6, hasAttach=True):
        ExperienceAdd.TabPanel.__init__(self, parent, tabName, instructText, numLimit, editInfo, colSize, childOrder=childOrder, hasAttach=hasAttach)

    def OnAdd(self, event):
        if self.isConfirm:
            pass
        elif self.gridRow == self.numLimit:
            dlg = wx.MessageDialog(self, u'最多添加' + str(self.numLimit) + u'项！', u'提示', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            # 添加弹窗
            addDialog = CustomDialog(self, u'添加' + self.tabName, self.editInfo)
            self.addResult(addDialog)

    def OnGridOperation(self, event):
        row = event.GetRow()
        col = event.GetCol()
        self.operationResult(row, col, CustomDialog)

    def addToJsonDict(self):
        JsonIO.patent = []
        for i in xrange(self.gridRow):
            tmp = {}
            tmp['person_name'] = self.infoGrid.GetCellValue(i, 0)
            tmp['patent_name'] = self.infoGrid.GetCellValue(i, 1)
            tmp['year'] = self.infoGrid.GetCellValue(i, 2)
            tmp['application_num'] = self.infoGrid.GetCellValue(i, 3)
            tmp['approved_year'] = self.infoGrid.GetCellValue(i, 4)
            tmp['patent_num'] = self.infoGrid.GetCellValue(i, 5)
            tmp['contribution_conduct'] = self.infoGrid.GetCellValue(i, 6)
            tmp['attach'] = self.attaches[i]

            JsonIO.patent.append(tmp)


class CustomDialog(ExperienceAdd.AddDialog):
    def __init__(self, parent, title, editInfo, hasAttach=True):
        ExperienceAdd.AddDialog.__init__(self, parent, title, editInfo, size=(600, 650), hasAttach=hasAttach)

    def defineLabelAndInput(self):
        for i in xrange(self.infoNum):
            labelName = self.editInfo[i]
            hSizer = wx.BoxSizer(wx.HORIZONTAL)
            self.info['label'][labelName] = wx.StaticText(self.panel, label=labelName + u'：', size=(150, -1))
            self.info['data'][labelName] = wx.TextCtrl(self.panel, size=(260, -1), style=wx.TE_CENTER)

            hSizer.Add(self.info['label'][labelName], 0, wx.ALIGN_CENTER)

            if labelName == u'申请年份':
                self.info['data'][labelName].Hide()
                self.info['data'][labelName] = wx.ComboBox(self.panel, choices=self.yearList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
                hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)
                hSizer.Add(wx.StaticText(self.panel, size=(192, -1)), 0, wx.ALIGN_CENTER)

            elif labelName == u'批准年份':
                self.info['data'][labelName].Hide()
                self.info['data'][labelName] = wx.ComboBox(self.panel, choices=self.yearList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
                hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)
                hSizer.Add(wx.StaticText(self.panel, size=(192, -1)), 0, wx.ALIGN_CENTER)

            elif labelName == u'主要贡献及专利实施情况':
                self.info['data'][labelName].Hide()
                self.info['data'][labelName] = wx.TextCtrl(self.panel, size=(260, 200), style=wx.TE_MULTILINE)
                hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)

            else:
                hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)

            self.hSizer.append(hSizer)
