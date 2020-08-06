from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# basic step for starting selenium
driver = webdriver.Chrome()
driver.get("https://www.google.co.in/")
element = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
element.clear()
element.send_keys("facebook") 
element.send_keys(Keys.RETURN)
driver.quit()
