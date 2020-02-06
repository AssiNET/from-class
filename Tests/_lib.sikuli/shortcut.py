from sikuli import *

class Shortcut(object):
    @classmethod
    def SelectAll(self):
        type('a', Key.CTRL)
        sleep(0.5)

    @classmethod
    def Copy(self):
        type('c', Key.CTRL)
        sleep(0.5)

    @classmethod
    def Paste(self):
        type('v', Key.CTRL)
        sleep(0.5)

    @classmethod
    def FocusAddressbar(self):
        type('d', Key.ALT)
        sleep(0.5)

    @classmethod
    def InvokeRunMenu(self):
        type('r', Key.WIN)
        sleep(0.5)