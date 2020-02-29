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
# driver = webdriver.Firefox(firefox_profile=profile, executable_path="D:\\Miscellaneous\\Work\\Shibani\\Freelancer\\google-login\\geckodriver.exe")
# driver.get("https://mail.google.com/mail/u/1/h/pq3m1hldlteh/")
# driver.maximize_window()
# email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")

with open('emails.csv', 'r+') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", row[2])
        profile.set_preference("network.proxy.http_port", row[3])
        profile.set_preference("network.proxy.ssl", row[2])
        profile.set_preference("network.proxy.ssl_port", row[3])
        profile.set_preference("network.proxy.socks", row[2]);
        profile.set_preference("network.proxy.socks_port", row[3]);
        profile.update_preferences()
        driver = webdriver.Firefox(firefox_profile=profile, executable_path="D:\\Miscellaneous\\Work\\Shibani\\Freelancer\\google-login\\geckodriver.exe")
        try:
            driver.get("https://mail.google.com/mail/u/1/h/pq3m1hldlteh/")
            # driver.maximize_window()
            email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
            email_phone.send_keys(row[0])
            driver.find_element_by_id("identifierNext").click()
            password = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
            )
            password.send_keys(row[1])
            next_button = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.ID , "passwordNext"))
            )
            next_button.click()
            spammer = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Spam')]"))
            )
            spammer.click()
            # driver.find_element_by_xpath("//*[contains(text(), 'Spam')]").click()
            if driver.find_element_by_xpath("//input[@type='checkbox']"):
                while driver.find_element_by_xpath("//input[@type='checkbox']"):
                    driver.find_element_by_xpath("//input[@type='checkbox']").click()
                    # for probable_unspam_button in driver.find_elements_by_xpath("//input[@type='submit'][@value='Non-spam']"):
                        # if probable_unspam_button.
                    # driver.find_element_by_xpath("//input[@value='Non-spam']").click()
                    driver.find_element_by_xpath("//*[contains(text(), 'Not Spam')] | //input[@type='submit'][@value='Non-spam']").click()
                    # driver.find_element_by_xpath("//input[@type='submit'][@value='Non-spam']").click()
            else:
                print('Nothing to Unpsam now for:', row[0])
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