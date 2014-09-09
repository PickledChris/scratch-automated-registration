from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementNotVisibleException
import csv
import logging

logger = logging.basicConfig(filename="students-created.log", level=logging.INFO)

monthDict = {'01': "January", '02': "February", '03': "March", '04': "April",
             '05': "May", '06': "June", '07': "July", '08': "August",
             '09': "September", '10': "October", '11': "November", '12': "December"}

with open("students.csv", 'rt') as file:
    students = csv.reader(file)
    
    driver = webdriver.Chrome()
    driver.get("http://scratch.mit.edu")

    for student in students:
        completed = False
        while not completed:
            try:       
                menu = driver.find_element_by_class_name("join-scratch")
                menu.click()

                driver.implicitly_wait(10)

                username = driver.find_element_by_xpath("(//input[@name='username'])[3]")
                username.send_keys(student[0].replace('.', '-'))
                password = driver.find_element_by_xpath("(//input[@name='password'])[3]")
                password.send_keys(student[1])
                password_confirm = driver.find_element_by_name("password-confirm")
                password_confirm.send_keys(student[1])

                next_button = driver.find_element_by_id("registration-next")
                next_button.click()

                birth_month = Select(driver.find_element_by_name("birthmonth"))
                birth_month.select_by_visible_text(monthDict[student[3][3:5]])
                birth_year = Select(driver.find_element_by_name("birthyear"))
                birth_year.select_by_visible_text(student[3][6:])
                gender = driver.find_element_by_id("gender_other_radio")
                gender.click()
                country = Select(driver.find_element_by_name("country"))
                country.select_by_visible_text("United Kingdom")
                email = driver.find_element_by_name("email")
                email.send_keys(student[2])

                next_button.click()
                
                logging.info(student[0].replace('.', '-') + " successfully created")
                
                driver.delete_all_cookies()
                driver.refresh()
                
            except ElementNotVisibleException:
                driver.close()
                driver = webdriver.Chrome()
                driver.get("http://scratch.mit.edu")
                logger.error("ElementNotVisibleException while processing " + student)
            else:
                completed = True


