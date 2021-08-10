import os
import json
import requests

class API_Getter():

    def __init__(self):
        self.url = r'https://a.4cdn.org/'
        pass
    
    def get_json(self, url):
        try:
            r = requests.get(url=url)
            return json.loads(r.text)
        except Exception as e:
            print('Something went wrong with request -> ', str(e))
            return None

    def get_boards(self):
        request = self.url + r'/boards.json'
        ret = self.get_json(url=request)
        return ret['boards'] if 'boards' in ret else None
    
    def get_threads(self, board: str):
        threads = []
        request = self.url + f'/{board}/threads.json'
        ret = self.get_json(url=request)
        
        for item in ret:
            try:
                threads.extend(item['threads'])
            except Exception as e:
                print('Something wrong with query -> ', str(e))
                continue
        return threads

    def get_posts_from_thread(self, board: str, thread: str):
        request = self.url + f'/{board}/thread/{thread}.json'
        ret = self.get_json(url=request)
        return ret['posts'] if 'posts' in ret else None
    
    def get_all_posts(self, board: str):
        posts = []
        threads = self.get_threads(board=board)
        lenThreads = len(threads)
        for idx, thread in enumerate(threads):
            threadID = str(thread['no'])
            print(idx, '/', lenThreads, ': Getting thread ', threadID)
            posts.append(
                self.get_posts_from_thread(board=board, thread=threadID)
            )
        return posts

