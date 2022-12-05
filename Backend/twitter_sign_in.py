from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import json


browser = webdriver.Firefox()


with open("config.json", "r") as f:
    config = json.load(f)

url = 'https://twitter.com/i/flow/login'
email = config["email"]
password = config["password"]
username = config["username"]


browser.get(url)
time.sleep(3)
#find login and password fields
email_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH ,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")))
email_field.send_keys(email)

next_btn = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
next_btn.click()
time.sleep(2)
try:
  pass_field = browser.find_element(By.XPATH ,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
  pass_field.send_keys(password)

  submit_btn = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
  submit_btn.click()
  time.sleep(2)
except Exception as e:
  #input("Enter data and then press any button")
  verify_field = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
  verify_field.send_keys(username)

  submit_btn = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div")
  submit_btn.click()
  time.sleep(2)



  
  pass_field = browser.find_element(By.XPATH ,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
  pass_field.send_keys(password)

  submit_btn = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
  submit_btn.click()
  time.sleep(2)





from selenium.webdriver import ActionChains

autotw1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
autotw1.click()

element = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
ActionChains(browser).move_to_element(element).send_keys("""Just a testing """).perform()

input_xpath = "//input[@accept]"
image_path = config["image_path"]
input_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
input_element.send_keys(image_path)

sendTw = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')))
sendTw.click()