from faker import Faker
import random

from db import main_storage
from db.db_classes import *

fake = Faker()

def random_id(cls, return_obj=False):
    ''' select a random instance's id of type cls '''
    objs = main_storage.all(cls)
    if len(objs) != 0:
        obj = random.choice(objs)
        if return_obj:
            return obj
        return obj['id']

class_generators = {
    "User": lambda: {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "user_name": fake.user_name(),
        "email": fake.free_email(),
        "pfp_url": fake.image_url(),
        "password": fake.password(),
    },
    "Folder": lambda: (lambda folder: {
        "title": fake.sentence()[:256],

        "user_id": folder['user_id'],
        "parent_id": folder['parent_id'],
    })(random_id(Folder, True)),
    "Task": lambda: (lambda project: {
        "title": fake.sentence()[:256],
        "description": fake.paragraph()[:2048],
        "status": random.choice(["todo", "doing", "done"]),
        "color": fake.safe_hex_color()[1:],
        "start": str(fake.date_time()),
        "end": str(fake.date_time()),

        "user_id": project['user_id'],
        "project_id": project['id'],
    })(random_id(Project, True)),
    "Note": lambda: (lambda project: {
        "title": fake.sentence()[:256],
        "content": fake.text(),
        "status": random.choice(["pinned", "normal", "archived", "trashed"]),
        "color": fake.safe_hex_color()[1:],

        "user_id": project['user_id'],
        "folder_id": (
            lambda folders:
                random.choice(folders).id if len(folders) > 0 else None
            )(main_storage.get(User, project['user_id']).folders),
        "project_id": project['id'],
    })(random_id(Project, True)),
    "NotesChangelog": lambda: {
        "time_stamp": str(fake.date_time()),
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
