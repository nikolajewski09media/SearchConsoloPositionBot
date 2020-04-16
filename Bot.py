import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import options
import time

domains = ['https://insektenbekaempfung24.de/', 'https://bio-kammerjaeger.de/', 'https://Wespen-beseitigen.de/',
'https://Ungeziefer-bekaempfen.de/', 'https://Insektenbekaempfung24h.de/',
'https://Schaedlinge-nicht-bei-mir.de/', 'https://kammerjaeger-huber.de/']
keywords = ['Schädlingsbemkäpfung', 'Kammerjäger', 'Wespenbekämpfung', 'Rattenbekämpfung',
'Bettwanzen', 'Kakerlaken', 'Ameisen', 'Flöhe', 'Milben', 'Tauben', 'Marder', 'Siebenschläfer']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Chrome("/Users/mediagmbh/PycharmProjects/SearchConsoloPositionBot/chromedriver",
                           options=chrome_options)
browser.get("https://stackexchange.com/")
time.sleep(5)
browser.find_element_by_link_text('Log in').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
time.sleep(5)
browser.find_element_by_id("identifierId").send_keys("sophia.ebersbacher1984@gmail.com")
time.sleep(5)
browser.find_element_by_id("identifierNext").click()
time.sleep(5)
browser.find_element_by_name("password").send_keys("DHE12345")
time.sleep(5)
browser.find_element_by_id("passwordNext").click()
time.sleep(5)
rating = []
for domain in domains:
    for keyword in keywords:
        url2Gsc = f'https://search.google.com/search-console/performance/search-analytics?resource_id={domain}&metrics=POSITION&query=*{keyword}&breakdown=device&num_of_days=7'
        browser.get(url2Gsc)
        time.sleep(1)
        ratingNr = browser.find_elements_by_class_name('nnLLaf')[3].text
        rating.append(domain)
        rating.append(keyword)
        rating.append(ratingNr)

with open('schädling.csv', 'w', newline='')as f:
    fieldnames = ['Domain', 'Keyword', 'Ranking']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    newIterator = iter(rating)
    endzeile = int(len(rating)/3)
    for itme in range(0,endzeile):
        thewriter.writerow({'Domain': next(newIterator), 'Keyword': next(newIterator), 'Ranking': next(newIterator)})
browser.quit()