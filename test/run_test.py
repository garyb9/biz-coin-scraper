import os
import sys
import json
from datetime import datetime

srcPath = os.path.join(os.path.dirname(__file__), '..', 'src')
dataPath = os.path.join(os.path.dirname(__file__), '..', 'data')
sys.path.extend([srcPath, dataPath])

from api_getter import API_Getter

api = API_Getter()

posts = api.get_all_posts(board='biz')

time = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
fileName = f'{dataPath}/dump.json'

if not os.path.isdir(dataPath): 
    os.makedirs(dataPath)
with open(fileName, mode="w", encoding="utf-8") as f:
    f.write(json.dumps(posts, indent=4, sort_keys=True))
    
print('\nDone - wrote profile to: ' + os.path.abspath(fileName)+'\n')