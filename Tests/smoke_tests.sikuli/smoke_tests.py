import unittest
from _lib import *
import HtmlXmlTestRunner_pkg.HtmlXmlTestRunner as HtmlXmlTestRunner

import urllib
import os

destination = 'C:\mini-framework\downloads\python-logo.jpg'

class SmokeTests(unittest.TestCase):

    def test_100_Start_Browser(self):
        print("XXXXXXXXX Test started XXXXXXXXX")
        Browser.Start("https://www.python.org")
        sleep(1)
        Browser.Maximize()

    def test_200_Download_Logo(self):
        rightClick(Website_Python_UI.logo_icon)
        sleep(0.5)
        click(Website_Python_UI.context_button_Copy_Adress)
        logo_url = Env.getClipboard() # https://www.python.org/static/img/python-logo@2x.png
        print logo_url
        Network.DownloadFile(logo_url, destination)

    def test_300_Validate_Image(self):
        assert os.path.exists(destination) # check first that file exists
        Shortcut.SelectAll
        Shortcut.InvokeRunMenu()
        type(destination)
        type(Key.ENTER)
        sleep(1)
        UIActions.MaximizeWindow()
        assert exists(OS_UI.image_logo_icon, 5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
    
    ## Use it to add manually test cases - handy when debugging a specific part of the set
    #suite = unittest.TestSuite()
    #suite.addTest(SmokeTests('test_100_Start_Browser'))
    #suite.addTest(SmokeTests('FREE_SLOT'))

    outfile = open("Report.html", "w")
    runner = HtmlXmlTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report', description="Description")
    runner.run(suite)
    outfile.close()

