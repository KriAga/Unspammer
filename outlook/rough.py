from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

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

# driver = webdriver.Firefox(capabilities=firefox_capabilities )

with open('../emails.csv', 'r+') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", row[2])
        profile.set_preference("network.proxy.http_port", row[3])
        profile.set_preference("network.proxy.ssl", row[2])
        profile.set_preference("network.proxy.ssl_port", row[3])
        profile.set_preference("network.proxy.socks", row[2])
        profile.set_preference("network.proxy.socks_port", row[3])
        profile.update_preferences()
        driver = webdriver.Firefox(firefox_profile=profile, executable_path="D:\\Miscellaneous\\Work\\Shibani\\Freelancer\\google-login\\geckodriver.exe")
        try:
            driver.get("https://outlook.live.com/mail/0/inbox")
            # driver.maximize_window()
            sign_in = WebDriverWait(driver, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Sign in')]"))
                )
            sign_in.click()
            email_phone = WebDriverWait(driver, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))
                )
            email_phone.send_keys(row[0])
            next_email = WebDriverWait(driver, 100).until(
                    EC.element_to_be_clickable((By.ID, "idSIButton9"))
                )
            next_email.click()
            password = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='passwd']"))
            )
            password.send_keys(row[1])
            next_password = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.ID, "idSIButton9"))
            )
            next_password.click()
            driver.get("https://outlook.live.com/mail/0/junkemail")
            time.sleep(5)
            while driver.find_element_by_xpath("//div[@role='checkbox'][@aria-label='Checkbox to select a message'] | //div[@role='checkbox'][@aria-label='Case à cocher pour sélectionner un message']").click():
                driver.find_element_by_xpath("//div[@role='checkbox'][@aria-label='Checkbox to select a message'] | //div[@role='checkbox'][@aria-label='Case à cocher pour sélectionner un message']").click()
                print('hello')
                mark_unspam = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[text()=\"It's not junk\"]"))
                )
                mark_unspam.click()
                print("hello")
                # driver.find_element_by_xpath("//*[text()=\"It's not junk\"]")
        except ElementClickInterceptedException:
            print('Failing becuase button is not Interactable for email:', row[0])
            pass
        except NoSuchElementException:
            print('No more mails to Unspam for:', row[0])
            driver.close()
            pass
        except Exception as e:
            try:
                driver.close()
            except:
                print('Browser Shut')
            print('Failed for: ', row[0], e)
            pass

#  | //*[text()='Courrier légitime']