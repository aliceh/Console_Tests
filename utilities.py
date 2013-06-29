from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

def click_by_link_text(self, link_text):

        driver = self.driver
        wait_in_secs=self.wait_in_secs
        print "==============Click_link_by_text " + link_text + " START================="
        for i in range(wait_in_secs):
            try:
                print "Test: Trying to find link to text: " + link_text
                if self.is_element_present(By.LINK_TEXT, link_text): break

            except: pass
            print "Test: Found link to text: " + link_text
            time.sleep(1)
        else: self.fail("time out")
        print "Test: Found link to link text: " + link_text
        try:
            print "Test: Verifying link to link text: " + link_text
            self.assertTrue(self.is_element_present(By.LINK_TEXT, link_text))
        except AssertionError as e: self.verificationErrors.append(str(e))
        print "Test: Trying to click "+ link_text
        driver.find_element_by_link_text(link_text).click()
        print "Test: Clicked link text: "+ link_text
        print "==============Click_link_by_text  " + link_text + " DONE=================="

def click_element_by_id(self, element_id):

        driver = self.driver
        wait_in_secs=self.wait_in_secs
        print "==============click_element_by_id " + element_id + " START================="
        for i in range(wait_in_secs):
            try:
                print "Test: Trying to find element by id: " + element_id
                if self.is_element_present(By.ID, element_id): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        print "Test: Found element by id: " + element_id
        try:
            print "Test: Verifying element by id: " + element_id
            self.assertTrue(self.is_element_present(By.ID, element_id))
        except AssertionError as e: self.verificationErrors.append(str(e))
        print "Test: Trying to click element by id: " + element_id
        driver.find_element_by_id(element_id).click()
        print "Test: Clicked element by id: " + element_id
        print "==============click_element_by_id " + element_id + " DONE=================="

def click_element_by_css(self, css_path):

        driver = self.driver
        wait_in_secs=self.wait_in_secs
        #Example: css-path = .lnk-instance
        print "==============click_element_by_css " + css_path + " START================="
        for i in range(wait_in_secs):
            try:
                print "Test: Trying to find element by css: " + css_path
                if self.is_element_present(By.CSS_SELECTOR, css_path): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        print "Test: Found element by css: " + css_path
        try:
            print "Test: Verifying element by css: " + css_path
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, css_path))
        except AssertionError as e: self.verificationErrors.append(str(e))
        print "Test: Trying to click element by css: " + css_path
        driver.find_element_by_css_selector(css_path).click()
        print "Test: Clicked element by css: " + css_path
        print "==============click_element_by_css " + css_path + " DONE=================="

def set_keys_by_element_id(self,element_id, type_keys):

        driver = self.driver
        wait_in_secs=self.wait_in_secs
        print "==============find_el_by_id " +element_id + " and_send_keys " + type_keys + " START================="

        for i in range(wait_in_secs):
            try:
                print "Test: Verifying element present by id: " + element_id
                if self.is_element_present(By.ID, element_id): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id(element_id).clear()
        print "Test: Trying to click element by id: " + element_id + " and send keys " +type_keys
        driver.find_element_by_id(element_id).send_keys(type_keys)
        print "Test: Sent keys " + type_keys
        print "==============find_el_by_id " +element_id + " and_send_keys " + type_keys + " DONE=================="

def set_keys_by_css(self, element_css, text):

        driver = self.driver
        wait_in_secs=self.wait_in_secs
        print "==============find_el_by_css " +element_css+ " and_send_text " + text + " START================="

        for i in range(wait_in_secs):
            try:
                print "Test: Verifying element present by css: " + element_css
                if self.is_element_present(By.CSS_SELECTOR, element_css): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector (element_css).clear()
        print "Test: Trying to click element by css: " + element_css + " and send keys " +text
        driver.find_element_by_css_selector(element_css).send_keys(text)
        print "Test: Sent keys " + text
        print "==============find_el_by_id " +element_css + " and_send_keys " + text + " DONE=================="


def set_keys_by_xpath(self, element_xpath, text):
        driver = self.driver
        wait_in_secs=self.wait_in_secs

        for i in range(wait_in_secs):
            try:
                print "Test: Verifying element present by xpath: " + element_xpath
                if self.is_element_present(By.XPATH, element_xpath): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        try: self.assertTrue(self.is_element_present(By.XPATH, element_xpath))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath(element_xpath).clear()
        driver.find_element_by_xpath(element_xpath).send_keys(text)
        print "Test: Typed: "+text+ " in the xpath location " + element_xpath




def get_value_by_css(self, element_css, what_is_it):
        '''
        element_css is the css path to the element the value of which we are interested in
        what_is_it is a short description of the element for the log; i.e. number of running instances
        saves the value of the desired element into self.save_value

        '''
        driver = self.driver
        wait_in_secs=self.wait_in_secs

        print "==============copy_value_into_var "+ what_is_it+ " by_css " + element_css + " START================="

        for i in range(wait_in_secs):
            try:
                print "Test: Verifying element present by css: " + element_css
                if self.is_element_present(By.CSS_SELECTOR, element_css): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        print "Test: Assert element present by css: " + element_css
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, element_css))
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.save_value = driver.find_element_by_css_selector(element_css).text
        while self.save_value == "":
            self.save_value = driver.find_element_by_css_selector(element_css).text
        print "Test: saved value for " + what_is_it + " " + self.save_value

        print "==============copy_value_into_var "+ what_is_it + " by_css " + element_css + " DONE================="



#def wait_for_visible_css(self,element_css):

