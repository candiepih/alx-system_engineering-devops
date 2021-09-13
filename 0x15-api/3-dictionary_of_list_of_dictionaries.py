#!/usr/bin/python3
"""Fetches a REST Api
Records all tasks from all employees
"""
import json
import requests


user_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

user_response = requests.get(user_url)
todos_response = requests.get(todos_url)

try:
    users = user_response.json()
    todos = todos_response.json()

    data = {}
    for user in users:
        user_id = user.get("id")
        user_todos = list(filter(lambda todo: (todo.get("userId") == user_id),
                                 todos))
        tasks = list(map(lambda todo: {
                             "username": user.get("username"),
                             "task": todo.get("title"),
                             "completed": todo.get("completed"),
                         },
                         user_todos))
        data[user_id] = tasks

    json_file = "todo_all_employees.json"
    with open(json_file, mode="w", encoding="utf-8") as f:
        json.dump(data, f)

except Exception as e:
    print(e)
