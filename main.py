import wx

class Frame(wx.Frame):

    def __init__(self, *args, **kw):
        super(Frame, self).__init__(*args, **kw)
        
        self.CreateStatusBar()
        self.SetStatusText("This is an example program...")
        self._makeMenuBar()

        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        vSizer = wx.BoxSizer(wx.VERTICAL)

        dialogButton = wx.Button(self, label="Dialog 1")
        dialogButton.Bind(event=wx.EVT_BUTTON, handler=None)

        vSizer.Add(wx.StaticText(self, label="Some static text"), flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        vSizer.Add(dialogButton, flag=wx.ALIGN_CENTER|wx.ALL, border=10)

        hSizer.Add(vSizer, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL)

        hSizer.SetMinSize(200, 100)
        self.SetSizerAndFit(hSizer)

    def _makeMenuBar(self):
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.onExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.onAbout, aboutItem)
    
    def onExit(self, event):
        self.Close(True)
    
    def onAbout(self, event):
        about = wx.adv.AboutDialogInfo()
        about.Name = "wxTextEntryDialog Example"
        about.Version = "0.1"
        about.Copyright = "(C) Emiliano Mesquita Drago"
        about.Description = "An example for wxTextEntryDialog"
        about.SetWebSite("https://github.com/mezka/wx-textentrydialog-example")
        wx.adv.AboutBox(about)

if __name__ == '__main__':
    app = wx.App()
    frm = Frame(None, title='wxTextEntryDialog Example')
    frm.Show()
    app.MainLoop()