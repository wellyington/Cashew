import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from getpass import getpass
import os
import datetime
import random
import mysql.connector
from config import host, database, myuser, mypass

# MySQL Connector

myconn = mysql.connector.connect(host=host, database=database, user=myuser, password=mypass)

#Timer 

def timecount(seconds):
    while seconds:
        min, sec = divmod(seconds, 60)
        count = 'Timer: {:d}min:{:d}sec'.format(min, sec)
        print(count, end='\r')
        sleep(1)
        seconds -= 1
randTime = random.randint(5, 20)

# doengagement() function

def doexplore(username, password, limit):
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
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
	print("Opening Explore")
	driver.get("https://www.instagram.com/explore/")
	timecount(25)
	engagements = 0
	engLimit = int(limit)
	driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div/div[2]").click()
	timecount(5)
	print("Starting Engagement: ")
	while engagements != engLimit:
		try:
			NULL_ = None
			date_time = datetime.datetime.now()
			username = instaUser
			profile = driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span/a").text
			url = driver.current_url
			_date = str(date_time.date())
			_time = str(date_time.strftime("%X"))
			cursor = myconn.cursor(buffered=True)
			verification = (username, url)
			sqlCheck = "Select username, url From engagements_explore where username = %s and url = %s"
			cursor.execute(sqlCheck,verification)
			row_count = cursor.rowcount
			if row_count == 0:
				try:
					print("Starting Engagement")
					engagement = (NULL_, username, profile, url, _date, _time)
					sql = "INSERT INTO `engagements_explore`(`ID`,`username`,`profile`,`url`,`date`,`time`) VALUES(%s,%s,%s,%s,%s,%s)"
					cursor.execute(sql,engagement)
					myconn.commit()
					driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
					engagements = engagements + 1
					timecount(randTime)
					print("Engagement: " + str(engagements) + "     ")
					timecount(randTime)
					try:
						driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button").click()
					except:
						driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button").click()
				except:
					try:
						driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button").click()
					except:
						driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button").click()
				timecount(randTime)
			else:
				print("Post already engaged!")
				timecount(randTime)
				try:
					driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button").click()
				except:
					driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button").click()
			timecount(5)
		except:
			try:
				driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button").click()
			except:
				driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button").click()
			timecount(5)
	else:
		print("Engagement complete.")
		driver.quit()

instaUser = input("Username: ")
instaPass = getpass("Password: ")
instaLimit = input("Limit: ")

doexplore(instaUser, instaPass, instaLimit)