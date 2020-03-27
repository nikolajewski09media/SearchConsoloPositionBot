import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import options
import time

keywords = []
with open('keywords.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=";")
    for spalte in csvReader:
        keywords.append(spalte[0])

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
#
# browser = webdriver.Chrome()


#chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

browser = webdriver.Chrome()            #options=chrome_options)
browser.get("https://www.google.com/intl/de/gmail/about/#")
time.sleep(5)
browser.find_element_by_partial_link_text("Anmelden").click()
time.sleep(5)
browser.switch_to.window(browser.window_handles[1])
time.sleep(5)
browser.find_element_by_id("identifierId").send_keys("sophia.ebersbacher1984@gmail.com")
time.sleep(5)
browser.find_element_by_id("identifierNext").click()
time.sleep(5)
browser.find_element_by_name("password").send_keys("DHE12345")
time.sleep(5)
browser.find_element_by_id("passwordNext").click()
time.sleep(5)