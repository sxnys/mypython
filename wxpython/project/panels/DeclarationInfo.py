# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/19 18:33'


''' 申报信息面板
'''

import wx
from extra import JsonIO


class TabPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.tabName = u'申报信息'

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

        self.typeInstruct = wx.StaticText(self, label=u'如果选择专家提名，请在“专家提名”填写页添加相关信息！')
        self.typeInstruct.SetFont(instructFont)

        self.typeLabel = wx.StaticText(self, label=u'申报类型：', size = (100, -1))
        self.type = u'单位推荐'
        self.radioButton1 = wx.RadioButton(self, 1, label=u'单位推荐', size = (150, -1), style = wx.RB_GROUP)
        self.radioButton2 = wx.RadioButton(self, 1, label=u'专家提名', size = (150, -1))
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioGroup)
        hSizer0 = wx.BoxSizer(wx.HORIZONTAL)
        hSizer0.Add(self.typeLabel, 0, wx.ALIGN_CENTER)
        hSizer0.Add(self.radioButton1, 0, wx.ALIGN_CENTER)
        hSizer0.Add(self.radioButton2, 0, wx.ALIGN_CENTER)
        self.editObject.append(self.radioButton1)
        self.editObject.append(self.radioButton2)

        self.applicantLabel = wx.StaticText(self, label=u'申请人：', size = (100, -1))
        self.applicant = wx.TextCtrl(self, size=(300, -1), style = wx.TE_CENTER)
        self.applicant.SetFont(editFont)
        hSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hSizer1.Add(self.applicantLabel, 0, wx.ALIGN_CENTER)
        hSizer1.Add(self.applicant, 0, wx.ALIGN_CENTER)
        self.editObject.append(self.applicant)

        self.projectNameLabel = wx.StaticText(self, label=u'项目名称：', size = (100, -1))
        self.projectName = wx.TextCtrl(self, size=(300, -1), style = wx.TE_CENTER)
        self.projectName.SetFont(editFont)
        hSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hSizer2.Add(self.projectNameLabel, 0, wx.ALIGN_CENTER)
        hSizer2.Add(self.projectName, 0, wx.ALIGN_CENTER)
        self.editObject.append(self.projectName)

        self.fieldLabel = wx.StaticText(self, label=u'申报领域：', size = (100, -1))
        self.fieldList = [u'陆战', u'海洋', u'航空', u'航天', u'电子', u'网络信息', u'核技术',
                          u'精确打击', u'材料', u'制造', u'生物及军事医学']
        self.field = wx.ComboBox(self, choices = self.fieldList, size=(300, -1), style = wx.CB_DROPDOWN | wx.CB_READONLY)
        self.field.SetFont(editFont)
        hSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hSizer3.Add(self.fieldLabel, 0, wx.ALIGN_CENTER)
        hSizer3.Add(self.field, 0, wx.ALIGN_CENTER)
        self.editObject.append(self.field)

        self.workspaceLabel = wx.StaticText(self, label=u'工作单位：', size = (100, -1))
        self.workspace = wx.TextCtrl(self, size=(300, -1), style = wx.TE_CENTER)
        self.workspace.SetFont(editFont)
        hSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        hSizer4.Add(self.workspaceLabel, 0, wx.ALIGN_CENTER)
        hSizer4.Add(self.workspace, 0, wx.ALIGN_CENTER)
        self.editObject.append(self.workspace)

        self.phoneLabel = wx.StaticText(self, label=u'联系电话：', size = (100, -1))
        self.phone = wx.TextCtrl(self, size=(300, -1), style = wx.TE_CENTER)
        self.phone.SetFont(editFont)
        hSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        hSizer5.Add(self.phoneLabel, 0, wx.ALIGN_CENTER)
        hSizer5.Add(self.phone, 0, wx.ALIGN_CENTER)
        self.editObject.append(self.phone)

        # self.expertNominationLabel = wx.StaticText(self, label=u'专家提名：', size=(100, -1))
        # self.expertNomination = wx.TextCtrl(self, size=(300, 240), style=wx.TE_MULTILINE)
        # self.expertNomination.SetFont(editFont)
        # self.expertNominationLabel.Disable()
        # self.expertNomination.Disable()
        # hSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        # hSizer6.Add(self.expertNominationLabel, 0, wx.ALIGN_CENTER)
        # hSizer6.Add(self.expertNomination, 0, wx.ALIGN_CENTER)
        # self.editObject.append(self.expertNomination)
        #
        # self.extraInstruct = wx.StaticText(self, label=u'          （至少给出三位提名专家，包括专家姓名、工作单位、研究领域。）')
        # self.extraInstruct.Disable()
        # tmpHSizer = wx.BoxSizer(wx.HORIZONTAL)
        # tmpHSizer.Add(self.extraInstruct, 0, wx.ALIGN_CENTER)

        self.confirmButton = wx.Button(self, label=u'保存')
        self.editButton = wx.Button(self, label=u'编辑')
        self.confirmButton.SetFont(editFont)
        self.editButton.SetFont(editFont)
        self.Bind(wx.EVT_BUTTON, self.OnConfirm, self.confirmButton)
        self.Bind(wx.EVT_BUTTON, self.OnEdit, self.editButton)
        hSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        hSizer7.Add(self.confirmButton, 0, wx.ALIGN_CENTER)
        hSizer7.Add(wx.StaticText(self,size = (100, -1)), 0, wx.ALIGN_CENTER)
        hSizer7.Add(self.editButton, 0, wx.ALIGN_CENTER)

        self.vSizer.Add((0, 0), 1, wx.ALIGN_CENTER)
        self.vSizer.Add(self.title, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(self.typeInstruct, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(hSizer0, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(hSizer1, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(hSizer2, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(hSizer3, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(hSizer4, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(hSizer5, 1, wx.ALIGN_CENTER)
        # self.vSizer.Add(hSizer6, 3, wx.ALIGN_CENTER)
        # self.vSizer.Add(tmpHSizer, 1, wx.ALIGN_CENTER)
        self.vSizer.Add(hSizer7, 3, wx.ALIGN_CENTER)

        self.SetSizerAndFit(self.vSizer)

    def getTabName(self):
        return self.tabName

    def OnRadioGroup(self, event):
        rb = event.GetEventObject()
        self.type = rb.GetLabel()
        # print self.type
        # if self.type == u'专家提名':
        #     self.expertNominationLabel.Enable()
        #     self.expertNomination.Enable()
        #     self.extraInstruct.Enable()
        # else:
        #     self.expertNominationLabel.Disable()
        #     self.expertNomination.Clear()
        #     self.expertNomination.Disable()
        #     self.extraInstruct.Disable()

    def OnConfirm(self, event):
        # if self.type == u'专家提名':
        #     self.radioButton1.Label = u'专家提名'
        #     self.radioButton1.SetFocus()
        # self.radioButton2.Hide()
        isEditAll = reduce(lambda x, y: x and y, map(lambda x: x.GetValue().strip() != '', self.editObject[2:]))
        if isEditAll == False:
            dlg = wx.MessageDialog(self, u'请确保所有信息均填写！', u'提示', wx.OK)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()
            return

        map(lambda x: x.Disable(), self.editObject)
        self.isConfirm = True
        JsonIO.isConfirm[0] = self.isConfirm
        JsonIO.cover["applicant"] = self.applicant.GetValue()
        JsonIO.cover["project_name"] = self.projectName.GetValue()
        JsonIO.cover["application_field"] = self.field.GetValue()
        JsonIO.cover["working_dep"] = self.workspace.GetValue()
        JsonIO.cover["telephone"] = self.phone.GetValue()

        if self.type == u'单位推荐':
            JsonIO.cover["type"] = u'单位推荐'
            if JsonIO.isConfirm[10] == False:
                JsonIO.isConfirm[10] = True
            # JsonIO.cover_dep_recommend["type"] = u'单位推荐'
            # JsonIO.cover_dep_recommend["applicant"] = self.applicant.GetValue()
            # JsonIO.cover_dep_recommend["project_name"] = self.projectName.GetValue()
            # JsonIO.cover_dep_recommend["application_field"] = self.field.GetValue()
            # JsonIO.cover_dep_recommend["working_dep"] = self.workspace.GetValue()
            # JsonIO.cover_dep_recommend["telephone"] = self.phone.GetValue()
        else:
            JsonIO.cover["type"] = u'专家提名'
            # JsonIO.cover_expert_nomination["type"] = u'专家提名'
            # JsonIO.cover_expert_nomination["applicant"] = self.applicant.GetValue()
            # JsonIO.cover_expert_nomination["project_name"] = self.projectName.GetValue()
            # JsonIO.cover_expert_nomination["application_field"] = self.field.GetValue()
            # JsonIO.cover_expert_nomination["working_dep"] = self.workspace.GetValue()
            # JsonIO.cover_expert_nomination["telephone"] = self.phone.GetValue()
            # JsonIO.cover_expert_nomination["expert"] = self.expertNomination.GetValue()

    def OnEdit(self, event):
        # self.radioButton1.Label = u'单位推荐'
        # self.radioButton2.Label = u'专家提名'
        # self.radioButton2.Show()
        # if self.type == u'专家提名':
        #     self.radioButton2.SetFocus()
        map(lambda x: x.Enable(), self.editObject)
        self.isConfirm = False
        JsonIO.isConfirm[0] = self.isConfirm
        # if self.type == u'专家提名':
        #     pass
        # else:
        #     self.expertNomination.Disable()
        #
        # JsonIO.cover_dep_recommend["type"] = ''
        # JsonIO.cover_dep_recommend["applicant"] = ''
        # JsonIO.cover_dep_recommend["project_name"] = ''
        # JsonIO.cover_dep_recommend["application_field"] = ''
        # JsonIO.cover_dep_recommend["working_dep"] = ''s
        # JsonIO.cover_dep_recommend["telephone"] = ''
        #
        # JsonIO.cover_expert_nomination["type"] = ''
        # JsonIO.cover_expert_nomination["applicant"] = ''
        # JsonIO.cover_expert_nomination["project_name"] = ''
        # JsonIO.cover_expert_nomination["application_field"] = ''
        # JsonIO.cover_expert_nomination["working_dep"] = ''
        # JsonIO.cover_expert_nomination["telephone"] = ''
        # JsonIO.cover_expert_nomination["expert"] = []
