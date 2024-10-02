from test_todo_api import create_task,new_task_payload, list_tasks

payload = new_task_payload()
N = 3
'''
for i in range(N):
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
'''
create_task_response = create_task(payload)

print(create_task_response.json())