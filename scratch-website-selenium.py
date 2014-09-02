from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("http://scratch.mit.edu")

menu = driver.find_element_by_class_name("join-scratch")
menu.click()

driver.implicitly_wait(5)

username = driver.find_element_by_xpath("(//input[@name='username'])[3]")
username.send_keys("benhurst1014")
password = driver.find_element_by_xpath("(//input[@name='password'])[3]")
password.send_keys("password1")
password_confirm = driver.find_element_by_name("password-confirm")
password_confirm.send_keys("password1")

next_button = driver.find_element_by_id("registration-next")
next_button.click()

birth_month = Select(driver.find_element_by_name("birthmonth"))
birth_month.select_by_visible_text("January")
birth_year = Select(driver.find_element_by_name("birthyear"))
birth_year.select_by_visible_text("1990")
gender = driver.find_element_by_name("gender")
gender.click()
country = Select(driver.find_element_by_name("country"))
country.select_by_visible_text("United Kingdom")
email = driver.find_element_by_name("email")
email.send_keys("benhurst1010@bugmenot.com")

next_button.click()

finish_button = driver.find_element_by_id("registration-done")
finish_button.click()

driver.delete_all_cookies()
driver.refresh()

