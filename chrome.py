
from selenium import webdriver
import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.proxy import Proxy, ProxyType

failure_flag = False
failed_emails = []
failed_pass = []
  
mail_type = 0   # 0 for Gmail and 1 for Hotmail/Outlook
with open('emails.csv', 'r+') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        try:
            print('Started for', row[0])
            if int(row[4]) == 1:
                proxy = row[2]
                port = int(row[3])
                myProxy = proxy + ":" + str(port)
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_extension('extension\extension_3_8_9_0.crx')
                chrome_options.add_argument('--proxy-server=%s' % myProxy)
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                driver = webdriver.Chrome(options=chrome_options, executable_path="chromedriver.exe")
            else:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_extension('extension\extension_3_8_9_0.crx')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                driver = webdriver.Chrome(options=chrome_options, executable_path="chromedriver.exe")
            passed = False
            if row[0].split('@')[-1] == 'gmail.com':
                mail_type = 0
            else:
                mail_type = 1
            if mail_type == 0:
                driver.get("https://mail.google.com/mail/u/1/h/pq3m1hldlteh/")
                email_phone = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//input[@id='identifierId']")),
                        message="Input tag email/phone not found"
                    )
                email_phone.send_keys(row[0])
                
                next_email = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.ID, "identifierNext")),
                        message="Next email button not found"
                    )
                next_email.click()

                password = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")),
                    message="Input tag password not found"
                )
                password.send_keys(row[1])
                
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID , "passwordNext")),
                    message="Next button after password not found"
                )
                next_button.click()
                
                spammer = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Spam')]")),
                    message="Spam box not found"
                )
                spammer.click()
                try:
                    checkbox_ready = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")),
                            message="Checkbox for junk mails in " + row[0] + " mailing address not found"
                    )
                except Exception as e:
                    driver.close()
                    print(row[0] + " : Passed :", e)
                    passed = True
                    if passed:
                        pass
                while checkbox_ready:

                    checkbox_ready.click()

                    mark_unspam = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Not Spam')] | //input[@type='submit'][@value='Non-spam'] | //input[@type='submit'][@value='Non Spam']")),
                        message="Unpamming link not found"
                    )
                    mark_unspam.click()
                    time.sleep(3)
                    try:
                        checkbox_ready = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")),
                            message="Checkbox for junk mails in " + row[0] + " mailing address not found"
                        )
                    except Exception as e:
                        driver.close()
                        print(row[0] + " : Passed :", e)
                        passed = True
                    if passed:
                        break
            else:
                driver.get("https://outlook.live.com/mail/0/inbox")
                sign_in = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Sign in')]")),
                        message="Sign in button not found"
                    )
                sign_in.click()
                
                email_phone = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")),
                        message="Input tag email/phone not found"
                    )
                email_phone.send_keys(row[0])
                
                next_email = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.ID, "idSIButton9")),
                        message="Next email button not found"
                    )
                next_email.click()
                
                password = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@name='passwd']")),
                    message="Input tag password not found"
                )
                password.send_keys(row[1])
                
                next_password = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "idSIButton9")),
                    message="Next button after password not found"
                )
                next_password.click()

                driver.get("https://outlook.live.com/mail/0/junkemail")
                try:
                    checkbox_ready = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox'][@aria-label='Checkbox to select a message'] | //div[@role='checkbox'][@aria-label='Case à cocher pour sélectionner un message']")),
                        message="Checkbox for junk mails in " + row[0] + " mailing address not found"
                    )
                except Exception as e:
                    driver.close()
                    print(row[0] + " : Passed :", e)
                    passed = True
                    if passed:
                        pass
                while checkbox_ready:

                    checkbox_ready.click()

                    mark_unspam = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[text()=\"It's not junk\"] | //a[text()='Courrier légitime']")),
                        message="Unpamming link not found"
                    )
                    mark_unspam.click()
                    time.sleep(10)
                    try:
                        checkbox_ready = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//div[@role='checkbox'][@aria-label='Checkbox to select a message'] | //div[@role='checkbox'][@aria-label='Case à cocher pour sélectionner un message']")),
                            message="Checkbox for junk mails in " + row[0] + " mailing address not found"
                        )
                    except Exception as e:
                        driver.close()
                        print(row[0] + " : Passed :", e)
                        passed = True
                    if passed:
                        break
        except ElementClickInterceptedException as e:
            driver.close()
            print('Failing because button is not Interactable for email:', row[0], "Error:", e)
            failure_flag = True
            failed_emails.append(row[0])
            failed_pass.append(row[1])
            pass
        except NoSuchElementException as e:
            driver.close()
            print('No more mails to Unspam for:', row[0], "Error:", e)
            pass
        except TimeoutException as e:
            driver.close()
            print("Time out for:", row[0], e)
            failure_flag = True
            failed_emails.append(row[0])
            failed_pass.append(row[1])
            pass
        except Exception as e:
            try:
                driver.close()
            except:
                print('Browser Shut')
            print('Failed for: ', row[0], e)
            failure_flag = True
            failed_emails.append(row[0])
            failed_pass.append(row[1])
            pass

if failure_flag:
    with open('failed_emails.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(failed_emails, failed_pass))