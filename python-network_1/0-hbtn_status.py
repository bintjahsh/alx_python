""" This module is about the python inbuilt module
requests and how to use it to get a url
"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alu-intranet.hbtn.io/status')
    type = r.content-type()
    print('''Body response: 
                - type: {:s}
                - content: {:s}'''.format(r['content-type'], r['reason']))

