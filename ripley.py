#!/usr/bin/python

# ripley.py - shows python commands, comentary and results

# warning, this app stuffs things onto your clipboard.

# filename = "ripley.txt"
filename = "b3.txt"

##==============================================================================
import wx
import wx.lib.sized_controls as sc
import subprocess

def main():
    app = wx.App()

    winsize=(500,300)
    frame = sc.SizedFrame(None, title='Ripley',  pos=(1,1), size=winsize)
    panel = frame.GetContentsPane()

    cr = CodeDesc()
    return

    cr.addWidgets(panel, frame)
    cr.refresh()

    frame.Show()

    app.MainLoop()

def parse(filename):

    """
# for testing UI
    mocfile = [
    {'code':'"hello world!"', 'desc':'evaluates the expression, displays the result.'},
    {'code':'2+3', 'desc':'evalutates...\n\ndisplays.'},
    {'code':'2/3', 'desc':'int division is the default in 2.x.'},
    ]
    return mocfile
    """

    state=0
    l=[]
    pre,post=[],[]
    for line in open(filename):
        line=line.strip('\n')
        print(line)
        if state==0 and line == "Programing:": state=1
        elif state == 1:
            pre.append(line)
            if line.startswith('>>>'):
# save this one
                l.append([line[4:],'\n'.join(pre)])

# setup for next
                post=pre
                pre=[]

    l.append([line[4:],'\n'.join(pre)])

    return l

class CodeDesc:

    def __init__(self):
        self.cmds = parse(filename)
        for c in self.cmds: print(c)
        self.cmdpos = 0
        self.clip()

    def refresh(self):
        self.txt1.SetValue(self.cmds[self.cmdpos][0])
        self.txt2.SetValue(self.cmds[self.cmdpos][1])

    def addWidgets(self, parent, topwindow):
        panel = sc.SizedPanel(parent)
        panel.SetSizerType('horizontal')
        panel.SetSizerProps(expand=True)
        self.panel = panel

        txt1 = wx.TextCtrl(panel)
        txt1.SetSizerProps(proportion=50, expand=True)
        self.txt1 = txt1

        # btn1 = wx.Button(panel, label='Clip')
        # btn1.Bind(wx.EVT_BUTTON, self.OnClipClicked)
        # btn1.SetSizerProps(proportion=5, expand=True)

        btn2 = wx.Button(panel, label='Prev')
        btn2.Bind(wx.EVT_BUTTON, self.OnPrevClicked)
        btn2.SetSizerProps(proportion=5, expand=True)

        btn3 = wx.Button(panel, label='Next')
        btn3.Bind(wx.EVT_BUTTON, self.OnNextClicked)
        btn3.SetSizerProps(proportion=5, expand=True)

        panel2 = sc.SizedPanel(parent)
        panel2.SetSizerType('vertical')
        panel2.SetSizerProps(expand=True, proportion=2)
        self.panel2 = panel2

        txt2 = wx.TextCtrl(panel2, style=wx.TE_READONLY|wx.TE_MULTILINE)
        txt2.SetSizerProps(proportion=1, expand=True)
        self.txt2 = txt2


    def clip(self):
         p = subprocess.Popen('xclip', stdin=subprocess.PIPE)
         p.communicate(self.cmds[self.cmdpos][0])
         """
         this don't work, sorry windows.
        # gconftool-2 -t str -s /apps/gnome-terminal/keybindings/paste "<Control>v"
        text=self.cmds[self.cmdpos][0]
        wx.Clipboard.UsePrimarySelection(wx.Clipboard(), primary = True)
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData( wx.TextDataObject(text) )
            wx.TheClipboard.Close()
         """

    # def OnClipClicked(self, event):
    #     self.clip()

    def OnNextClicked(self, event):
        if self.cmdpos<len(self.cmds)-1: self.cmdpos += 1
        self.clip()
        self.refresh()

    def OnPrevClicked(self, event):
        if self.cmdpos: self.cmdpos -= 1
        self.clip()
        self.refresh()


if __name__ == '__main__':
    main()
