from bs4 import BeautifulSoup
import requests


url = 'https://abiturient.kpfu.ru/entrant/abit_entrant_originals_list?p_open=&p_faculty=4&p_speciality=543&p_inst=0&p_typeofstudy=1'


def gethtml(url):
    r = requests.get(url)
    return r


def get_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(id="t_common")
    table_rows = table.find_all('tr')

    count = 0
    score = 1000
    lol = 0
    limit = int(7 * 0.8)
    lnRow = 0

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]

        lol += 1
        if lol == 1:
            continue
        lnRow = max(lnRow, len(row))
        print(row[lnRow - 6])

        if row[lnRow - 3] == '\nда\n':
            count += 1
            if count <= limit:
                if row[lnRow - 6] == '':
                    continue
                score = min(score, int(row[lnRow - 6]))

    if count < 0:
        score = 0

    print("Подано согласий:", str(count) + '/' + str(limit))
    print("Текущий проходной:", score)


html = gethtml(url)
get_list(html.text)