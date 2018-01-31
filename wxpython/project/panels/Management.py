# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/22 19:45'


import wx
from templates import ExperienceAdd
from extra import JsonIO


class TabPanel(ExperienceAdd.TabPanel):
    instructText = u'论文、著作、研究技术报告、重要学术会议邀请报告，10篇以内第一作者或通信作者，按照重要性排序。\n每篇应说明申请人的主要贡献，包括：提出的学术思想、创造性、学术刊物中的主要引用及评价情况等。\n填写顺序：论文、著作、研究技术报告、重要学术会议邀请报告'
    # management = u'代表性论文、著作（包括教材）、研究技术报告、重要学术会议邀请报告'
    def __init__(self, parent):
        ExperienceAdd.TabPanel.__init__(self, parent, u'代表性论著', TabPanel.instructText, 10, [u'论著类型', u'作者（按原排序）', u'题目（名称）', u'论著相关信息', u'主要贡献及引用评价情况'], [200, 250, 250, 300, 300], childOrder=4, hasAttach=True)
        self.allInfo = []

    def addResult(self, addDialog):
        if addDialog.ShowModal() == wx.ID_OK:
            result = addDialog.getInfo()     # 因为添加窗口的getInfo重写，返回了两个值，这里也需要重写
            self.info = result[0]
            self.allInfo.append(result[1])
            self.infoGrid.AppendRows()
            for i in xrange(self.gridCol):
                self.infoGrid.SetCellValue(self.gridRow, i, self.info[self.editInfo[i]])
                self.infoGrid.SetCellAlignment(align=wx.ALIGN_CENTRE, row=self.gridRow, col=i)
                self.infoGrid.AutoSizeRow(self.gridRow)

            self.infoGrid.SetCellValue(self.gridRow, self.gridCol, u'修改')
            self.infoGrid.SetCellValue(self.gridRow, self.gridCol + 1, u'删除')
            self.infoGrid.SetCellFont(self.gridRow, self.gridCol, self.editLinkFont)
            self.infoGrid.SetCellFont(self.gridRow, self.gridCol + 1, self.editLinkFont)
            self.infoGrid.SetCellAlignment(align=wx.ALIGN_CENTRE, row=self.gridRow, col=self.gridCol)
            self.infoGrid.SetCellAlignment(align=wx.ALIGN_CENTRE, row=self.gridRow, col=self.gridCol + 1)

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
            addDialog = CustomDialog(self, u'添加' + self.tabName, self.editInfo, editType=None)
            self.addResult(addDialog)

    def OnGridOperation(self, event):
        row = event.GetRow()
        col = event.GetCol()
        self.operationResult(row, col, CustomDialog)

    def operationResult(self, row, col, AddDialog):
        # 如果点击的是编辑操作那一列
        if col == self.gridCol:
            # 设置传入弹窗的info值
            for i in xrange(self.gridCol):
                self.info[self.editInfo[i]] = self.infoGrid.GetCellValue(row, i)

            # 传附件信息
            self.info['attach'] = self.attaches[row]

            # 重写下面三句##################################################
            editDialog = CustomDialog(self, u'编辑第' + str(row + 1) + u'个' + self.tabName, self.editInfo, editType=self.allInfo[row].get(u'论著类型'))
            editDialog.setInfo(self.allInfo[row])
            ###############################################################
            if editDialog.ShowModal() == wx.ID_OK:
                result = editDialog.getInfo()  # 因为添加窗口的getInfo重写，返回了两个值，这里也需要重写
                self.info = result[0]
                # print self.info
                self.allInfo[row] = result[1]
                for i in xrange(self.gridCol):
                    self.infoGrid.SetCellValue(row, i, self.info[self.editInfo[i]])
                    self.infoGrid.AutoSizeRow(row)
                # 重新设置对应的附件信息
                self.attaches[row] = self.info['attach']

        # 如果点击的是删除操作那一列
        elif col == self.gridCol + 1:
            self.infoGrid.DeleteRows(pos=row, numRows=1)
            self.gridRow -= 1
            self.allInfo.pop(row)       # 加上这一句删除所有信息中的该项
            # 相应的附件也删除
            self.attaches.pop(row)
        else:
            pass

    def addToJsonDict(self):
        JsonIO.repr_results_to_word = []
        for i in xrange(self.gridRow):
            tmp = {}
            tmp['type'] = self.infoGrid.GetCellValue(i, 0)
            tmp['author'] = self.infoGrid.GetCellValue(i, 1)
            tmp['title'] = self.infoGrid.GetCellValue(i, 2)
            tmp['detail_info'] = self.infoGrid.GetCellValue(i, 3)
            tmp['contribution_refs_info'] = self.infoGrid.GetCellValue(i, 4)
            tmp['attach'] = self.attaches[i]

            JsonIO.repr_results_to_word.append(tmp)


