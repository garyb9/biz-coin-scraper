import os
import sys
import json
from datetime import datetime

srcPath = os.path.join(os.path.dirname(__file__), '..', 'src')
dataPath = os.path.join(os.path.dirname(__file__), '..', 'data')
sys.path.extend([srcPath, dataPath])

from biz_coin_scraper import BizCoinScraper

bizCoinScraper = BizCoinScraper()

bizCoinScraper.update_coingecko()
bizCoinScraper.get_all_text()

time = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
fileName = f'{dataPath}/dump.json'

if not os.path.isdir(dataPath): 
    os.makedirs(dataPath)
with open(fileName, mode="w", encoding="utf-8") as f:
    f.write(json.dumps({}, indent=4, sort_keys=True))
    
print('\nDone - wrote profile to: ' + os.path.abspath(fileName)+'\n')