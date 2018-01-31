# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/19 18:36'


''' 申请人基本信息面板
'''

import wx
from extra import JsonIO


class TabPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.tabName = u'申请人基本信息'

        self.editObject = list()
        self.isConfirm = False

        self.vSizer = wx.BoxSizer(wx.VERTICAL)

        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        titleFont = wx.Font(24, wx.MODERN, wx.NORMAL, wx.BOLD)
        instructFont = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
        guideFont = wx.Font(18, wx.MODERN, wx.NORMAL, wx.BOLD)
        editFont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.SetFont(font)

        self.title = wx.StaticText(self, label=self.tabName)
        self.title.SetFont(titleFont)

        self.instruct = wx.StaticText(self, label=u'保证所填写的信息均真实有效，无任何虚假信息。保证完全清楚本声明的法律后果，如有不实，需要承担相应的法律责任。')
        self.instruct.SetFont(instructFont)

        '''申请人情况
        '''
        self.guide1 = wx.StaticText(self, label=u'申请人情况')
        self.guide1.SetFont(guideFont)
        self.separator1 = wx.StaticText(self, label='_' * 30)

        self.grid = wx.GridBagSizer(hgap=5, vgap=5)
        self.grid.Add(self.guide1, pos=(0, 0), span=(1, 10), flag=wx.EXPAND)
        self.grid.Add(self.separator1, pos=(1, 0), span=(1, 2), flag=wx.EXPAND)

        # 第一列
        self.nameLabel = wx.StaticText(self, label=u'姓名：')
        self.name = wx.TextCtrl(self, size=(200, -1), style = wx.TE_CENTER)
        self.name.SetFont(editFont)
        self.grid.Add(self.nameLabel, pos=(3, 0))
        self.grid.Add(self.name, pos=(3, 1), span=(1, 2), flag=wx.EXPAND)
        self.editObject.append(self.name)

        self.grid.Add((50, -1), pos=(3,3))

        self.genderLabel = wx.StaticText(self, label=u'性别：')
        self.gender = u'男'
        self.radioButton1 = wx.RadioButton(self, 1, label=u'男', style=wx.RB_GROUP)
        self.radioButton2 = wx.RadioButton(self, 1, label=u'女')
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioGroup)
        self.grid.Add(self.genderLabel, pos=(3, 4))
        self.grid.Add(self.radioButton1, pos=(3, 5))
        self.grid.Add(self.radioButton2, pos=(3, 6))
        self.editObject.append(self.radioButton1)
        self.editObject.append(self.radioButton2)

        self.grid.Add((50, -1), pos=(3, 7))

        self.birthLabel = wx.StaticText(self, label=u'出生年月：')
        self.yearList = map(lambda x: str(x), reversed(xrange(1960, 2018)))
        self.monthList = map(lambda x: str(x), xrange(1, 13))
        self.birthYear = wx.ComboBox(self, choices= self.yearList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.birthYear.SetFont(editFont)
        self.yearLabel = wx.StaticText(self, label=u' 年 ')
        self.birthMonth = wx.ComboBox(self, choices= self.monthList, style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.birthMonth.SetFont(editFont)
        self.monthLabel = wx.StaticText(self, label=u' 月')
        self.hSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.hSizer.Add(self.birthYear, 0, wx.ALIGN_CENTER)
        self.hSizer.Add(self.yearLabel, 0, wx.ALIGN_CENTER)
        self.hSizer.Add(self.birthMonth, 0, wx.ALIGN_CENTER)
        self.hSizer.Add(self.monthLabel, 0, wx.ALIGN_CENTER)
        self.grid.Add(self.birthLabel, pos=(3, 8))
        self.grid.Add(self.hSizer, pos=(3, 9), span=(1, 3), flag=wx.EXPAND)
        self.editObject.append(self.birthYear)
        self.editObject.append(self.birthMonth)

        # 第二列
        self.levelLabel = wx.StaticText(self, label=u'学位：')
        self.level = wx.TextCtrl(self, style=wx.TE_CENTER)
        self.level.SetFont(editFont)
        self.grid.Add(self.levelLabel, pos=(4, 0))
        self.grid.Add(self.level, pos=(4, 1), span=(1, 2), flag=wx.EXPAND)
        self.editObject.append(self.level)

        self.workNameLabel = wx.StaticText(self, label=u'职称：')
        self.workName = wx.TextCtrl(self, size=(200, -1), style=wx.TE_CENTER)
        self.workName.SetFont(editFont)
        self.grid.Add(self.workNameLabel, pos=(4, 4))
        self.grid.Add(self.workName, pos=(4, 5), span=(1, 2), flag=wx.EXPAND)
        self.editObject.append(self.workName)

        self.workLabel = wx.StaticText(self, label=u'单位职务：')
        self.work = wx.TextCtrl(self, size=(200, -1), style=wx.TE_CENTER)
        self.work.SetFont(editFont)
        self.grid.Add(self.workLabel, pos=(4, 8))
        self.grid.Add(self.work, pos=(4, 9), span=(1, 2), flag=wx.EXPAND)
        self.editObject.append(self.work)

        # 第三列
        self.directorLabel = wx.StaticText(self, label=u'主要研究方向：')
        self.director = wx.TextCtrl(self, style=wx.TE_CENTER)
        self.director.SetFont(editFont)
        self.grid.Add(self.directorLabel, pos=(5, 0))
        self.grid.Add(self.director, pos=(5, 1), span=(1, 10), flag=wx.EXPAND)
        self.editObject.append(self.director)

        # 第四列
        self.IDType = [u'身份证', u'军官证']
        self.IDLabel = wx.StaticText(self, label=u'身份证件名称：')
        # self.ID = wx.TextCtrl(self, style=wx.TE_CENTER)
        self.ID = wx.ComboBox(self, choices=self.IDType, style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.ID.SetFont(editFont)
        self.grid.Add(self.IDLabel, pos=(6, 0))
        self.grid.Add(self.ID, pos=(6, 1), span=(1, 2), flag=wx.EXPAND)
        self.editObject.append(self.ID)

        self.IDNumberLabel = wx.StaticText(self, label=u'证件编号：')
        self.IDNumber = wx.TextCtrl(self, style=wx.TE_CENTER)
        self.IDNumber.SetFont(editFont)
        self.grid.Add(self.IDNumberLabel, pos=(6, 4))
        self.grid.Add(self.IDNumber, pos=(6, 5), span=(1, 6), flag=wx.EXPAND)
        self.editObject.append(self.IDNumber)

        # 第五列
        self.telephoneLabel = wx.StaticText(self, label=u'办公电话：')
        self.telephone = wx.TextCtrl(self, style=wx.TE_CENTER)
        self.telephone.SetFont(editFont)
        self.grid.Add(self.telephoneLabel, pos=(7, 0))
        self.grid.Add(self.telephone, pos=(7, 1), span=(1, 2), flag=wx.EXPAND)
        self.editObject.append(self.telephone)

        self.phoneLabel = wx.StaticText(self, label=u'手机：')
        self.phone = wx.TextCtrl(self, style=wx.TE_CENTER)
        self.phone.SetFont(editFont)
        self.grid.Add(self.phoneLabel, pos=(7, 4))
        self.grid.Add(self.phone, pos=(7, 5), span=(1, 2), flag=wx.EXPAND)
        self.editObject.append(self.phone)

        self.emailLabel = wx.StaticText(self, label='E-mail：')
        self.email = wx.TextCtrl(self, style=wx.TE_CENTER)
        self.email.SetFont(editFont)
        self.grid.Add(self.emailLabel, pos=(7, 8))
        self.grid.Add(self.email, pos=(7, 9), span=(1, 2), flag=wx.EXPAND)
        self.editObject.append(self.email)

        '''申请单位情况
        '''
        self.guide2 = wx.StaticText(self, label=u'申请单位情况')
        self.guide2.SetFont(guideFont)
        self.separator2 = wx.StaticText(self, label='_' * 30)

        self.grid.Add(self.guide2, pos=(9, 0), span=(1, 10), flag=wx.EXPAND)
        self.grid.Add(self.separator2, pos=(10, 0), span=(1, 2), flag=wx.EXPAND)

        self.workspaceLabel = wx.StaticText(self, label=u'单位名称：')
        self.workspace = wx.TextCtrl(self, size=(200, -1), style=wx.TE_CENTER)
        self.workspace.SetFont(editFont)
        self.grid.Add(self.workspaceLabel, pos=(12, 0))
        self.grid.Add(self.workspace, pos=(12, 1), span=(1, 6), flag=wx.EXPAND)
        self.editObject.append(self.workspace)

        self.contactLabel = wx.StaticText(self, label=u'联系人（手机）：')
        self.contact = wx.TextCtrl(self, size=(200, -1), style=wx.TE_CENTER)
        self.contact.SetFont(editFont)
        self.grid.Add(self.contactLabel, pos=(12, 8))
        self.grid.Add(self.contact, pos=(12, 9), span=(1, 2), flag=wx.EXPAND)
        self.editObject.append(self.contact)

        self.addressLabel = wx.StaticText(self, label=u'通信地址：')
        self.address = wx.TextCtrl(self, style=wx.TE_CENTER)
        self.address.SetFont(editFont)
        self.grid.Add(self.addressLabel, pos=(13, 0))
        self.grid.Add(self.address, pos=(13, 1), span=(1, 11), flag=wx.EXPAND)
        self.editObject.append(self.address)

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

    def OnRadioGroup(self, event):
        rb = event.GetEventObject()
        self.gender = rb.GetLabel()
        # print self.type

    def OnConfirm(self, event):
        # if self.gender == u'女':
        #     self.radioButton1.Label = u'女'
        #     self.radioButton1.SetFocus()
        # self.radioButton2.Hide()

        isEditAll = reduce(lambda x, y: x and y, map(lambda x: x.GetValue().strip() != '', self.editObject[3:]) )
        if isEditAll == False or self.editObject[0].GetValue().strip() == '':
            dlg = wx.MessageDialog(self, u'请确保所有信息均填写！', u'提示', wx.OK)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()
            return

        map(lambda x: x.Disable(), self.editObject)
        self.isConfirm = True
        JsonIO.isConfirm[1] = self.isConfirm

        JsonIO.personal_info['name'] = self.name.GetValue()
        JsonIO.personal_info['gender'] = self.gender
        JsonIO.personal_info['birthday'] = self.birthYear.GetValue() + u'年' + self.birthMonth.GetValue() + u'月'
        JsonIO.personal_info['bachelor'] = self.level.GetValue()
        JsonIO.personal_info['job'] = self.workName.GetValue()
        JsonIO.personal_info['dep_job'] = self.work.GetValue()
        JsonIO.personal_info['research'] = self.director.GetValue()
        JsonIO.personal_info['id_name'] = self.ID.GetValue()
        JsonIO.personal_info['id_num'] = self.IDNumber.GetValue()
        JsonIO.personal_info['office_phone'] = self.telephone.GetValue()
        JsonIO.personal_info['telephone'] = self.phone.GetValue()
        JsonIO.personal_info['email'] = self.email.GetValue()

        JsonIO.dep_info['dep_name'] = self.workspace.GetValue()
        JsonIO.dep_info['telephone'] = self.contact.GetValue()
        JsonIO.dep_info['address'] = self.address.GetValue()

    def OnEdit(self, event):
        # self.radioButton1.Label = u'男'
        # self.radioButton2.Label = u'女'
        # self.radioButton2.Show()
        # if self.gender == u'女':
        #     self.radioButton2.SetFocus()
        map(lambda x: x.Enable(True), self.editObject)
        self.isConfirm = False
        JsonIO.isConfirm[1] = self.isConfirm