class CustomDialog(ExperienceAdd.AddDialog):
    def __init__(self, parent, title, editInfo, editType):
        ExperienceAdd.AddDialog.__init__(self, parent, title, editInfo, size=(1000, 700), editType=editType)
        self.chosenType = ''
        self.singleInfo = {}

    def defineLabelAndInput(self):
        self.managementTypeList = [u'论文', u'著作', u'研究技术报告', u'重要学术会议邀请报告']
        self.gridSizer = wx.GridBagSizer(hgap=0, vgap=0)
        self.HideAndShowComponentLW = []
        self.HideAndShowComponentZZ = []
        self.HideAndShowComponentYJJSBG = []
        self.HideAndShowComponentHYYQBG = []

        # self.chosenType = None

        self.EditLW = []
        self.EditZZ = []
        self.EditYJJSBG = []
        self.EditHYYQBG = []

        for i in xrange(self.infoNum):
            labelName = self.editInfo[i]
            if i < 3:   # 去除类型、作者、题目，因为这3个作为代表性著作标签下的具体内容
                continue
            if i == 3:
                labelName = u'代表性论著'
            self.componentHSizer = wx.BoxSizer(wx.HORIZONTAL)
            if labelName == u'代表性论著':
                self.info['label'][labelName] = wx.StaticText(self.panel, label=labelName + u'：', size=(105, -1))
            else:
                self.info['label'][labelName] = wx.StaticText(self.panel, label=labelName + u'：', size=(160, -1))
            self.info['data'][labelName] = wx.TextCtrl(self.panel, size=(750, 150), style=wx.TE_MULTILINE)

            self.componentHSizer.Add(self.info['label'][labelName], 0, wx.ALIGN_CENTER_HORIZONTAL)
            self.componentHSizer.Add(self.info['data'][labelName], 0, wx.ALIGN_CENTER_HORIZONTAL)

            # 处理代表性论著的录入，神烦
            if labelName == u'代表性论著':
                self.managementType = wx.StaticText(self.panel, label=u'论著类型 ')
                self.managementTypeChoice = wx.ComboBox(self.panel, choices=self.managementTypeList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
                self.managementTypeInstruct = wx.StaticText(self.panel, label=u'（如果你更换了论著类型，之前编辑的其他相关信息将清空）')
                self.managementTypeChoice.Bind(wx.EVT_COMBOBOX, self.managementTypeChosen)
                self.gridSizer.Add(self.managementType, pos=(0,0))
                self.gridSizer.Add(self.managementTypeChoice, pos=(0,1))
                self.gridSizer.Add(self.managementTypeInstruct, pos=(0,2), span=(1, 3))
                # 额外处理
                self.info['label'][u'论著类型'] = self.managementType
                self.info['data'][u'论著类型'] = self.managementTypeChoice

                self.gridSizer.Add((1,3), pos=(1, 0))

                self.author = wx.StaticText(self.panel, label=u'作者（按原排序） ')
                self.authorEdit = wx.TextCtrl(self.panel, size=(300, -1), style = wx.TE_CENTER)
                self.gridSizer.Add(self.author, pos=(2, 0))
                self.gridSizer.Add(self.authorEdit, pos=(2, 1))
                # 额外处理
                self.info['label'][u'作者（按原排序）'] = self.author
                self.info['data'][u'作者（按原排序）'] = self.authorEdit

                self.gridSizer.Add((3, 50), pos=(3, 0))

                # 附件
                self.attach['exist'] = True
                self.chooseButton = wx.Button(self.panel, wx.ID_OPEN, label=u'选择附件', size=(60, 20))
                self.chooseButton.Bind(wx.EVT_BUTTON, self.OnAttach)
                self.attachName = wx.StaticText(self.panel)
                hSizer = wx.BoxSizer(wx.HORIZONTAL)
                hSizer.Add(self.chooseButton, 0, wx.ALIGN_CENTER)
                hSizer.Add((10, 10), 0, wx.ALIGN_CENTER)
                hSizer.Add(self.attachName, 0, wx.ALIGN_CENTER)
                self.gridSizer.Add(hSizer, pos=(2, 4))

                attachInstruct = wx.StaticText(self.panel, label=u'（仅一个PDF文件，不超过5M，\n其中著作附件包含封面、目录、封底）')
                self.gridSizer.Add(attachInstruct, pos=(3, 4))

                # 论文对应的组件 ************************************************************************
                self.topic = wx.StaticText(self.panel, label=u'题目 ')
                self.topicEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.gridSizer.Add(self.topic, pos=(4, 0))
                self.gridSizer.Add(self.topicEdit, pos=(4, 1))
                self.HideAndShowComponentLW.append(self.topic)
                self.HideAndShowComponentLW.append(self.topicEdit)
                self.EditLW.append(self.topicEdit)
                # 额外处理
                self.info['label'][u'题目（名称）'] = self.topic
                self.info['data'][u'题目（名称）'] = self.topicEdit

                self.gridSizer.Add((5, 3), pos=(5, 0))

                self.periodicalName = wx.StaticText(self.panel, label=u'期刊名称 ')
                self.periodicalNameEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.gridSizer.Add(self.periodicalName, pos=(6, 0))
                self.gridSizer.Add(self.periodicalNameEdit, pos=(6, 1))
                self.HideAndShowComponentLW.append(self.periodicalName)
                self.HideAndShowComponentLW.append(self.periodicalNameEdit)
                self.EditLW.append(self.periodicalNameEdit)

                self.gridSizer.Add((7, 3), pos=(7, 0))

                self.juan = wx.StaticText(self.panel, label=u'卷（期）（年） ')
                self.juanEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.gridSizer.Add(self.juan, pos=(8, 0))
                self.gridSizer.Add(self.juanEdit, pos=(8, 1))
                self.HideAndShowComponentLW.append(self.juan)
                self.HideAndShowComponentLW.append(self.juanEdit)
                self.EditLW.append(self.juanEdit)

                self.gridSizer.Add((9, 3), pos=(9, 0))

                self.startEndPage = wx.StaticText(self.panel, label=u'起止页码 ')
                # self.startEndPageEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.startEdit = wx.SpinCtrl(self.panel, min=1, max=10000, size=(50, -1))
                self.toLabel = wx.StaticText(self.panel, label=u'  至  ')
                self.endEdit = wx.SpinCtrl(self.panel, min=1, max=10000, size=(50, -1))
                tmpHSizer = wx.BoxSizer(wx.HORIZONTAL)
                tmpHSizer.Add(self.startEdit, 0, wx.ALIGN_CENTER)
                tmpHSizer.Add(self.toLabel, 0, wx.ALIGN_CENTER)
                tmpHSizer.Add(self.endEdit, 0, wx.ALIGN_CENTER)
                self.gridSizer.Add(self.startEndPage, pos=(10, 0))
                self.gridSizer.Add(tmpHSizer, pos=(10, 1))
                # self.gridSizer.Add(self.startEndPageEdit, pos=(10, 1))
                self.HideAndShowComponentLW.append(self.startEndPage)
                self.HideAndShowComponentLW.append(self.startEdit)
                self.HideAndShowComponentLW.append(self.toLabel)
                self.HideAndShowComponentLW.append(self.endEdit)
                # self.HideAndShowComponentLW.append(self.startEndPageEdit)
                # self.EditLW.append(self.startEndPageEdit)
                self.EditLW.append(self.startEdit)
                self.EditLW.append(self.endEdit)

                self.gridSizer.Add((11, 3), pos=(11, 0))

                self.collect = wx.StaticText(self.panel, label=u'收录 ')
                self.collectEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.gridSizer.Add(self.collect, pos=(12, 0))
                self.gridSizer.Add(self.collectEdit, pos=(12, 1))
                self.HideAndShowComponentLW.append(self.collect)
                self.HideAndShowComponentLW.append(self.collectEdit)
                self.EditLW.append(self.collectEdit)

                self.gridSizer.Add((13, 50), pos=(13, 0))

                self.gridSizer.Add((50, 10), pos=(4, 2))

                # 著作对应的组件布局 *****************************************************************
                self.workName = wx.StaticText(self.panel, label=u'著作名称 ')
                self.workNameEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.gridSizer.Add(self.workName, pos=(4, 3))
                self.gridSizer.Add(self.workNameEdit, pos=(4, 4))
                self.HideAndShowComponentZZ.append(self.workName)
                self.HideAndShowComponentZZ.append(self.workNameEdit)
                self.EditZZ.append(self.workNameEdit)
                # 额外处理
                self.info['label'][u'题目（名称）'] = self.workName
                self.info['data'][u'题目（名称）'] = self.workNameEdit

                self.press = wx.StaticText(self.panel, label=u'出版社 ')
                self.pressEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.gridSizer.Add(self.press, pos=(6, 3))
                self.gridSizer.Add(self.pressEdit, pos=(6, 4))
                self.HideAndShowComponentZZ.append(self.press)
                self.HideAndShowComponentZZ.append(self.pressEdit)
                self.EditZZ.append(self.pressEdit)

                self.pressYear = wx.StaticText(self.panel, label=u'出版年份 ')
                self.yearList = map(lambda x: str(x) + u'年', reversed(xrange(1960, 2018)))
                # self.pressYearEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.pressYearEdit = wx.ComboBox(self.panel, choices=self.yearList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
                self.gridSizer.Add(self.pressYear, pos=(8, 3))
                self.gridSizer.Add(self.pressYearEdit, pos=(8, 4))
                self.HideAndShowComponentZZ.append(self.pressYear)
                self.HideAndShowComponentZZ.append(self.pressYearEdit)
                self.EditZZ.append(self.pressYearEdit)

                self.pressPlace = wx.StaticText(self.panel, label=u'出版地 ')
                self.pressPlaceEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.gridSizer.Add(self.pressPlace, pos=(10, 3))
                self.gridSizer.Add(self.pressPlaceEdit, pos=(10, 4))
                self.HideAndShowComponentZZ.append(self.pressPlace)
                self.HideAndShowComponentZZ.append(self.pressPlaceEdit)
                self.EditZZ.append(self.pressPlaceEdit)

                # 研究技术报告对应的组件布局 ***********************************************************
                self.report = wx.StaticText(self.panel, label=u'报告题目 ')
                self.reportEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.gridSizer.Add(self.report, pos=(14, 0))
                self.gridSizer.Add(self.reportEdit, pos=(14, 1))
                self.HideAndShowComponentYJJSBG.append(self.report)
                self.HideAndShowComponentYJJSBG.append(self.reportEdit)
                self.EditYJJSBG.append(self.reportEdit)
                # 额外处理
                self.info['label'][u'题目（名称）'] = self.report
                self.info['data'][u'题目（名称）'] = self.reportEdit

                self.gridSizer.Add((15, 3), pos=(15, 0))

                self.finishYear = wx.StaticText(self.panel, label=u'完成年份 ')
                # self.finishYearEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.finishYearEdit = wx.ComboBox(self.panel, choices=self.yearList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
                self.gridSizer.Add(self.finishYear, pos=(16, 0))
                self.gridSizer.Add(self.finishYearEdit, pos=(16, 1))
                self.HideAndShowComponentYJJSBG.append(self.finishYear)
                self.HideAndShowComponentYJJSBG.append(self.finishYearEdit)
                self.EditYJJSBG.append(self.finishYearEdit)

                self.gridSizer.Add((17, 3), pos=(17, 0))
                self.gridSizer.Add((19, 3), pos=(19, 0))

                # 重要学术会议邀请报告对应的组件布局 ******************************************************
                self.reportName = wx.StaticText(self.panel, label=u'报告题目 ')
                self.reportNameEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.gridSizer.Add(self.reportName, pos=(14, 3))
                self.gridSizer.Add(self.reportNameEdit, pos=(14, 4))
                self.HideAndShowComponentHYYQBG.append(self.reportName)
                self.HideAndShowComponentHYYQBG.append(self.reportNameEdit)
                self.EditHYYQBG.append(self.reportNameEdit)
                # 额外处理
                self.info['label'][u'题目（名称）'] = self.reportName
                self.info['data'][u'题目（名称）'] = self.reportNameEdit

                self.reportYear = wx.StaticText(self.panel, label=u'报告年份 ')
                # self.reportYearEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.reportYearEdit = wx.ComboBox(self.panel, choices=self.yearList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
                self.gridSizer.Add(self.reportYear, pos=(16, 3))
                self.gridSizer.Add(self.reportYearEdit, pos=(16, 4))
                self.HideAndShowComponentHYYQBG.append(self.reportYear)
                self.HideAndShowComponentHYYQBG.append(self.reportYearEdit)
                self.EditHYYQBG.append(self.reportYearEdit)

                self.meetingName = wx.StaticText(self.panel, label=u'会议名称 ')
                self.meetingNameEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.gridSizer.Add(self.meetingName, pos=(18, 3))
                self.gridSizer.Add(self.meetingNameEdit, pos=(18, 4))
                self.HideAndShowComponentHYYQBG.append(self.meetingName)
                self.HideAndShowComponentHYYQBG.append(self.meetingNameEdit)
                self.EditHYYQBG.append(self.meetingNameEdit)

                self.gridSizer.Add((19, 3), pos=(19, 1))

                self.meetingPlace = wx.StaticText(self.panel, label=u'地点 ')
                self.meetingPlaceEdit = wx.TextCtrl(self.panel, size=(300, -1), style=wx.TE_CENTER)
                self.gridSizer.Add(self.meetingPlace, pos=(20, 3))
                self.gridSizer.Add(self.meetingPlaceEdit, pos=(20, 4))
                self.HideAndShowComponentHYYQBG.append(self.meetingPlace)
                self.HideAndShowComponentHYYQBG.append(self.meetingPlaceEdit)
                self.EditHYYQBG.append(self.meetingPlaceEdit)

                self.gridSizer.Add((21, 20), pos=(21, 1))


                if self.editType == None or self.editType == '':
                    map(lambda x: x.Disable(), self.HideAndShowComponentLW)
                    map(lambda x: x.Disable(), self.HideAndShowComponentZZ)
                    map(lambda x: x.Disable(), self.HideAndShowComponentYJJSBG)
                    map(lambda x: x.Disable(), self.HideAndShowComponentHYYQBG)

                elif self.editType == u'论文':
                    map(lambda x: x.Disable(), self.HideAndShowComponentZZ)
                    map(lambda x: x.Disable(), self.HideAndShowComponentYJJSBG)
                    map(lambda x: x.Disable(), self.HideAndShowComponentHYYQBG)

                elif self.editType == u'著作':
                    map(lambda x: x.Disable(), self.HideAndShowComponentLW)
                    map(lambda x: x.Disable(), self.HideAndShowComponentYJJSBG)
                    map(lambda x: x.Disable(), self.HideAndShowComponentHYYQBG)

                elif self.editType == u'研究技术报告':
                    map(lambda x: x.Disable(), self.HideAndShowComponentLW)
                    map(lambda x: x.Disable(), self.HideAndShowComponentZZ)
                    map(lambda x: x.Disable(), self.HideAndShowComponentHYYQBG)

                else:
                    map(lambda x: x.Disable(), self.HideAndShowComponentLW)
                    map(lambda x: x.Disable(), self.HideAndShowComponentZZ)
                    map(lambda x: x.Disable(), self.HideAndShowComponentYJJSBG)

                self.componentHSizer.Add(self.gridSizer, 8, wx.ALIGN_CENTER_HORIZONTAL)

                # 为了与其他一般形式的输入一致，方便getInfo或setInfo方法的统一，这里设置隐藏的info['data'][labelName]文本框
                self.info['data'][labelName].Hide()

            self.hSizer.append(self.componentHSizer)
            # self.hSizer.append(wx.StaticText(self.panel, size=(-1, 10)))

    def managementTypeChosen(self, event):
        self.chosenType = self.managementTypeList[event.GetSelection()]
        # self.info['data'][u'主要贡献及引用评价情况'].Clear()
        if self.chosenType == u'论文':
            map(lambda x: x.Enable(), self.HideAndShowComponentLW)
            map(lambda x: x.Disable(), self.HideAndShowComponentZZ)
            map(lambda x: x.Disable(), self.HideAndShowComponentYJJSBG)
            map(lambda x: x.Disable(), self.HideAndShowComponentHYYQBG)
            # 清空其他的
            map(lambda x: x.SetValue(''), self.EditZZ)
            map(lambda x: x.SetValue(''), self.EditYJJSBG)
            map(lambda x: x.SetValue(''), self.EditHYYQBG)

        elif self.chosenType == u'著作':
            map(lambda x: x.Disable(), self.HideAndShowComponentLW)
            map(lambda x: x.Enable(), self.HideAndShowComponentZZ)
            map(lambda x: x.Disable(), self.HideAndShowComponentYJJSBG)
            map(lambda x: x.Disable(), self.HideAndShowComponentHYYQBG)
            # 清空其他的
            map(lambda x: x.SetValue('') if type(x) != wx._core.SpinCtrl else x.SetValue('1'), self.EditLW)
            map(lambda x: x.SetValue(''), self.EditYJJSBG)
            map(lambda x: x.SetValue(''), self.EditHYYQBG)

        elif self.chosenType == u'研究技术报告':
            map(lambda x: x.Disable(), self.HideAndShowComponentLW)
            map(lambda x: x.Disable(), self.HideAndShowComponentZZ)
            map(lambda x: x.Enable(), self.HideAndShowComponentYJJSBG)
            map(lambda x: x.Disable(), self.HideAndShowComponentHYYQBG)
            # 清空其他的
            map(lambda x: x.SetValue('') if type(x) != wx._core.SpinCtrl else x.SetValue('1'), self.EditLW)
            map(lambda x: x.SetValue(''), self.EditZZ)
            map(lambda x: x.SetValue(''), self.EditHYYQBG)

        else:
            map(lambda x: x.Disable(), self.HideAndShowComponentLW)
            map(lambda x: x.Disable(), self.HideAndShowComponentZZ)
            map(lambda x: x.Disable(), self.HideAndShowComponentYJJSBG)
            map(lambda x: x.Enable(), self.HideAndShowComponentHYYQBG)
            # 清空其他的
            map(lambda x: x.SetValue('') if type(x) != wx._core.SpinCtrl else x.SetValue('1'), self.EditLW)
            map(lambda x: x.SetValue(''), self.EditZZ)
            map(lambda x: x.SetValue(''), self.EditYJJSBG)


    def getInfo(self):
        info = {}
        for editInfo in self.editInfo:
            labelName = editInfo
            if labelName == u'论著相关信息':
                labelName = u'代表性论著'
            if labelName == u'代表性论著':
                self.singleInfo[u'论著类型'] = self.chosenType
                self.singleInfo[u'作者（按原排序）'] = self.authorEdit.GetValue()
                self.singleInfo[u'题目（名称）'] = ''
                info[u'论著类型'] = self.singleInfo[u'论著类型']
                info[u'作者（按原排序）'] = self.singleInfo[u'作者（按原排序）']

                # value = u'论著类型：%s  作者：%s  ' % (self.singleInfo[u'论著类型'], self.singleInfo[u'作者'])
                value = ''
                if self.chosenType == '':
                    value = ''
                elif self.chosenType == u'论文':
                    self.singleInfo[u'题目'] = self.topicEdit.GetValue()
                    self.singleInfo[u'期刊名称'] = self.periodicalNameEdit.GetValue()
                    self.singleInfo[u'卷（期）（年）'] = self.juanEdit.GetValue()
                    self.singleInfo[u'起页码'] = self.startEdit.GetValue()
                    self.singleInfo[u'止页码'] = self.endEdit.GetValue()
                    self.singleInfo[u'收录'] = self.collectEdit.GetValue()
                    value += u'期刊名称：%s  卷（期）（年）：%s  起止页码：%s至%s  收录：%s' % \
                    (self.singleInfo[u'期刊名称'], self.singleInfo[u'卷（期）（年）'], \
                     self.singleInfo[u'起页码'], self.singleInfo[u'止页码'], self.singleInfo[u'收录'])

                    self.singleInfo[u'题目（名称）'] = self.singleInfo[u'题目']

                elif self.chosenType == u'著作':
                    self.singleInfo[u'著作名称'] = self.workNameEdit.GetValue()
                    self.singleInfo[u'出版社'] = self.pressEdit.GetValue()
                    self.singleInfo[u'出版年份'] = self.pressYearEdit.GetValue()
                    self.singleInfo[u'出版地'] = self.pressPlaceEdit.GetValue()
                    value += u'出版社：%s  出版年份：%s  出版地：%s' % \
                    (self.singleInfo[u'出版社'], self.singleInfo[u'出版年份'], self.singleInfo[u'出版地'])

                    self.singleInfo[u'题目（名称）'] = self.singleInfo[u'著作名称']

                elif self.chosenType == u'研究技术报告':
                    self.singleInfo[u'报告题目'] = self.reportEdit.GetValue()
                    self.singleInfo[u'完成年份'] = self.finishYearEdit.GetValue()
                    value += u'完成年份：%s' % (self.singleInfo[u'完成年份'])

                    self.singleInfo[u'题目（名称）'] = self.singleInfo[u'报告题目']

                else:
                    self.singleInfo[u'报告题目'] = self.reportNameEdit.GetValue()
                    self.singleInfo[u'报告年份'] = self.reportYearEdit.GetValue()
                    self.singleInfo[u'会议名称'] = self.meetingNameEdit.GetValue()
                    self.singleInfo[u'地点'] = self.meetingPlaceEdit.GetValue()
                    value += u'报告年份：%s  会议名称：%s  地点：%s' % \
                    (self.singleInfo[u'报告年份'], self.singleInfo[u'会议名称'], self.singleInfo[u'地点'])

                    self.singleInfo[u'题目（名称）'] = self.singleInfo[u'报告题目']

                self.info['data'][labelName].SetValue(value)
                info[u'论著相关信息'] = self.info['data'][labelName].GetValue()
                self.singleInfo[u'论著相关信息'] = info[u'论著相关信息']

                info[u'题目（名称）'] = self.singleInfo[u'题目（名称）']

            else:
                info[labelName] = self.info['data'][labelName].GetValue()
                self.singleInfo[u'主要贡献及引用评价情况'] = info[labelName]

        info['attach'] = self.attach
        self.singleInfo['attach'] = self.attach

        return [info, self.singleInfo]

    # 设置填写信息
    def setInfo(self, info):
        for editInfo in self.editInfo:
            labelName = editInfo
            value = info[editInfo]
            if labelName == u'论著类型':
                self.chosenType = value
                self.managementTypeChoice.SetValue(self.chosenType)

            elif labelName == u'作者（按原排序）':
                self.authorEdit.SetValue(value)

            elif labelName == u'论著相关信息':
                managementType = info[u'论著类型']
                # self.chosenType = managementType
                # self.managementTypeChoice.SetValue(managementType)
                # self.authorEdit.SetValue(info[u'作者'])

                if managementType == u'论文':
                    self.topicEdit.SetValue(info[u'题目'])
                    self.periodicalNameEdit.SetValue(info[u'期刊名称'])
                    self.juanEdit.SetValue(info[u'卷（期）（年）'])
                    self.startEdit.SetValue(info[u'起页码'])
                    self.endEdit.SetValue(info[u'止页码'])
                    self.collectEdit.SetValue(info[u'收录'])

                elif managementType == u'著作':
                    self.workNameEdit.SetValue(info[u'著作名称'])
                    self.pressEdit.SetValue(info[u'出版社'])
                    self.pressYearEdit.SetValue(info[u'出版年份'])
                    self.pressPlaceEdit.SetValue(info[u'出版地'])

                elif managementType == u'研究技术报告':
                    self.reportEdit.SetValue(info[u'报告题目'])
                    self.finishYearEdit.SetValue(info[u'完成年份'])

                elif managementType == u'重要学术会议邀请报告':
                    self.reportNameEdit.SetValue(info[u'报告题目'])
                    self.reportYearEdit.SetValue(info[u'报告年份'])
                    self.meetingNameEdit.SetValue(info[u'会议名称'])
                    self.meetingPlaceEdit.SetValue(info[u'地点'])

                else:
                    pass

                labelName = u'代表性论著'

            self.info['data'][labelName].SetValue(value)

            self.attach = info['attach']
            self.attachName.SetLabel(self.attach['name'])  # 显示附件名