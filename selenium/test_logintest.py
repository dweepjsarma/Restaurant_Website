# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogintest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_logintest(self):
    self.driver.get("http://localhost:8081/website/backend/home.php")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.CSS_SELECTOR, ".icons").click()
    self.driver.find_element(By.ID, "user-btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".delete-btn").click()
    assert self.driver.switch_to.alert.text == "logout from this website?"
    self.driver.switch_to.alert.dismiss()
    self.driver.find_element(By.LINK_TEXT, "login").click()
    self.driver.find_element(By.NAME, "email").send_keys("sarmadweepjyoti@gmail.com")
    self.driver.find_element(By.NAME, "pass").send_keys("7086642252")
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.CSS_SELECTOR, "form").click()
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-container").click()
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.ID, "user-btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".profile").click()
    self.driver.find_element(By.CSS_SELECTOR, ".flex > .btn").click()
  
