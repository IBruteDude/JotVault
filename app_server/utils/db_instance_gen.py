from faker import Faker
import random

from db import main_storage
from db.db_classes import *

fake = Faker()

def random_id(cls):
    ''' select a random instance's id of type cls '''
    objs = main_storage.all(cls)
    if len(objs) != 0:
        return random.choice(objs)['id']

class_generators = {
    "User": lambda: {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "user_name": fake.user_name(),
        "email": fake.free_email(),
        "pfp_url": fake.image_url(),
        "password": fake.password(),
    },
    "Folder": lambda: {
        "title": fake.sentence()[:256],

        "user_id": random_id(User),
        "parent_id": random_id(Folder),
    },
    "Task": lambda: {
        "title": fake.sentence()[:256],
        "description": fake.paragraph()[:2048],
        "status": random.choice(["todo", "doing", "done"]),
        "color": fake.safe_hex_color()[1:],
        "start": fake.date_time(),
        "end": fake.date_time(),

        "user_id": random_id(User),
        "project_id": random_id(Project),
    },
    "Note": lambda: {
        "title": fake.sentence()[:256],
        "content": fake.text(),
        "status": random.choice(["pinned", "normal", "archived", "trashed"]),
        "color": fake.safe_hex_color()[1:],

        "user_id": random_id(User),
        "folder_id": random_id(Folder),
        "project_id": random_id(Project),
    },
    "NotesChangelog": lambda: {
        "time_stamp": fake.date_time(),
        "offset": random.randint(0, 1024),
        "modification": random.choice(["addition", "deletion"]),
        "modified_data": fake.text()[:1024],

        "note_id": random_id(Note),
    },
    "Project": lambda: {
        "title": fake.sentence()[:256],

        "user_id": random_id(User),
    },
}
