import os
import sys
import re
from pycoingecko import CoinGeckoAPI
from bs4 import BeautifulSoup
import basc_py4chan as bp4

class BizCoinScraper():
    '''
        BizCoinScraper is an object that gets data from 4chan's /biz/ (by default)
        and computes coin statistics data.
    '''
    def __init__(self, board: str='biz', filters: list=[]):
        print('Building Biz Coin Scraper...')
        self.board = bp4.Board(board)
        self.threads = self.board.get_all_threads()
        self.posts = []
        for thread in self.threads:
            for post in thread.posts:
                self.posts.append(post)
        self.filters = filters
        self.wordHist = {}
        self.coingecko = CoinGeckoAPI()
        self.coingecko_coins_list = []
        print('Done.')
    
    def toJSON(self):
        pass
    
    def clean_text(self, rawText: str):
        # cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        # filteredText = re.sub(cleaner, '', rawText)
        bsFiltered = BeautifulSoup(rawText, "lxml").text
        # cleaner = re.compile('>>[0-9]{8}')  # clean replies through GETs
        # filteredText = re.sub(cleaner, '', bsFiltered)
        # cleaner = re.compile('>> [0-9]{8}')  # clean replies through GETs
        # filteredText = re.sub(cleaner, '', filteredText)
        cleaner = re.compile('[0-9]')  # clean replies through GETs
        filteredText = re.sub(cleaner, '', bsFiltered)
        filters = [
            '>', '[', ']', '<', '.', ':', '?', '%', '!', '(', ')', '-',
            '/', '\\', '\'', '$', '@', '=', 'www', 'https', 'http'
        ]
        for filter in filters:
            filteredText = filteredText.replace(filter, ' ') 
        return filteredText.lower()

    def update_coingecko(self):
        print("Fetching from coingecko API...")
        self.coingecko_coins_list = self.coingecko.get_coins_list()
        for num, coinDict in enumerate(self.coingecko_coins_list):
            self.coingecko_coins_list[num] = [
                coinDict['name'].lower(), 
                coinDict['symbol'].lower()
            ]
        print("Done.")
        return self.coingecko_coins_list
    
    def group_all_text(self):
        allText = [
            self.clean_text(rawText=x.comment) for x in self.posts
        ]
        for txt in allText:
            splt = txt.split(' ')
            for word in splt:
                if word:
                    self.wordHist[word] = self.wordHist.get(word, 0) + 1
    
    def find_coin_mentions(self):
        # for num, coinDict in enumerate(self.coingecko_coins_list):
            
        1==1
    
    def scrape(self):
        self.update_coingecko()
        self.group_all_text()
        self.find_coin_mentions()