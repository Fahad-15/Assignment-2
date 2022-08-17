from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

username = "Your Username"
password = "Your Password"

# Chrome Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://tmoodle.fccollege.edu.pk/moodle/login/index.php")

# Web title
title = driver.title
print("Login Page Title:", driver.title)

# Login attempt
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)

# For absolute path
driver.find_element(By.XPATH, '/html/body/div/div/div/div/section/div/div/div/div/div/div/div/div/form/button').click()

title2 = driver.title

if title2 == "Forman Christian College (A Chartered University)":
    print("Login was Successfull")
else:
    print("Login was Un-Successfull")
