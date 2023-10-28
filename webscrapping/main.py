import time
import requests
import selectorlib
import sqlite3


URL = 'https://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect('webscrapping/data.db')



class Event:
    def scrape(self,url):
        ##Scrape de page soucer from the URL
        response = requests.get(url,HEADERS)
        source = response.text
        return source

    def extract(self,source):
        extractor = selectorlib.Extractor.from_yaml_file('webscrapping\extract.yaml')
        value = extractor.extract(source)['tours']
        return value
    

def send_email():
    print('Email Sent')
    

class DataBase:
    def store(self,extracted):
        row = extracted.split(',')
        row = [item.strip() for item in row]
        cursos = connection.cursor()
        cursos.execute("INSERT INTO events VALUES(?,?,?)",row)
        connection.commit()
            
    def read(self,extracted):
        row = extracted.split(',')
        row = [item.strip() for item in row]
        band,city,date = row
        cursos = connection.cursor()
        cursos.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band,city,date))
        rows = cursos.fetchall()
        print(rows)
        return rows

if __name__ == '__main__':
    while True:
        event = Event()   
        dataBase = DataBase()
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print('extracted: ', extracted)
        if extracted != 'No upcoming tours':
            row = dataBase.read(extracted)          
            if not row:
                dataBase.store(extracted)
                send_email()
        time.sleep(2)