from selenium import *
import unittest, time, re
from lib_euca_ui_test import *


class testcase_comprehensive(lib_euca_ui_test):

    def comprehensive(self):
        print "=== runTest: comprehensive ==="
        self.test_ui_login()
        self.test_change_password(new_password = "testpass")
        self.test_ui_logout()
        self.test_ui_login()
        self.test_change_password(new_password = "mypassword1")
        self.test_ui_logout()



if __name__ == "__main__":
    unittest.main()
