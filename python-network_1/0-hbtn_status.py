""" This module is about the python inbuilt module
requests and how to use it to get a url
"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alu-intranet.hbtn.io/status')
    text = type(r.text)
    contents = r.text
    res = ('''Body response:\n\t- type: {}\n\t- content: {} '''.format(text, contents))
    print(res)
    # print(len(res))