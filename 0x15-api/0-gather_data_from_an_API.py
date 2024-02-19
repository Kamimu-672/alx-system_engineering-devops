#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""


from requests import get
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(sys.argv[1])).json()
    todos = get(url + "users/{}/todos".format(sys.argv[1])).json()

    todos_num = len(todos)
    todos_complete = len([todo for todo in todos if todo.get("completed")])
    name = user.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todos_complete, todos_num))
    for todo in todos:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
