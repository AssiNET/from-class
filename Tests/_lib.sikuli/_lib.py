from sikuli import *
from _uimap import *
from shortcut import *

import urllib
import os
import shutil

class Browser(object):
    @classmethod
    def Start(self, url):
        type('r', Key.WIN)
        sleep(0.5)
        type("chrome " + url)
        sleep(0.5)
        type(Key.ENTER)
        wait(Browser_UI.button_Refresh, 5)

    @classmethod
    def Maximize(self):
        type(Key.SPACE, Key.ALT)
        sleep(0.5)
        type('x')

    @classmethod
    def OpenNewTab(self):
        type('t', Key.CTRL)

    @classmethod
    def OpenURL(self, url):
        Shortcut.FocusAddressbar()
        sleep(0.5)
        type(url)
        sleep(0.5)
        type(Key.ENTER)
        sleep(0.5)

class UIActions(object):
    @classmethod
    def MaximizeWindow(self):
        type(Key.SPACE, Key.ALT)
        sleep(0.5)
        type('x')

    @classmethod
    def CopyAllToClipBoard():
        Shortcut.SelectAll()
        sleep(1)
        Shortcut.Copy()

    @classmethod
    def GetClipboard():
        return Env.getClipboard()

    @classmethod
    def ClearClipboard():
        from java.awt.datatransfer import StringSelection
        from java.awt import Toolkit
        toolkit = Toolkit.getDefaultToolkit()
        clipboard = toolkit.getSystemClipboard()
        clipboard.setContents(StringSelection(""), None)

class Network(object):
    @classmethod
    def DownloadFile(self, download_url, destination):
        try:
            if os.path.exists(destination):
                os.remove(destination)

            urllib.urlretrieve(download_url, destination)
        except Exception as ex:
            print("Download failed!")
            print("Exception: " + str(ex))


