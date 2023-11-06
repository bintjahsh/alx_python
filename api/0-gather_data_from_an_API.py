import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    employee_tasks = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id))
    data1 = employee.text
    pjson = json.loads(data1)
    data2 = employee_tasks.text
    pjson1 = json.loads(data2)

    task_count = 0
    task_complete = 0
    employee_name = pjson['name']

    for item in pjson1:
        # Count the tasks in todo list and check if completed or not
        if 'title' in item:
            task_count += 1 
        if (item['completed'] == True):
            task_complete += 1

    print("Employee {} is done with tasks({}/{}):".format(employee_name, task_complete, task_count))

    for item in pjson1:
        # Print all completed tasks
        if (item['completed'] == True):
            tasks_name = item['title']
            print("\t {}".format(tasks_name))
