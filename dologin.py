import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import datetime

#Timer 

def timecount(seconds):
    while seconds:
        min, sec = divmod(seconds, 60)
        count = 'Timer: {:d}min:{:d}sec'.format(min, sec)
        print(count, end='\r')
        sleep(1)
        seconds -= 1

def dologin(username, password, hashtag, limit):
	driver = webdriver.Firefox(executable_path="./geckodriver")
	driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
	print("Opening Instagram")
	timecount(5)
	print("Handling Cookies")
	driver.find_element(by=By.XPATH, value="//html/body/div[4]/div/div/button[1]").click()
	timecount(15)
	userLogin = driver.find_element(by=By.NAME, value="username")
	userLogin.send_keys(username)
	userPass = driver.find_element(by=By.NAME, value="password")
	userPass.send_keys(password)
	submit = driver.find_element(by=By.TAG_NAME, value="form")
	submit.submit()
	timecount(5)
	driver.get("https://instagram.com/" + username)
	timecount(5)

instaUser = input("Username: ")
instaPass = getpass("Password: ")
instaHashtag = input("Hashtag: #")
instaLimit = input("Limit: ")

dologin(instaUser, instaPass, InstaHashtag, InstaLimit)