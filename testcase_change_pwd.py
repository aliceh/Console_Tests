from selenium import *
import unittest, time, re
from lib_euca_ui_test import *


class testcase_change_pwd(lib_euca_ui_test):

    def change_pwd(self):
        print "=== runTest: change_pwd ==="
        self.test_ui_login()
        self.test_change_password(new_password="pwd1")
        self.test_ui_logout()


if __name__ == "__main__":
    unittest.main()
