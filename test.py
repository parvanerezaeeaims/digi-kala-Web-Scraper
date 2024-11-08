
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from unidecode import unidecode
from bs4 import BeautifulSoup
from time import sleep
from os import system
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome(executable_path=r"C:\Users\ASUS\Desktop\digikala\chromedriver.exe", options= webdriver.ChromeOptions())
url = 'https://www.digikala.com/best-selling/'
driver.get(url)
# sleep(10)
# try :
#     driver.find_element(By.XPATH ,'//*[@id="base_layout_desktop_fixed_header"]/header/nav/div[1]/div[1]/div[2]/div[4]/a').click()
# except :
#         pass
# sleep(5)
# try :
#     elements = driver.find_elements(By.CLASS_NAME,"styles_Link__RMyqc" )
# except :
#         pass
# print(elements)
page_source = driver.page_source

# Close the webdriver session
driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

# Find all anchor elements with class 'styles_Link__RMyqc' and get their 'href' attribute
links = [a['href'] for a in soup.find_all('a', class_='styles_Link__RMyqc')]


df = pd.DataFrame(links,columns=['MainLink'] )
df.to_csv('links.csv' ,index=False)