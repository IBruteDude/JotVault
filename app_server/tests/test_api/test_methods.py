import requests as rs
from socket import gethostname, gethostbyname
from time import sleep

from db.db_classes import User, Note
from utils.db_instance_gen import class_generators, random_id

ip_address = gethostbyname(gethostname())

# the api request url prefix
api_url = f'http://172.22.112.189:5000/api/v1'

api_routes = {
    'User': '/users',
    'Folder': f'/{random_id(User)}/folders',
    'Task': f'/{random_id(User)}/tasks',
    'Note': f'/{random_id(User)}/notes',
    'NotesChangelog': f'/{random_id(User)}/notes/{random_id(Note)}/changes',
    'Project': f'/{random_id(User)}/projects',
}

for cls, route in api_routes.items():
	instance_dict = class_generators[cls]()

	print(f"<<<<{cls}>>>>\n\n")
	print(f"Original: {instance_dict}\n")

	old = len(rs.get(api_url + route).json())

	response = rs.post(api_url + route, json=instance_dict).json()
	for key, value in instance_dict.items():
		assert response[key] == value

	print(f"Response: {response}")

	new = len(rs.get(api_url + route).json())

	assert old + 1 == new
	sleep(2)

# instance_dict = class_generators['User']()

# print(f"Original: {instance_dict}\n\n")

# old = len(rs.get(f'{api_url}/users').json())

# print("Response: {}".format(
#     rs.post(f'{api_url}/users', json=instance_dict).json()
# ))

# new = len(rs.get(f'{api_url}/users').json())

# print("old: ", old)
# print("new: ", new)
