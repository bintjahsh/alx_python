""" This module is about a python script using inbuilt module
requests to takes in a letter and sends a POST request to 
a url with the letter as a parameter. 
"""
import sys
import requests

if __name__ == "__main__":
        url = 'http://0.0.0.0:5000/search_user'

        if len(sys.argv) < 2 | sys.argv[1] == None:
            q = ""
        else:
            q = sys.argv[1]

        r = requests.post(url, {'q': q})

        try:
            res = r.json()
            if res == {}:
                print('No result')
            else:
                print('[{}] {}'.format(res['id'], res['name']))
        except:
            print('Not a valid JSON')
            

        # url = 'https://jsonplaceholder.org/posts/1'

        # if sys.argv == None:
        #     q = ""
        # else:
        #     q = sys.argv

        # r = requests.get(url)
        # try:
        #     res = r.json()
        #     if res == {}:
        #         print('No result')
        #     else:
        #         print('[{}] {}'.format(res['id'], res['status']))
        # except:
        #     print('Not a valid JSON')
        
