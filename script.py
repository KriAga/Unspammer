from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import threading
import os,time,csv,datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


a = webdriver.Chrome()
a.get("https://accounts.google.com/")
user = a.find_element_by_name("identifier").send_keys('username@gmail.com')
login = a.find_element_by_id("identifierNext")
login.click()
pwd = WebDriverWait(a, 100).until(EC.presence_of_element_located((By.NAME, "password")))
pwd.send_keys('p######')
login = a.find_element_by_id("passwordNext")
login.click()
clk = WebDriverWait(a, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'myaccount')))
clk.click()
logout = WebDriverWait(a, 10).until(EC.presence_of_element_located((By.ID, "gb_71")))
logout.click()