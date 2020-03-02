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
from selenium.common.exceptions import TimeoutException

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
            driver.maximize_window()
            
            sign_in = WebDriverWait(driver, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Sign in')]")),
                    message="Sign in button not found"
                )
            sign_in.click()
            
            email_phone = WebDriverWait(driver, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")),
                    message="Input tag email/phone not found"
                )
            email_phone.send_keys(row[0])
            
            next_email = WebDriverWait(driver, 100).until(
                    EC.element_to_be_clickable((By.ID, "idSIButton9")),
                    message="Next email button not found"
                )
            next_email.click()
            
            password = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='passwd']")),
                message="Input tag password not found"
            )
            password.send_keys(row[1])
            
            next_password = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.ID, "idSIButton9")),
                message="Next button after password not found"
            )
            next_password.click()

            driver.get("https://outlook.live.com/mail/0/junkemail")
            
            checkbox_ready = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox'][@aria-label='Checkbox to select a message'] | //div[@role='checkbox'][@aria-label='Case à cocher pour sélectionner un message']")),
                message="No more mails to unspam"
            )
            while checkbox_ready:
                checkbox_ready.click()
                mark_unspam = WebDriverWait(driver, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[text()=\"It's not junk\"] | //a[text()='Courrier légitime']")),
                    message="Unpamming link not found"
                )
                mark_unspam.click()
                checkbox_ready = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox'][@aria-label='Checkbox to select a message'] | //div[@role='checkbox'][@aria-label='Case à cocher pour sélectionner un message']")),
                    message="No more mails to unspam"
                )
        except ElementClickInterceptedException as e:
            print('Failing becuase button is not Interactable for email:', row[0], "Error:", e)
            pass
        except NoSuchElementException as e:
            print('No Tag found for:', row[0], "Error:", e)
            driver.close()
            pass
        except TimeoutException as e:
            print(e)
            driver.close()
            pass
        except Exception as e:
            try:
                driver.close()
            except:
                print('Browser already shut')
            print('Failed for: ', row[0], e)
            pass
