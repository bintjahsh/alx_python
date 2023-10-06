""" This module is about the python inbuilt module
requests and how to use it to get a url
"""
import sys
import requests

if __name__ == "__main__":
        url = sys.argv
        r = requests.get(url)
        print('{:s}'.format(r.headers.get('X-Request-Id')))
