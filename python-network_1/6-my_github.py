""" This module is about a python script that takes
your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = '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'
    header_dict = {'Authorization': 'Bearer {}'.format(password), 'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    
    r = requests.get(url, headers=header_dict)
    res = r.json()
    print(res['id'])