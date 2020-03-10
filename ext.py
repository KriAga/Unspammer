from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 

options = webdriver.ChromeOptions()
options.add_extension('extension\extension_3_8_9_0.crx')
driver = webdriver.Chrome(options=options) 
driver.get('http://www.google.com')