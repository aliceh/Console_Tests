from selenium import *
import unittest, time, re
from lib_euca_ui_test import *


class testcase_ip(lib_euca_ui_test):


    def allocate_ip(self):
        print "=== runTest: allocate_ip ==="
        self.test_ui_login()
        self.test_add_tag_to_volume(tag="test-tag",key="test-key")
        self.test_ui_logout()

    def release_ip(self):
        print "=== runTest: release the first IP to cloud ==="
        self.test_ui_login()
        self.test_release_ip()
        self.test_ui_logout()

    def churn_ip(self):

        for i in range(4):

            print "=== runTest: create IP and release it to cloud ==="
            self.test_ui_login()
            self.test_allocate_ip()
            self.test_release_ip()
            self.test_ui_logout()

if __name__ == "__main__":
    unittest.main()
