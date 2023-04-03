import wx

class Window(wx.Frame):
    """
    Build a hello world window in the center of the screen
    """
    def __init__(self,title):
        super().__init__(parent=None,title=title)
        self.panel = wx.Panel(self)

        sizer = wx.GridBagSizer(4,3)

        sizer.Add(wx.StaticText(self.panel,label="My little keypad"),pos = (0,1),flag=wx.ALIGN_CENTRE)

        sizer.Add(wx.Button(self.panel,label="1"),pos=(1,0),flag=wx.EXPAND)
        sizer.Add(wx.Button(self.panel,label="2"),pos=(1,1),flag=wx.EXPAND)
        sizer.Add(wx.Button(self.panel,label="3"),pos=(1,2),flag=wx.EXPAND)

        sizer.Add(wx.Button(self.panel,label="4"),pos=(2,0),flag=wx.EXPAND)
        sizer.Add(wx.Button(self.panel,label="5"),pos=(2,1),flag=wx.EXPAND)
        sizer.Add(wx.Button(self.panel,label="6"),pos=(2,2),flag=wx.EXPAND)

        sizer.Add(wx.Button(self.panel,label="7"),pos=(3,0),flag=wx.EXPAND)
        sizer.Add(wx.Button(self.panel,label="8"),pos=(3,1),flag=wx.EXPAND)
        sizer.Add(wx.Button(self.panel,label="9"),pos=(3,2),flag=wx.EXPAND)

        sizer.Add(wx.Button(self.panel,label="0"),pos=(4,0),flag=wx.EXPAND)
        sizer.Add(wx.Button(self.panel,label="#"),pos=(4,2),flag=wx.EXPAND)

        sizer.AddGrowableRow(1)
        sizer.AddGrowableRow(2)
        sizer.AddGrowableRow(3)
        sizer.AddGrowableRow(4)

        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
        sizer.AddGrowableCol(2)

        self.panel.SetSizer(sizer)

        self.Centre()
        self.Show()

app = wx.App()

window = Window("Hello, World!")

app.MainLoop()
