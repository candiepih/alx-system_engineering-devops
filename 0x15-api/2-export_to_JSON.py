#!/usr/bin/python3
"""Fetches a REST Api
Records all tasks that are owned by this employee to a json file
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos" \
        .format(employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    try:
        user = user_response.json()
        user_todos = todos_response.json()
        tasks = list(map(lambda todo: {
                             "task": todo.get("title"),
                             "completed": todo.get("completed"),
                             "username": user.get("username")
                         },
                         user_todos))
        json_data = {
            user.get("id"): tasks
        }
        json_file = "{}.json".format(user.get("id"))
        with open(json_file, mode="w", encoding="utf-8") as f:
            json.dump(json_data, f)

    except Exception as e:
        print(e)
