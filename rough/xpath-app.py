from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
caps = DesiredCapabilities().FIREFOX
caps["marionette"] = True
driver = webdriver.Firefox(capabilities=caps, firefox_binary=binary, executable_path="D:\\Miscellaneous\\Work\\Shibani\\Freelancer\\google-login\\geckodriver.exe")
# time.sleep(10)
driver.get("https://mail.google.com/")
email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
email_phone.send_keys("kriaga3@gmail.com")
driver.find_element_by_id("identifierNext").click()
password = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
)
password.send_keys("K_A.01.11.1996")
driver.get("https://mail.google.com/mail/u/0/#spam")
# driver.find_element_by_id("passwordNext").click()
# driver.find_element_by_link_text("More")
# driver.find_element_by_link_text("Spam")

# driver.find_element_by_xpath("body/table/tbody/tr/td[2]").click()
# # driver.find_element_by_class_name("CJ").click()
# # driver.find_element_by_id(":108").click()
# # driver.find_element_by_id(":12i").click()
# driver.find_elements_by_xpath("//*[contains(text(), 'Not Spam')]").click()
# # a = driver.find_element_by_name('tbody')
# # print(a)

# more_button = driver.find_element_by_xpath("//div//span[@role='button']")
# if more_button.text == 'More':
#     if driver.find_element_by_xpath("//div//span")
# print(a.text)
# a.click()
# driver.find_element_by_link_text("More")
# driver.find_element_by_link_text("Spam")