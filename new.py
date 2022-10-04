from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import lxml

products = []
prices = []
ratings = []
driver = webdriver.Chrome('D:\DSA\Week 4 Lab\chromedriver.exe')

driver.get("http://eduko.spikotech.com/Course")
content = driver.page_source
soup = BeautifulSoup(content,features="lxml")


card = soup.find_all('div', attrs={"class":"card-title"})
print(card)