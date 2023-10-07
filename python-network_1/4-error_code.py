""" This module is about the python inbuilt module
requests and how to use it to get a url status code
"""
import sys
import requests

if __name__ == "__main__":
        url = sys.argv
        r = requests.post(url)
        if r.status_code >= 400:
            print('Error code: {:d}'.format(r.status_code))
        else:
            print(str(r.text))