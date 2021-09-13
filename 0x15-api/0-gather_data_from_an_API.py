#!/usr/bin/python3
"""Fetches a REST Api
For a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos" \
        .format(employee_id)
    
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    
    try:
        user = user_response.json()
        user_todos = todos_response.json()
        completed_tasks = list(filter(lambda x: x.get("completed") is True,
                                      user_todos))
        print("Employee {} is done with tasks({}/{}):"
              .format(user.get("name"), len(completed_tasks),
                      len(user_todos)))
    
        for todo in completed_tasks:
            print("\t{}".format(todo.get("title")))
    except Exception as e:
        print(e)
