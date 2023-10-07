""" This module is about a python script that takes
your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    header_dict = {'Authorization': 'Bearer ' + password, 'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    
    r = requests.get(url, headers=header_dict)
    res = r.json()
    if r.status_code == 200:
        print(res['id'])
    else:
        print('None')
