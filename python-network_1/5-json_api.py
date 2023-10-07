""" This module is about a python script using inbuilt module
requests to takes in a letter and sends a POST request to 
a url with the letter as a parameter. 
"""
import sys
import requests

if __name__ == "__main__":
        url = 'http://0.0.0.0:5000/search_user'

        if len(sys.argv) == 1:
            q = ""
        else:
            q = sys.argv[1]

        r = requests.post(url, {'q': q})
        
        if r.text != {} & type(r.text) == dict:
            print('[{}] {}'.format(r.text['id'], r.text['name']))
        elif r.text == {}:
            print('No result')
        elif type(r.text) == dict:
            print('Not a valid JSON')

        
