from pygithub3 import Github
import sys
import subprocess
import time

username = raw_input("Enter your username : ")
password = raw_input("Enter your password : ")
githubclient = Github(login = username, password = password)

repo = githubclient.create({"name": raw_input("RepoName: "), "description": raw_input("Description: "), "homepage":""})
subprocess.call(["git", "init"])
subprocess.call(["git", "remote", "add", "origin", repo.clone_url])