import requests as rs
from socket import gethostname, gethostbyname

from utils.db_instance_gen import class_generators, hash_password

ip_address = gethostbyname(gethostname())

# the api request url prefix
api_url = f'http://172.22.112.189:5000/api/v1'
instance_dict = class_generators['User']()

api_routes = {
    'Folder': '/<user_id>/folders',
    'User': '/users',
    'Task': '/<user_id>/tasks',
    'Note': '/<user_id>/notes',
    'NotesChangelog': '/<user_id>/notes/<note_id>/changes',
    'Project': '/<user_id>/projects',
    'ProjectNotes': '/<user_id>/projects/<project_id>/notes',
    'ProjectTasks': '/<user_id>/projects/<project_id>/tasks',
    # 'TaskTimings': ''
}

print(f"Original: {instance_dict}")

old = len(rs.get(f'{api_url}/users').json())

print("Response: {}".format(
    rs.post(f'{api_url}/users', json=instance_dict).json()
))

new = len(rs.get(f'{api_url}/users').json())

print("old: ", old)
print("new: ", new)
