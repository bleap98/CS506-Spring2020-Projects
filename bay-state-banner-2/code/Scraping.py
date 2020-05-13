# Generated by Selenium IDE
import pytest
import time
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random


class TestFre():
  def setup_method(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', {"plugins.always_open_pdf_externally": True,"download.default_directory":"D:\\506dataPDF\\ic"})
    #chrome_options.add_argument('--proxy-server=%s' % proxy)
    self.driver=webdriver.Chrome(executable_path='/Users/ymy/chromedriver', options=chrome_options)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_fre(self,word):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', {"plugins.always_open_pdf_externally": True,"download.default_directory":"D:\\506dataPDF\\ic"})
    #chrome_options.add_argument('--proxy-server=%s' % proxy)
    self.driver=webdriver.Chrome(executable_path='/Users/ymy/chromedriver', options=chrome_options)
   
    self.vars = {}
    self.driver.get("http://corp.sec.state.ma.us/corpweb/CorpSearch/CorpSearch.aspx")
    self.driver.set_window_size(787, 824)
    self.driver.find_element(By.ID, "MainContent_txtEntityName").click()
    self.driver.find_element(By.ID, "MainContent_txtEntityName").send_keys(word)
    self.driver.find_element(By.ID, "MainContent_ddRecordsPerPage").click()
    dropdown = self.driver.find_element(By.ID, "MainContent_ddRecordsPerPage")
    dropdown.find_element(By.XPATH, "//option[. = 'All items']").click()
    #links=[link.find_element_by_css_selector('td a') for link in self.driver.find_element(By.XPATH, "//td/a")]
    links=[link.get_attribute("href") for link in self.driver.find_elements(By.XPATH, "//td/a")]
    num=0
    for link in links:
    #for link in self.driver.find_elements(By.XPATH, "//td/a"):
      #link.get_attribute("href")
      #print(link.get_attribute("href"))
      #sleep(random.randint(1,6))
      self.driver.get(link)
      #num+=1
      #link.click()
      sleep(0.5)
      dropdown = self.driver.find_element(By.ID, "MainContent_lstFilings")
      if(len(dropdown.find_elements(By.XPATH, "//option[. = 'Annual Report']")) < 1):
        continue
      dropdown.find_element(By.XPATH, "//option[. = 'Annual Report']").click()
      self.driver.find_element(By.ID, "MainContent_btnViewFilings").click()
      pdflinks=[]
      for pdflink in self.driver.find_elements(By.XPATH, "//td/a"):
        attr=pdflink.get_attribute("href")
        if(attr.find("2010")>0):
          pdflinks.append(pdflink.get_attribute("href"))
        elif(attr.find("2011")>0):
          pdflinks.append(pdflink.get_attribute("href"))
        elif(attr.find("2012")>0):
          pdflinks.append(pdflink.get_attribute("href"))
        elif(attr.find("2013")>0):
          pdflinks.append(pdflink.get_attribute("href"))
        elif(attr.find("2014")>0):
          pdflinks.append(pdflink.get_attribute("href"))
        elif(attr.find("2015")>0):
          pdflinks.append(pdflink.get_attribute("href"))
        elif(attr.find("2016")>0):
          pdflinks.append(pdflink.get_attribute("href"))
        elif(attr.find("2017")>0):
          pdflinks.append(pdflink.get_attribute("href"))
        elif(attr.find("2018")>0):
          pdflinks.append(pdflink.get_attribute("href"))
        elif(attr.find("2019")>0):
          pdflinks.append(pdflink.get_attribute("href"))
        elif(attr.find("2020")>0):
          pdflinks.append(pdflink.get_attribute("href"))
      #pdflinks.extend([pdflink.get_attribute("href") for pdflink in self.driver.find_elements(By.XPATH, "//td/a")]) 
      for pdflink in pdflinks:
        self.driver.get(pdflink)
        num+=1
        if (num%50==0):
          sleep(2)
          self.driver.quit()
          self.driver=webdriver.Chrome(executable_path='/Users/ymy/chromedriver', options=chrome_options)
      #for pdf in self.driver.find_elements(By.XPATH, "//td/a"):
       # pdf.click()
        

      
    '''
    dropdown = self.driver.find_element(By.ID, "MainContent_lstFilings")
    dropdown.find_element(By.XPATH, "//option[. = 'Annual Report']").click()
    #self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.ID, "MainContent_btnViewFilings").click()
    #self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.XPATH, "//td[6]/a").click()
    '''
    sleep(3)
    self.driver.quit()
    '''
    self.vars["win4233"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win4233"])
    #self.driver.get_screenshot_as_file("C:/Users/82585/Desktop/study/cs506/project/1.png")
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    '''
    #self.driver.get('CorpSearchRedirector.aspx?Action=PDF&Path=CORP_DRIVE1/2018/1129/000000000/0023/201849186580_1.pdf')
test=TestFre()
words=[]
#a=["a","b","c","z"]
letter1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#b=["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
letter2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letter3=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#letter3=["m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for letter_1 in letter1:
  for letter_2 in letter2:
    for letter_3 in letter3:
      word=letter_1+letter_2+letter_3
      words.append(word)
#print(words)
for word in words:
  test.test_fre(word)

#test.test_fre("ibb")