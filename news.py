import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)
now = datetime.now()
month_day_year = now.strftime("%m%d%Y")


web_link = 'https://www.thesun.co.uk/sport/football/'
chromdriver_path = 'C:/Users/mamon/Downloads/chromedriver_win32\chromedriver.exe'

# Creating driver connection
driver_service = Service(executable_path=chromdriver_path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web_link)

# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')
# special_offerNews=driver.find_elements(by="xpath", value='//div[@class="rail__item-content"]')

news_titles = []
news_subtitles = []
news_links = []
# offer_headrs=[]
# offer_link=[]
for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    news_titles.append(title)
    news_subtitles.append(subtitle)
    news_links.append(link)

# for special_offer in special_offerNews:
#     offer_head=special_offer.find_element(by='xpath',value='./a/h3').text
#     # offer_links=special_offer.find_element(by='xpath',value='./a').get_attribute('href')
#     offer_headrs.append(offer_head)
#     # offer_link.append(offer_links)

# Creating CSV file for data exporting
news_dict = {'title': news_titles, 'subtitle': news_subtitles, 'link': news_links}
news_dataF = pd.DataFrame(news_dict)
file_name = f'newsheadline_{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
news_dataF.to_csv(final_path)
# news_dataF.to_csv('newsheadline.csv')
# #offer dict
# offer_dict={'offer_head':offer_headrs}
# offer_dataF=pd.DataFrame(news_dict)
# offer_dataF.to_csv('offer.csv')

driver.quit()