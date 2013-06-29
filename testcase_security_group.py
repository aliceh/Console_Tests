from selenium import *
import unittest, time, re
from lib_euca_ui_test import *

class testcase_security_group(lib_euca_ui_test):

    def create_security_group(self):
        print "=== runTest: Create Security Group ==="
        self.test_ui_login()
        self.test_ui_create_security_group()
        self.test_ui_logout()

    def delete_security_group(self):
        print "=== runTest: Delete Security Group ==="
        self.test_ui_login()
        self.test_ui_delete_security_group()
        self.test_ui_logout()

    def create_s_group_churn(self):
        print "=== runTest: Create 100 Security Groups ==="
        self.test_ui_login()
        #i=0
        i=26
        while(i<100):
            name="group"+`i`
            self.test_ui_create_security_group(group_name=name)
            i+=1
        self.test_ui_logout()


if __name__ == "__main__":
    unittest.main()



