""" This module is about a python script using inbuilt module
requests to takes in a letter and sends a POST request to 
a url with the letter as a parameter. 
"""
import sys
import requests

if __name__ == "__main__":
        url = 'http://0.0.0.0:5000/search_user'

        if sys.argv == None:
            q = ""
        else:
            q = sys.argv

        r = requests.post(url, {'q': q})
        # res = r.json()
        
        
        if r == None:
            print('No result') 
        elif type(r) != dict:
            print('Not a valid JSON')
        else:
            print('[{}] {}'.format(r.items['id'], r.items['name']))
            

        
