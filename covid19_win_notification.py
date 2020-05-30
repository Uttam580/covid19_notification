# data scrapped from mohfw website using beautifulsoup
# get notification  on desktop using plyer

#'this is created by uttam'

from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title, message):
    notification.notify(title=title,
                        message=message,
                        app_icon=None,
                        timeout=5)


def getdata(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    myHtmldata = getdata('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(myHtmldata, 'html.parser')
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    total = []
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        total.append(cols)
    final = total[:33]
    lst = ['Maharashtra', 'Rajasthan', 'Gujarat']
    for item in final:
        if item[1] in lst:
            # print(item)
            nTitle = 'Cases of Covid_19'
            nText = f"State :{item[1]},Indian : {item[2]}, Foreigner : {item[3]},Death : {item[4]}"
            print(nText)
            notifyme(nTitle, nText)
            time.sleep(3)
