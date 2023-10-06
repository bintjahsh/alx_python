""" This module is about the python inbuilt module
requests and how to use it to get a url
"""
import sys
import requests

if __name__ == "__main__":
    def get_value():
        """  takes in a URL, sends a request to the URL and 
        displays the value of the variable X-Request-Id in
        the response header
        """
        url = sys.argv
        r = requests.get(url)
        print('{:s}'.format(r.headers.get('X-Request-Id')))
