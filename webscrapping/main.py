import requests
import selectorlib


URL = 'https://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    ##Scrape de page soucer from the URL
    response = requests.get(url,HEADERS)
    source = response.text
    return source

def extract(source):
   extractor = selectorlib.Extractor.from_yaml_file('webscrapping\extract.yaml')
   value = extractor.extract(source)['tours']
   return value

def send_email():
    print('Email Sent')
    
def store(extracted):
    with open('webscrapping/data.txt', 'a') as file:
        file.write(extracted + '\n')
        
def read(extracted):
    with open('webscrapping/data.txt','r') as file:
        return file.read()

if __name__ == '__main__':
    scraped = scrape(URL)
    extracted = extract(scraped)
    print('extracted: ', extracted)
    content = read(extracted)
    if extracted != 'No upcoming tours':
        if  extracted not in content:
            store(extracted)
            send_email()