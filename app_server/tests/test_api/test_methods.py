import requests as rs
import socket as sok
from time import sleep
from datetime import datetime
import random

from db import main_storage
from db.db_classes import User, Note, Task, Project, Folder, classes
from utils.db_instance_gen import class_generators, random_id

ipaddress = '172.22.112.189' # rs.get('https://api.ipify.org').text

# the api request url prefix
api_url = f'http://{ipaddress}:5000/api/v1'

########## The complete list of available api routes ##########
'/users/<user_id>'
'/<user_id>/folders/<folder_id>'
'/<user_id>/tasks/<task_id>'
'/<user_id>/tasks/todo'
'/<user_id>/tasks/doing'
'/<user_id>/tasks/done'
'/<user_id>/notes/<note_id>'
'/<user_id>/notes/<note_id>/content'
'/<user_id>/notes/<note_id>/changes/<change_id>'
'/<user_id>/notes/<note_id>/changes/<change_id>/content'
'/<user_id>/notes/normal'
'/<user_id>/notes/archived'
'/<user_id>/notes/trashed'
'/<user_id>/notes/pinned'
'/<user_id>/projects/<project_id>'
'/<user_id>/projects/<project_id>/tasks/<task_id>'
'/<user_id>/projects/<project_id>/notes/<note_id>'

api_routes = [
    ('User', f'/users/{random_id(User)}'),
    ('Folder', (lambda folder:
        f"/{folder['user_id']}/folders/{folder['id']}")(random_id(Folder, True))),
    ('Task', (lambda task:
        f"/{task['user_id']}/tasks/{task['id']}")(random_id(Task, True))),
    ('Note', (lambda note:
        f"/{note['user_id']}/notes/{note['id']}")(random_id(Note, True))),
    ('Project', (lambda project:
        f"/{project['user_id']}/projects/{project['id']}")(random_id(Project, True))),
    ('Task', (lambda task:
        f"/{task['user_id']}" +
        (f"/projects/{task['project_id']}" if task.get('project_id') else "") +
        f"/tasks/{task['id']}")(random_id(Task, True))),
    ('Note', (lambda note:
        f"/{note['user_id']}" +
        (f"/projects/{note['project_id']}" if note.get('project_id') else "") +
        f"/notes/{note['id']}")(random_id(Note, True))),
]

readonly_api_routes = [
    ('Note', f'/{random_id(User)}/notes/normal'),
    ('Note', f'/{random_id(User)}/notes/archived'),
    ('Note', f'/{random_id(User)}/notes/trashed'),
    ('Note', f'/{random_id(User)}/notes/pinned'),
    ('Task', f'/{random_id(User)}/tasks/todo'),
    ('Task', f'/{random_id(User)}/tasks/doing'),
    ('Task', f'/{random_id(User)}/tasks/done'),

    # WATCH OUT FOR 5WAZEEK
    ('NoteChanges', (lambda note:
        f"/{note['user_id']}/notes/{note['id']}/changes")(random_id(Note, True))),
    ('Note', (lambda note:
        f"/{note['user_id']}/notes/{note['id']}/content")(random_id(Note, True))),
    # ('NoteChangelog', (lambda note:
    #     f"/{note.user_id}/notes/{note.id}/changes/{random.choice(note.changelog).id}/content")(main_storage.get(Note, random_id(Note))))
]

def test_get_post(cls, route):
    instance_dict = class_generators[cls]()
    if cls == 'Task':
        instance_dict['start'] = str(instance_dict['start'])
        instance_dict['end'] = str(instance_dict['end'])
    print('-' * 80)
    print(f"{cls}")
    print('-' * 80)
    print(f"Original: {instance_dict}\n")
    remote_url = api_url + route[:-37]
    print(f"request url: {remote_url}\n")
    old = len(rs.get(remote_url).json())
    response = rs.post(remote_url, json=instance_dict).json()
    print(f"Response: {response}\n")
    for key, value in instance_dict.items():
        if key[-2:] != 'id':
            assert response[key] == value
    if cls != 'User':
        remote_url = f"{api_url}/{response.get('user_id')}{route[37:-37]}/{response['id']}"
    else:
        remote_url = api_url + route[:-37] + '/' + response['id']
    print(remote_url, end='\n\n')
    remote_obj = rs.get(remote_url).json()
    print(f"Remote: {remote_obj}\n\n", flush=True)
    assert not remote_obj.get('error')
    new = len(rs.get(api_url + route).json())
    print(f'old length: {old}\nnew length: {new}\n')


def test_put_delete(cls, route):
    print('-' * 80)
    print(f"{cls}")
    print('-' * 80)

    url = api_url + route

    print(f"request url: {url}\n")
    instance = class_generators[cls]()
    original = main_storage.get(classes[cls], route[-36:])
    print(f'Original: {original}\n', flush=True)
    key, value = random.choice(list(filter(lambda tup: tup[0][-2:] != 'id', instance.items())))
    if type(value) is datetime:
        value = str(value)
    print(f'Change:- {key} : {value}\n', flush=True)
    response = rs.put(url, json={key: value}).json()
    print(f'Response: {response}\n', flush=True)
    if response.get('error') is None:
        if response[key] != value:
            print(f'response[key] = {response[key]}, value = {value}', flush=True)
    response = rs.delete(url).json()
    print(f'Delete Response: {response}\n', flush=True)

for cls, route in api_routes:
    # try:
        test_get_post(cls, route)
        test_put_delete(cls, route)
    # except Exception as e:
    #     print('-' * 80)
    #     print(f"[{e.__class__.__name__}]: {e}")
    #     print('-' * 80)
    #     exit(1)
