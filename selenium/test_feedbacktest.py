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

class TestFeedbacktest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_feedbacktest(self):
    self.driver.get("http://localhost:8081/website/backend/home.php")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.LINK_TEXT, "CONTACT").click()
    self.driver.find_element(By.NAME, "name").click()
    self.driver.find_element(By.NAME, "name").send_keys("Dweepjyoti Sarma")
    self.driver.find_element(By.NAME, "number").click()
    self.driver.find_element(By.NAME, "number").send_keys("7086642252")
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("sarmadweepjyoti@gmail.com")
    self.driver.find_element(By.NAME, "msg").click()
    self.driver.find_element(By.NAME, "msg").send_keys("Loved it!!")
    self.driver.find_element(By.NAME, "send").click()
  