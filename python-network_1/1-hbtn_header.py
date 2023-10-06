""" This module is about the python inbuilt module
requests and how to use it to get a url
"""
import sys
import requests

if __name__ == "__main__":
    def get_value(url):
        """  takes in a URL, sends a request to the URL and 
        displays the value of the variable X-Request-Id in
        the response header
        """
        # url = sys.argv
        headers = {'X-Request-Id': 'None'}
        r = requests.get(url, headers=headers)
        print('{:s}'.format(r.headers.get('X-Request-Id')))
