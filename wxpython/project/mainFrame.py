# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/19 18:19'


''' 主窗口，包含标签页和菜单
'''

import os
import wx
from panels import DeclarationInfo, ApplicantInfo, StudyResults, Studying, StudyExperience, WorkExperience, DefenseProject, Management, TechnologyAwards, Parent, ExpertNomination
from extra import JsonIO, DoExport


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(-1, -1))

        self.icon = wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        screenSize = wx.DisplaySize()
        x = screenSize[0] * 0.9
        y = screenSize[1] * 0.9

        self.SetMaxSize((x, y))
        self.SetMinSize((x, y))
        # self.ShowFullScreen(True, wx.FULLSCREEN_NOMENUBAR)

        # 创建位于窗口底部的状态栏
        # self.CreateStatusBar()

        self.panel = wx.Panel(self, size=(1920, 1080))

        self.gSizer = wx.BoxSizer(wx.VERTICAL)

        img = wx.Image('bglogo.jpg', wx.BITMAP_TYPE_ANY)
        sz = self.GetClientSize()
        img = img.Scale(x, y / 10)

        sb1 = wx.StaticBitmap(self.panel, -1, wx.Bitmap(img), style=wx.EXPAND)
        self.gSizer.Add(sb1, 1, wx.EXPAND)

        # 首页背景图片
        self.homeImg = wx.Image('homeBackground.jpg', wx.BITMAP_TYPE_ANY).Scale(x, y).ConvertToBitmap()
        self.homeBackground = wx.StaticBitmap(self.panel, -1, self.homeImg, style=wx.EXPAND)


        # 布置标签面板
        notebook = wx.Notebook(self.panel, size=(x, y))
        declaration_panel = DeclarationInfo.TabPanel(notebook)
        applicant_panel = ApplicantInfo.TabPanel(notebook)
        studyResults_panel = StudyResults.TabPanel(notebook)
        studying_panel = Studying.TabPanel(notebook)
        studyExperience_panel = StudyExperience.TabPanel(notebook)
        workExperience_panel = WorkExperience.TabPanel(notebook)
        defenseProject_panel = DefenseProject.TabPanel(notebook)
        management_panel = Management.TabPanel(notebook)
        technologyAwards_panel = TechnologyAwards.TabPanel(notebook)
        parent_panel = Parent.TabPanel(notebook)
        expertNomination_panel = ExpertNomination.TabPanel(notebook)

        notebook.AddPage(declaration_panel, declaration_panel.getTabName())
        notebook.AddPage(applicant_panel, applicant_panel.getTabName())
        notebook.AddPage(studyResults_panel, studyResults_panel.getTabName())
        notebook.AddPage(studying_panel, studying_panel.getTabName())
        notebook.AddPage(studyExperience_panel, studyExperience_panel.getTabName())
        notebook.AddPage(workExperience_panel, workExperience_panel.getTabName())
        notebook.AddPage(defenseProject_panel, defenseProject_panel.getTabName())
        notebook.AddPage(management_panel, management_panel.getTabName())
        notebook.AddPage(technologyAwards_panel, technologyAwards_panel.getTabName())
        notebook.AddPage(parent_panel, parent_panel.getTabName())
        notebook.AddPage(expertNomination_panel, expertNomination_panel.getTabName())

        self.gSizer.Add(notebook, 10, wx.EXPAND)

        self.panel.SetSizerAndFit(self.gSizer)
        self.Fit()

        # self.panel.Hide()

        # # 设置菜单
        # fileMenu = wx.Menu()
        # exportJson = fileMenu.Append(wx.ID_NEW, u'导出Json文件', u'导出填写的项目申报书对应的Json文件')
        # exportWord = fileMenu.Append(wx.ID_OPEN, u'导出word', u'导出一个项目申报书的文档')
        # printBook = fileMenu.Append(wx.ID_PRINT, u'打印', u'打印项目申报书')
        # fileMenu.AppendSeparator()
        # menuExit = fileMenu.Append(wx.ID_EXIT, u'退出', u'终止应用程序')
        #
        # # 创建菜单栏
        # menuBar = wx.MenuBar()
        # menuBar.Append(fileMenu, u'文件')
        # self.SetMenuBar(menuBar)
        #
        # self.Bind(wx.EVT_MENU, self.OnExportJson, exportJson)
        # self.Bind(wx.EVT_MENU, self.OnExportWord, exportWord)
        # self.Bind(wx.EVT_MENU, self.OnPrintBook, printBook)
        # self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # 创建工具栏
        self.createToolBar()

    def createToolBar(self):  # 1创建工具栏
        toolbar = self.CreateToolBar()
        for each in self.toolbarData():
            self.createSimpleTool(toolbar, *each)

        toolbar.Realize()  # 2 显现工具栏

    def createSimpleTool(self, toolbar, label, filename, help, handler):  # 3 创建常规工具
        if not label:
            toolbar.AddSeparator()
            return
        img = wx.Image(filename, wx.BITMAP_TYPE_PNG)
        imgSize = img.GetSize()
        bmp = img.Scale(imgSize.x / 5, imgSize.y / 5).ConvertToBitmap()
        # tool = toolbar.AddTool(-1, bitmap=bmp, label=label)
        tool = toolbar.AddSimpleTool(-1, bmp, label, help)
        self.Bind(wx.EVT_MENU, handler, tool)

    def toolbarData(self):
        return (('', '', '', ''), ('', '', '', ''),
                (u"填报信息", "edit.png", u"填报信息", self.OnInfoEdit),
                (u"导出Json数据文件", "export.png", u"导出Json数据文件", self.OnExportJson),
                (u"导出Word文件供打印", "word.png", u"导出Word文件供打印", self.OnExportWord),
                ('', '', '', ''),
                (u"帮助", "help.png", u"帮助", self.OnHelp),
                ( u"关于", "about.png", u"关于", self.OnAbout),
                ('', '', '', ''), ('', '', '', ''))


    def OnInfoEdit(self, event):
        self.homeBackground.Hide()

    def OnExportJson(self, event):
        # print JsonIO.isConfirm
        isFinish = DoExport.exportJson()
        if isFinish:
            path = os.getcwd()
            # exportFilePath = '\\'.join(path.split('\\')[:-1])
            instruct = u'导出Json文件成功！文件在“%s”目录下！' % (path + '\\ExportData')
            dlg = wx.MessageDialog(self, instruct, u'提示', wx.OK)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()
        else:
            dlg = wx.MessageDialog(self, u'请检查是否所有的信息录入均保存！', u'提示', wx.OK)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()

    def OnExportWord(self, event):
        isFinish = DoExport.exportWord()
        if isFinish:
            path = os.getcwd()
            # exportFilePath = '\\'.join(path.split('\\')[:-1])
            instruct = u'导出Word成功！文件在“%s”目录下！' % (path + '\\ExportWord')
            dlg = wx.MessageDialog(self, instruct, u'提示', wx.OK)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()
        else:
            dlg = wx.MessageDialog(self, u'请检查是否所有的信息录入均确定！', u'提示', wx.OK)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()

    def OnHelp(self, event):
        try:
            os.system(os.getcwd() + '\\help.doc')
        except:
            dlg = wx.MessageDialog(self, u'用户手册已不存在！', u'错误', wx.OK)
            dlg.SetOKLabel(u'确定')
            dlg.ShowModal()
            dlg.Destroy()


    def OnAbout(self, event):
        instruct = u'国防科技卓越青年人才基金项目申报系统\n'
        instruct += u'版本：2017.05.30\n'
        instruct += u'(C) 2017中央军委科学技术委员会\n'
        instruct += u'技术支持电话：12345678'
        dlg = wx.MessageDialog(self, instruct, u'关于', wx.OK)
        dlg.SetOKLabel(u'确定')
        dlg.ShowModal()
        dlg.Destroy()

    def OnPrintBook(self, event):
        print 'lcx'

    def OnExit(self, event):
        self.Close(True)


