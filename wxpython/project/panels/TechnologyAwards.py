# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/22 19:46'


import wx
from templates import ExperienceAdd
from extra import JsonIO


class TabPanel(ExperienceAdd.TabPanel):
    instructText = u'按顺序填写全部获奖人姓名（按原顺序）；获奖项目名称；获奖年份、类别及等级，并分别阐述申请人的主要贡献（限100字）。'
    def __init__(self, parent, tabName=u'重要科技奖项情况', instructText=instructText, numLimit=10, editInfo=[u'全部获奖人', u'本人排名', u'获奖项目名称', u'获奖年份', u'获奖类别', u'获奖等级', u'主要贡献'], colSize=[250, 10, 250, 100, 250, 100, 250], childOrder=5, hasAttach=True):
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
        JsonIO.awards = []
        for i in xrange(self.gridRow):
            tmp = {}
            tmp['person_name'] = self.infoGrid.GetCellValue(i, 0)
            tmp['sort'] = self.infoGrid.GetCellValue(i, 1)
            tmp['project_name'] = self.infoGrid.GetCellValue(i, 2)
            tmp['year'] = self.infoGrid.GetCellValue(i, 3)
            tmp['category'] = self.infoGrid.GetCellValue(i, 4)
            tmp['rank'] = self.infoGrid.GetCellValue(i, 5)
            tmp['contribution'] = self.infoGrid.GetCellValue(i, 6)
            tmp['attach'] = self.attaches[i]

            JsonIO.awards.append(tmp)


class CustomDialog(ExperienceAdd.AddDialog):
    def __init__(self, parent, title, editInfo, hasAttach=True):
        ExperienceAdd.AddDialog.__init__(self, parent, title, editInfo, size=(600, 650), hasAttach=hasAttach)

    def defineLabelAndInput(self):
        for i in xrange(self.infoNum):
            labelName = self.editInfo[i]
            hSizer = wx.BoxSizer(wx.HORIZONTAL)
            self.info['label'][labelName] = wx.StaticText(self.panel, label=labelName + u'：', size=(120, -1))
            self.info['data'][labelName] = wx.TextCtrl(self.panel, size=(260, -1), style=wx.TE_CENTER)

            hSizer.Add(self.info['label'][labelName], 0, wx.ALIGN_CENTER)


            if labelName == u'获奖年份':
                self.info['data'][labelName].Hide()
                self.yearList = map(lambda x: str(x) + u'年', reversed(xrange(1960, 2018)))
                self.info['data'][labelName] = wx.ComboBox(self.panel, choices=self.yearList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
                hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)
                hSizer.Add(wx.StaticText(self.panel, size=(192, -1)), 0, wx.ALIGN_CENTER)

            elif labelName == u'获奖等级':
                self.info['data'][labelName].Hide()
                self.awardLevelList = ['特等奖', '一等奖', '二等奖', '三等奖']
                self.info['data'][labelName] = wx.ComboBox(self.panel, choices=self.awardLevelList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
                hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)
                hSizer.Add(wx.StaticText(self.panel, size=(195, -1)), 0, wx.ALIGN_CENTER)

            elif labelName == u'本人排名':
                self.info['data'][labelName].Hide()
                self.info['data'][labelName] = wx.SpinCtrl(self.panel, min=1, max=10000, size=(100, -1))
                hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)
                hSizer.Add(wx.StaticText(self.panel, size=(155, -1)), 0, wx.ALIGN_CENTER)

            elif labelName == u'获奖类别':
                self.info['data'][labelName].Hide()
                self.awardTypeList = ['国家最高科学技术奖', '国家自然科学奖', '国家技术发明奖', '国家科学技术进步奖', '国家教学成果奖',
                                      '军队科学技术进步奖', '国防科学技术进步奖', '军队技术侦察成果奖', '军队教学成果奖', '军队医疗成果奖',
                                      '全军军事科学优秀成果奖', '（可输入其它获奖类别）']
                self.info['data'][labelName] = wx.ComboBox(self.panel, choices=self.awardTypeList, style=wx.CB_DROPDOWN)
                hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)
                hSizer.Add(wx.StaticText(self.panel, size=(100, -1)), 0, wx.ALIGN_CENTER)

            elif labelName == u'主要贡献':
                self.info['data'][labelName].Hide()
                self.info['data'][labelName] = wx.TextCtrl(self.panel, size=(260, 200), style=wx.TE_MULTILINE)
                hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)

            else:
                hSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER)

            self.hSizer.append(hSizer)


