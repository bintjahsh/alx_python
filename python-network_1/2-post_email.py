""" This module is about the python inbuilt module
requests and how to use it to post to a url
"""
import sys
import requests

if __name__ == "__main__":
        url = sys.argv[0]
        email = sys.argv[1]
        r = requests.post(url, param=email)
        print(r.text)

