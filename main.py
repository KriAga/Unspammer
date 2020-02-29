from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

proxy = "89.33.192.56"
port = "3128"
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True

# firefox_capabilities['proxy'] = {
#     "proxyType": "MANUAL",
#     "httpProxy": proxy,
#     "ftpProxy": proxy,
#     "sslProxy": proxy
# }

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", proxy)
profile.set_preference("network.proxy.http_port", port)
profile.set_preference("network.proxy.ssl", proxy)
profile.set_preference("network.proxy.ssl_port", port)
profile.update_preferences()


# driver = webdriver.Firefox(capabilities=firefox_capabilities )
driver = webdriver.Firefox(firefox_profile=profile, executable_path="D:\\Miscellaneous\\Work\\Shibani\\Freelancer\\google-login\\geckodriver.exe")
driver.get("https://mail.google.com/mail/u/1/h/pq3m1hldlteh/")
driver.maximize_window()
email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")

with open('emails.csv', 'r+') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        driver = webdriver.Firefox(firefox_profile=profile, executable_path="D:\\Miscellaneous\\Work\\Shibani\\Freelancer\\google-login\\geckodriver.exe")
        driver.get("https://mail.google.com/mail/u/1/h/pq3m1hldlteh/")
        driver.maximize_window()
        email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
        email_phone.send_keys(row[0])
        driver.find_element_by_id("identifierNext").click()
        password = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
        )
        password.send_keys(row[1])
        driver.find_element_by_id("passwordNext").click()
        driver.find_element_by_xpath("//*[contains(text(), 'Spam')]").click()
        while driver.find_element_by_xpath("//input[@type='checkbox']"):
            driver.find_element_by_xpath("//input[@type='checkbox']").click()
            driver.find_element_by_xpath("//*[contains(text(), 'Not Spam')] | //*[@value='Not Spam']").click()
        driver.close()