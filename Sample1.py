from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

s=Service(executable_path="C:\\Selenium Web Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[contains(@id,'u_0_0_')]").click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"firstname"))).send_keys("Rajesh")
driver.find_element(By.NAME,"lastname").send_keys("Kanna")

