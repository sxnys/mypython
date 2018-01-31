# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/19 15:57'


import wx
import os

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname = ''
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()      # 创建位于窗口底部的状态栏

        # 设置菜单
        fileMenu = wx.Menu()
        menuOpen = fileMenu.Append(wx.ID_OPEN, u'打开', u'打开一个文件')
        menuAbout = fileMenu.Append(wx.ID_ABORT, u'关于', u'关于程序的信息')
        fileMenu.AppendSeparator()
        menuExit = fileMenu.Append(wx.ID_EXIT, u'退出', u'终止应用程序')

        # 创建菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, u'文件')
        self.SetMenuBar(menuBar)

        # 设置事件处理
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # 设置sizer
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &" + str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.SHAPED)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.GROW)

        # 位图按钮
        image = wx.Image('add.jpg', wx.BITMAP_TYPE_JPEG)
        image = image.Scale(image.GetWidth() / 20, image.GetHeight() / 20)
        bitmap = image.ConvertToBitmap()
        bitmapButton = wx.BitmapButton(self, -1, bitmap, style=wx.BU_AUTODRAW)
        self.sizer.Add(bitmapButton, 1, wx.ALIGN_CENTER)

        # 激活sizer
        self.SetSizer(self.sizer)
        # self.SetAutoLayout(True)
        # self.sizer.Fit(self)
        self.Show(True)

    def OnOpen(self, e):
        """ open a file. """
        # wx.FileDialog语法：(self, parent, message, defaultDir, defaultFile,
        #                    wildcard, style, pos)
        dlg = wx.FileDialog(self, u'选择一个文件', self.dirname, '', '*.*',
                            wx.ID_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')  # 暂时只读
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, u'一个简单的编辑器', u'关于此程序', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        self.Close(True)

