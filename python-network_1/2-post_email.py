""" This module is about the python inbuilt module
requests and how to use it to post to a url
"""
import sys
import requests

if __name__ == "__main__":
        url = sys.argv[0]
        email = sys.argv[1]
        payload = email
        r = requests.post(url, data=payload)
        print(r.text)