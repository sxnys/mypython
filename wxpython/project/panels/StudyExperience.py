# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/21 20:04'

import wx
from templates import ExperienceAdd
from extra import JsonIO


class TabPanel(ExperienceAdd.TabPanel):
    def __init__(self, parent, tabName=u'学习经历', instructText=u'从大学教育填起', numLimit=10, editInfo=[u'起止年月', u'校（院）及系名称', u'专业', u'学位'], colSize=[250, 250, 250, 250], childOrder=1, hasAttach=False):
        ExperienceAdd.TabPanel.__init__(self, parent, tabName, instructText, numLimit, editInfo, colSize, childOrder=childOrder)

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
        JsonIO.learning_exp = []
        for i in xrange(self.gridRow):
            tmp = {}
            tmp['start_end_date'] = self.infoGrid.GetCellValue(i, 0)
            tmp['school_name'] = self.infoGrid.GetCellValue(i, 1)
            tmp['major_subject'] = self.infoGrid.GetCellValue(i, 2)
            tmp['bachelor'] = self.infoGrid.GetCellValue(i, 3)
            JsonIO.learning_exp.append(tmp)


class CustomDialog(ExperienceAdd.AddDialog):
    def __init__(self, parent, title, editInfo, hasAttach=False):
        ExperienceAdd.AddDialog.__init__(self, parent, title, editInfo, hasAttach=hasAttach)

    def defineLabelAndInput(self):
        for i in xrange(self.infoNum):
            labelName = self.editInfo[i]
            hSizer = wx.BoxSizer(wx.HORIZONTAL)
            self.info['label'][labelName] = wx.StaticText(self.panel, label=labelName + u'：', size=(120, -1))

            if labelName == u'本人承担任务':      # 在承担国防相关代表性项目情况中这里要求为文本域
                self.info['data'][labelName] = wx.TextCtrl(self.panel, size=(260, 120), style=wx.TE_MULTILINE)
            else:
                self.info['data'][labelName] = wx.TextCtrl(self.panel, size=(260, -1), style=wx.TE_CENTER)

            hSizer.Add(self.info['label'][labelName], 0, wx.ALIGN_CENTER)
            hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)

            if labelName == u'起止年月':
                self.yearList = map(lambda x: str(x) + u'年', reversed(xrange(1960, 2018)))
                self.monthList = map(lambda x: str(x) + u'月', xrange(1, 13))
                self.startYear = wx.ComboBox(self.panel, choices=self.yearList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
                self.startMonth = wx.ComboBox(self.panel, choices=self.monthList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
                self.toText = wx.StaticText(self.panel, label=u' 至 ')
                self.endYear = wx.ComboBox(self.panel, choices=self.yearList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
                self.endMonth = wx.ComboBox(self.panel, choices=self.monthList, style=wx.CB_DROPDOWN | wx.CB_READONLY)

                hSizer.Add(self.startYear, 0, wx.ALIGN_CENTER)
                hSizer.Add(self.startMonth, 0, wx.ALIGN_CENTER)
                hSizer.Add(self.toText, 0, wx.ALIGN_CENTER)
                hSizer.Add(self.endYear, 0, wx.ALIGN_CENTER)
                hSizer.Add(self.endMonth, 0, wx.ALIGN_CENTER)

                # 为了与其他一般形式的输入一致，方便getInfo或setInfo方法的统一，这里设置隐藏的info['data'][labelName]文本框
                self.info['data'][labelName].Hide()

            self.hSizer.append(hSizer)

    def getInfo(self):
        info = {}
        for editInfo in self.editInfo:
            labelName = editInfo
            if labelName == u'起止年月':
                value = u'%s%s 至 %s%s' % (self.startYear.GetValue(), self.startMonth.GetValue(), self.endYear.GetValue(), self.endMonth.GetValue())
                self.info['data'][labelName].SetValue(value)
            info[labelName] = self.info['data'][labelName].GetValue()

        info['attach'] = self.attach
        return info

    # 设置填写信息
    def setInfo(self, info):
        for editInfo in self.editInfo:
            labelName = editInfo
            value = info[editInfo]
            if labelName == u'起止年月':
                startYear = value[:5]
                startMonth = value[5:7]
                endYear = value[10:15]
                endMonth = value[15:]
                self.startYear.SetValue(startYear)
                self.startMonth.SetValue(startMonth)
                self.endYear.SetValue(endYear)
                self.endMonth.SetValue(endMonth)
            self.info['data'][labelName].SetValue(value)
