from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

username = 'PES2UG23CS049'
password = 'donteventry'
url = 'https://www.pesuacademy.com/Academy/'
newurl = 'https://www.pesuacademy.com/Academy/s/studentProfilePESU'
driver = webdriver.Chrome()
driver.get(url)


driver.find_element(By.XPATH, '//*[@id="j_scriptusername"]').send_keys(username)
driver.find_element(By.NAME, 'j_password').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="postloginform#/Academy/j_spring_security_check"]').click()

time.sleep(1)  


try:
    time.sleep(1)
    courses = driver.find_element(By.XPATH, '//*[@id="menuTab_653"]/a/span[2]')
    courses.click()
    time.sleep(1)
    select_element = driver.find_element(By.XPATH, '//*[@id="semesters"]')
    select = Select(select_element)
    select.select_by_visible_text('Sem-3')

except Exception as e:
    print(f"Error: {e}")

time.sleep(100)  # Keep the browser open to observe changes
driver.quit()
