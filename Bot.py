import csv
from selenium import webdriver
import time
import platform
from selenium.common.exceptions import NoSuchElementException

# Überprüft das Betriebssystem
if platform.system() == 'Darwin':
    path2Chromedriver = '/Users/mediagmbh/PycharmProjects/SearchConsoloPositionBot/'
else:
    path2Chromedriver = ''

# Zu untersuchende Domains
domains = ['https://sanitaer-service-24h.de/']#, 'https://heizung-sanitaer-hilfe.net/', 'https://sanitaer-nd.de/',
           #'https://klempner24h.de/', 'https://ihr-klempner.de/',
           #'https://notdienst-sanitaer.de/', 'https://sanitaerhilfe.de/']
# Unter folgenden Keywords
keywords = ['Sanitär', 'Sanitärservice']#, 'Sanitärnotdienst', 'Heizung Sanitär',
            #'Gas-Wasser-Installateur', 'Wasserschaden', 'Rohrbruch']
# In folgenden Ortschaften (Regensburg und Umgebung)
ortschaften = ['Regensburg']#, 'Lappersdorf', 'Tegernheim', 'Barbing', ' Neutraubling', 'Obertraubling', 'Pentling',
               #'Sinzing', 'Nittendorf', 'Pettendorf', 'Zeitlarn', 'Wenzenbach', 'Bach%20an%20der%20Donau', 'Mintraching',
               #'Köfering', 'Deuerling', 'Pielenhofen', 'Wolfsegg', 'Regenstauf', 'Bernhardswald', 'Brennberg',
               #'Wiesent', 'Wörth%20an%20der%20Donau', 'Pfatter', 'Riekofen', 'Mötzing', 'Sünching', 'Aufhausen',
               #'Pfakofen', 'Hagelstadt', 'Thalmassing', 'Schierling', 'Laaber', 'Brunn', 'Duggendorf', 'Beratshausen',
               #'Holzheim%20am%20Forst', 'Kallmünz',
               #'Nittenau', 'Falkenstein', 'Roding', 'Bad%20Abbach', 'Kelheim', 'Essing', 'Parsberg', 'Burglengenfeld',
               #'Teublitz', 'Hohenfels', 'Painten', 'Saal%20an%20der%20Donau', 'Abendsberg', 'Langquaid',
               #'Maxhütte%20Haidhof']

untersuchungsZeitRaumInTagen = 7

# Google-Account-Zugangsdaten
benutzer = "steffen.glockner1966@gmail.com"
passwort = "DHE12345"

# Öffnet den Browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Chrome(f"{path2Chromedriver}chromedriver", options=chrome_options)
# Navigiert zum Google-Account-Login (Workaround über externe Seite)
browser.get("https://stackexchange.com/")
time.sleep(5)
browser.find_element_by_link_text('Log in').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
time.sleep(5)
browser.find_element_by_id("identifierId").send_keys(benutzer)
time.sleep(5)
browser.find_element_by_id("identifierNext").click()
time.sleep(5)
browser.find_element_by_name("password").send_keys(passwort)
time.sleep(5)
browser.find_element_by_id("passwordNext").click()
time.sleep(5)
# Untersucht ab hier das Ranking auf Google-Search-Console
rating = []
try:
    for domain in domains:
        for keyword in keywords:
            for ort in ortschaften:
                url2Gsc = f'https://search.google.com/search-console/performance/search-analytics?resource_id={domain}' \
                          f'&metrics=POSITION&query=*{keyword}%20' \
                          f'{ort}&breakdown=device&num_of_days=' \
                          f'{untersuchungsZeitRaumInTagen}'

                browser.get(url2Gsc)
                browser.find_elements_by_class_name('Ec82ie')[10].click()
                #Stellschraube für Zeit
                time.sleep(4)
                #Stellschraube für Zeit
                try:
                    ratingNrMobil = browser.find_elements_by_class_name('CrQbQ')[1].text
                except NoSuchElementException:
                    ratingNrMobil = '0'
                try:
                    ratingNrPC = browser.find_elements_by_class_name('CrQbQ')[0].text
                except NoSuchElementException:
                     ratingNrPC = '0'
                try:
                    ratingNrTablet = browser.find_elements_by_class_name('CrQbQ')[2].text
                except NoSuchElementException:
                    ratingNrTablet = '0'

                rating.append(domain)
                rating.append(keyword)
                rating.append(ort)
                rating.append(ratingNrMobil)
                rating.append(ratingNrPC)
                rating.append(ratingNrTablet)
finally:
    # Schreibt die Daten in eine CSV
    with open('schädling.csv', 'w', newline='')as f:
        fieldnames = ['Domain', 'Keyword', 'Ort', 'RankingMobil', 'RankingPC', 'RankingTablet']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        thewriter.writeheader()
        newIterator = iter(rating)
        endzeile = int(len(rating)/6)
        for item in range(0, endzeile):
            thewriter.writerow({'Domain': next(newIterator),
                                'Keyword': next(newIterator),
                                'Ort': next(newIterator),
                                'RankingMobil': next(newIterator),
                                'RankingPC': next(newIterator),
                                'RankingTablet': next(newIterator)})
    # Beendet den gesamten Vorgang
   # browser.quit()