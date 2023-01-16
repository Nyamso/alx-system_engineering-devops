#!/usr/bin/python3
"""Accepts employee ID and returns TODO list progress"""
import requests
import sys
if __name__ == "__main__":
    
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    dict_user = user.json()

    tasks = requests.get('{}todos?userId={}'.format(url, sys.argv[1]))
    list_tasks = tasks.json()

    num_done = 0
    num_total = 0
    titles = []
    for task in list_tasks:
        if task.get("completed") is True:
            num_done += 1
            titles.append(task.get("title"))
        num_total += 1

    string = 'Employee {} is done with tasks({:d}/{:d}):'
    print(string.format(dict_user.get("name"), num_done, num_total))
    for title in titles:
        print("\t {}".format(title))
