from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://mail.google.com/mail/u/0/h/1pq68r75kzvdr/?v%3Dlui")
driver.maximize_window()
email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
email_phone.send_keys("kriaga3@gmail.com")
driver.find_element_by_id("identifierNext").click()
password = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
)
password.send_keys("K_A.01.11.1996")
driver.find_element_by_id("passwordNext").click()
# driver.find_elements_by_partial_link_text('Load').click()
# spammer = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.XPATH, "//table[@role='grid']//tbody//tr[@draggable='true']//td[2]"))
# )
# driver.find_element_by_xpath("//*[contains(text(), 'More')]").click()
driver.find_element_by_xpath("//*[contains(text(), 'Spam')]").click()
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("//*[contains(text(), 'Not Spam')] | //*[@value='Not Spam']").click()
# driver.get("https://mail.google.com/mail/u/0/#spam")
# driver.implicitly_wait(10)
# time.sleep(10)
# for i in range(5):
    # time.sleep(5)
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div/@data-tooltip='Select'[span/@role='checkbox']")))
    # driver.find_element(By.CLASS_NAME, value='zA zE').click()
    # a = driver.find_elements_by_class_name('zA zE')
    # driver.find_element_by_xpath("//*[contains(text(), '...')]").click()
    # print(a)
    # for j in a:
    #     print("j", j)
    #     j.click()
    # break;
    # print(a.get_attribute("role"))
    # driver.find_element_by_xpath("//*[contains(text(), 'Not Spam')]").click()

# driver.find_element_by_link_text("Not Spam")