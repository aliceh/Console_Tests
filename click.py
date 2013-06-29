from selenium import *
import unittest, time, re
from lib_euca_ui_test import *


class testcase_click(lib_euca_ui_test):


    def click_link(self):
        print "=== runTest: Click Link ==="
        self.test_ui_login()
        self.click_by_link_text()
        self.test_ui_logout()


if __name__ == "__main__":
    unittest.main()
