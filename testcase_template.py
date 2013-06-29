from selenium import *
import unittest, time, re
from lib_euca_ui_test import *


class testcase_template(lib_euca_ui_test):

    def testcase1(self):    #replace testcase1 with the name of your first testcase
        print "=== runTest: testcase1 ==="
        self.test_ui_login()
                             #insert one or more  testcases from lib_euca_ui_test.py
        self.test_ui_logout()

    def testcase2(self):    #replace testcase2 with the name of your second testcase
        print "=== runTest: testcase2 ==="
        self.test_ui_login()
                            #insert one or more  testcases from lib_euca_ui_test.py
        self.test_ui_logout()

if __name__ == "__main__":
    unittest.main()
