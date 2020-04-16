import csv
from selenium import webdriver
import time

# Zu untersuchende Domains
domains = ['https://insektenbekaempfung24.de/']#, 'https://bio-kammerjaeger.de/', 'https://Wespen-beseitigen.de/',
           #'https://Ungeziefer-bekaempfen.de/', 'https://Insektenbekaempfung24h.de/',
           #'https://Schaedlinge-nicht-bei-mir.de/', 'https://kammerjaeger-huber.de/']
# Unter folgenden Keywords
keywords = ['Schädlingsbemkäpfung', 'Kammerjäger', 'Wespenbekämpfung', 'Rattenbekämpfung',
            'Bettwanzen', 'Kakerlaken', 'Ameisen', 'Flöhe', 'Milben', 'Tauben', 'Marder', 'Siebenschläfer']
# In folgenden Ortschaften (Regensburg und Umgebung)
ortschaften = ['Regensburg', 'Lappersdorf', 'Tergernheim', 'Barbing', ' Neutraubling', 'Obertraubling', 'Pentling',
               'Sinzing', 'Nittendorf', 'Pettendorf', 'Zeitlan', 'Wenzenbach', 'Bach%20an%20der%20Donau', 'Mintraching',
               'Köfering', 'Deuerling', 'Pielenhofen', 'Woflsegg', 'Regenstauf', 'Bernhardswald', 'Brennberg',
               'Wiesent', 'Wörth%20an%20der%20Donau', 'Pfatter', 'Riekofen', 'Mötzing', 'Sünching', 'Aufhausen',
               'Pfakofen', 'Hagelstadt', 'Thalmassing', 'Schierling', 'Laaber', 'Brunn', 'Duggendorf', 'Beratshausen',
               'Holzheim%20am%20Forst', 'Kallmünz',
               'Nittenau', 'Falkenstein', 'Roding', 'Bad%20Abbach', 'Kelheim', 'Essing', 'Parsberg', 'Burglengenfeld',
               'Teublitz', 'Hohenfels', 'Painten', 'Saal%20an%20der%20Donau', 'Abendsberg', 'Langquaid',
               'Maxhütte%20Haidhof']

untersuchungsZeitRaumInTagen = 7

# Google-Account-Zugangsdaten
benutzer = "sophia.ebersbacher1984@gmail.com"
passwort = "DHE12345"

# Öffnet den Browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Chrome("/Users/mediagmbh/PycharmProjects/SearchConsoloPositionBot/chromedriver",
                           options=chrome_options)
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
for domain in domains:
    for keyword in keywords:
        for ort in ortschaften:
            url2Gsc = f'https://search.google.com/search-console/performance/search-analytics?resource_id={domain}' \
                      f'&metrics=POSITION&query=*{keyword}%20' \
                      f'{ort}&breakdown=device&num_of_days=' \
                      f'{untersuchungsZeitRaumInTagen}'
            browser.get(url2Gsc)
            time.sleep(10)
            ratingNr = browser.find_elements_by_class_name('nnLLaf')[3].text
            rating.append(domain)
            rating.append(keyword)
            rating.append(ort)
            rating.append(ratingNr)

# Schreibt die Daten in eine CSV
with open('schädling.csv', 'w', newline='')as f:
    fieldnames = ['Domain', 'Keyword', 'Ort', 'Ranking']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    newIterator = iter(rating)
    endzeile = int(len(rating)/4)
    for item in range(0,endzeile):
        thewriter.writerow({'Domain': next(newIterator),
                            'Keyword': next(newIterator),
                            'Ort': next(newIterator),
                            'Ranking': next(newIterator)})
# Beendet den gesamten Vorgang
browser.quit()