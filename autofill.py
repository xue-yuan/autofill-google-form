import json

import requests
from bs4 import BeautifulSoup

class Form:

    class Console:
        @staticmethod
        def log(text):
            print('[-]', text)

        @staticmethod
        def info(text):
            print('[!]', text)

        @staticmethod
        def success(text):
            print('[+]', text)

        @staticmethod
        def warn(text):
            print('[?]', text)

        @staticmethod
        def error(text):
            print('[x]', text)

    def __init__(self, config):
        self.viewFormURL = config['form_url']
        self.formResponseURL = config['form_url'].replace('viewform', 'formResponse')
        self.response = config['response']
        self.headers = {
            'Host': 'docs.google.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '365',
            'Origin': 'https://docs.google.com',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
            'Referer': self.viewFormURL,
        }
        self.data = {}
        self.__setData()

    def __getContainerID(self, container):
        return json.loads('{"tmp":[' + container.select('.m2')[0].get('data-params')[4:] + '}')['tmp'][0][4][0][0]

    def __setData(self):
        form_html = requests.get(self.viewFormURL)
        dom = BeautifulSoup(form_html.text, 'html.parser')
        containers = dom.select('.freebirdFormviewerViewNumberedItemContainer')

        for container, response in zip(containers, self.response):
            ID = self.__getContainerID(container)
            self.data[f'entry.{ID}'] = response

    def send(self):
        self.Console.log('Start to autofilling...')

        request = requests.post(
            url = self.formResponseURL,
            data = self.data,
            headers = self.headers
        )
        
        if request.status_code == 200: self.Console.success('Success!')
        else: self.Console.error('Failed!')

    def inspector(self, symbol):
        INFO_URL = f'URL:\n{self.viewFormURL}\n{self.formResponseURL}\n'
        INFO_HEADERS = f'HEADERS:\n{self.headers}\n'
        INFO_DATA = f'DATA:\n{self.data}\n'

        if (symbol == 'all'): 
            self.Console.info(f'{INFO_URL}\n')
            self.Console.info(f'{INFO_HEADERS}\n')
            self.Console.info(f'{INFO_DATA}\n')
        elif (symbol == 'url'): self.Console.info(f'{INFO_URL}\n')
        elif (symbol == 'headers'): self.Console.info(f'{INFO_HEADERS}\n')
        elif (symbol == 'data'): self.Console.info(f'{INFO_DATA}\n')
        else: self.Console.error('Invalid Symbol\n')

if __name__ == '__main__':
    with open('autofill.json', 'r') as f:
        config = json.load(f)
    
    form = Form(config)
    form.send()
