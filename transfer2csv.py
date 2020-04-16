import csv

rating = ['https://insektenbekaempfung24.de/', 'Schädlingsbemkäpfung', 0 , 'https://insektenbekaempfung24.de/', 'Kammerjäger', 45,
          'https://insektenbekaempfung24.de/', 'Schädlingsbemkäpfung', 0 , 'https://insektenbekaempfung24.de/', 'Kammerjäger', 45,
          'https://insektenbekaempfung24.de/', 'Schädlingsbemkäpfung', 0 , 'https://insektenbekaempfung24.de/', 'Kammerjäger', 45,
          'https://insektenbekaempfung24.de/', 'Schädlingsbemkäpfung', 0 , 'https://insektenbekaempfung24.de/', 'Kammerjäger', 45,
          'https://insektenbekaempfung24.de/', 'Schädlingsbemkäpfung', 0 , 'https://insektenbekaempfung24.de/', 'Kammerjäger', 45,
          'https://insektenbekaempfung24.de/', 'Schädlingsbemkäpfung', 0 , 'https://insektenbekaempfung24.de/', 'Kammerjäger', 45,
          'https://insektenbekaempfung24.de/', 'Schädlingsbemkäpfung', 0 , 'https://insektenbekaempfung24.de/', 'Kammerjäger', 45]


with open('schädling.csv', 'w', newline='')as f:
    fieldnames = ['Domain', 'Keyword', 'Ranking']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    newIterator = iter(rating)
    endzeile = int(len(rating)/3)
    for itme in range(0,endzeile):
        thewriter.writerow({'Domain': next(newIterator), 'Keyword': next(newIterator), 'Ranking': next(newIterator)})