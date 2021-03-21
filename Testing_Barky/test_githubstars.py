import os
from datetime import datetime
import sqlite3
import requests
import pytest

'''from Testing_Barky.githubaccount import GithubAccountTest'''


def test_get_github_starred_bookmark():
  '''  githubtest_username = "winzadot" '''
  ''' Check this repo is there repo["name"]=='Assignment1-RomanNumbers' '''

next_page_of_results = f"https://api.github.com/users/winzadot/starred"

while next_page_of_results:
            stars_response = requests.get(
                next_page_of_results,
                headers={"Accept": "application/vnd.github.v3.star+json"},
            )
            next_page_of_results = stars_response.links.get("next", {}).get("url")
            for repo_info in stars_response.json():
                repo = repo_info["repo"]
            assert repo["name"]=='Assignment1-RomanNumbers'



def test_get_github_starred_time():
  ''''Assignment1-RomanNumbers' starred_at '2021-03-08T00:06:34Z'''

next_page_of_results = f"https://api.github.com/users/winzadot/starred"
while next_page_of_results:
            stars_response = requests.get(
                next_page_of_results,
                headers={"Accept": "application/vnd.github.v3.star+json"},
            )
            next_page_of_results = stars_response.links.get("next", {}).get("url")
            for repo_info in stars_response.json():
                repo = repo_info["repo"]
            assert repo_info["starred_at"]!=None

           