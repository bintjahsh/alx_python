""" This module is about the python inbuilt module
requests and how to use it to get a url
"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alu-intranet.hbtn.io/status')
    type = str(type(r.text))
    contents = r.text
    print("Body response:\n - type: {:s}\n - content: {:s}".format(type, contents))