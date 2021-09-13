#!/usr/bin/python3
"""Fetches a REST Api
Records all tasks that are owned by this employee to a csv file
"""
import csv
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
        csv_name = "{}.csv".format(user.get("id"))
        with open(csv_name, mode="w", encoding="utf-8",
                  newline='') as data_file:
            csv_writer = csv.writer(data_file)
            for todo in user_todos:
                row = [
                    user.get("id"),
                    user.get("username"),
                    todo.get("completed"),
                    todo.get("title")
                ]
                csv_writer.writerow(row)

    except Exception as e:
        print(e)
