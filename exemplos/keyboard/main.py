import wx

class Window(wx.Frame):
    """
    Build a hello world window in the center of the screen
    """
    def __init__(self,title):
        super().__init__(parent=None,title=title)
        self.panel = wx.Panel(self)

        sizer = wx.GridBagSizer(4,3)

        sizer.Add(wx.Button(self.panel,label="1"),pos=(0,0))
        sizer.Add(wx.Button(self.panel,label="2"),pos=(0,1))
        sizer.Add(wx.Button(self.panel,label="3"),pos=(0,2))

        sizer.Add(wx.Button(self.panel,label="4"),pos=(1,0))
        sizer.Add(wx.Button(self.panel,label="5"),pos=(1,1))
        sizer.Add(wx.Button(self.panel,label="6"),pos=(1,2))

        sizer.Add(wx.Button(self.panel,label="7"),pos=(2,0))
        sizer.Add(wx.Button(self.panel,label="8"),pos=(2,1))
        sizer.Add(wx.Button(self.panel,label="9"),pos=(2,2))

        sizer.Add(wx.Button(self.panel,label="0"),pos=(3,0))
        sizer.Add(wx.Button(self.panel,label="#"),pos=(3,2))

        self.panel.SetSizer(sizer)

        self.SetSize(260,400)
        self.Centre()
        self.Show()

app = wx.App()

window = Window("Hello, World!")

app.MainLoop()
