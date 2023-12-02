from uuid import uuid4
from sqlalchemy import Column, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.types import String, CHAR, VARCHAR, VARBINARY, DATETIME, Enum
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class StorageBase:
    id = Column(CHAR(36), primary_key=True)

    def __init__(self, *args, **kwargs):
        self.id = uuid4()

    def dict_repr(self):
        "{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7f93f572b880>, 'last_name': 'Doe', 'user_name': 'john_doe', 'pfp_url': 'https://example.com/john_profile.jpg', 'id': '620ed68c-90e0-11ee-b4cd-00155db5b53c'"
        copy = self.__dict__.copy()
        del copy['_sa_instance_state']
        return copy
    
    def __str__(self):
        """String representation of the BaseModel class"""
        return "{:s}-{:s}: {}".format(self.__class__.__name__, self.id,
                                      self.__dict__)


class Folder(StorageBase, Base):
    __tablename__ = 'folders'

    id = Column(CHAR(36), primary_key=True)
    title = Column(VARCHAR(256), nullable=False)
    parent_id = Column(CHAR(36), ForeignKey('folders.id', onupdate='CASCADE', ondelete='CASCADE'))

    notes = relationship('Note', back_populates='folder', remote_side=[id])
    child_folders = relationship('Folder', back_populates='parent_folder', remote_side=[id])
    parent_folder = relationship('Folder', back_populates='child_folders', remote_side=[parent_id])


class User(StorageBase, Base):
    __tablename__ = 'users'

    id = Column(CHAR(36), primary_key=True)
    first_name = Column(VARCHAR(35), nullable=False)
    last_name = Column(VARCHAR(35), nullable=False)
    user_name = Column(VARCHAR(64), nullable=False)
    email = Column(VARCHAR(256), nullable=False)
    pfp_url = Column(VARCHAR(75), nullable=False)
    password = Column(VARBINARY(64), nullable=False)

    notes = relationship('Note', back_populates='user')
    tasks = relationship('Task', back_populates='user')
    projects = relationship('Project', back_populates='user')


class Task(StorageBase, Base):
    __tablename__ = 'tasks'

    id = Column(CHAR(36), primary_key=True)
    title = Column(VARCHAR(256), nullable=False)
    description = Column(VARCHAR(2048), nullable=False)
    status = Column(Enum('todo', 'doing', 'done', name='task_status'), default='todo')
    user_id = Column(CHAR(36), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))

    timestamps = relationship('TaskTimings', back_populates='task')
    user = relationship('User', back_populates='tasks') # or [user_id] idk


class Note(StorageBase, Base):
    __tablename__ = 'notes'

    id = Column(CHAR(36), primary_key=True)
    title = Column(VARCHAR(256), nullable=False)
    content_url = Column(VARCHAR(75), nullable=False)
    status = Column(Enum('pinned', 'normal', 'archived', 'trashed', name='note_status'), default='normal')
    user_id = Column(CHAR(36), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))
    folder_id = Column(CHAR(36), ForeignKey('folders.id', onupdate='CASCADE', ondelete='CASCADE'))

    user = relationship('User', back_populates='notes')
    folder = relationship('Folder', back_populates='notes')
    changelog = relationship('NotesChangelog', back_populates='note')


class NotesChangelog(StorageBase, Base):
    __tablename__ = 'notes_changelog'

    id = Column(CHAR(36), primary_key=True)
    time_stamp = Column(DATETIME, nullable=False)
    offset = Column(String(256), nullable=False)
    modification = Column(Enum('addition', 'deletion', name='modification_type'), nullable=False)
    modified_data = Column(VARCHAR(1024), nullable=False)
    note_id = Column(CHAR(36), ForeignKey('notes.id', onupdate='CASCADE', ondelete='CASCADE'))

    note = relationship('Note', back_populates='changelog')


class Project(StorageBase, Base):
    __tablename__ = 'projects'

    id = Column(CHAR(36), primary_key=True)
    title = Column(VARCHAR(256), nullable=False)
    user_id = Column(CHAR(36), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))

    user = relationship('User', back_populates='projects') # or [user_id] idk


class ProjectNotes(StorageBase, Base):
    __tablename__ = 'project_notes_assoc'

    project_id = Column(CHAR(36), ForeignKey('projects.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    note_id = Column(CHAR(36), ForeignKey('notes.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)

    # project = relationship('Project', back_populates='notes')
    # note = relationship('Note', back_populates='projects')


class ProjectTasks(StorageBase, Base):
    __tablename__ = 'project_tasks_assoc'

    project_id = Column(CHAR(36), ForeignKey('projects.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    task_id = Column(CHAR(36), ForeignKey('tasks.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)

    # project = relationship('Project', back_populates='tasks')
    # tasks = relationship('Task', back_populates='project', primaryjoin='Project.id == ProjectTasks.project_id')


class TaskTimings(StorageBase, Base):
    __tablename__ = 'task_timestamps'

    task_id = Column(CHAR(36), ForeignKey('tasks.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    start = Column(DATETIME, nullable=False)
    end = Column(DATETIME, nullable=False)

    task = relationship('Task', back_populates='timestamps')

classes = {
    'Folder': Folder,
    'User': User,
    'Task': Task,
    'Note': Note,
    'NotesChangelog': NotesChangelog,
    'Project': Project,
    'ProjectNotes': ProjectNotes,
    'ProjectTasks': ProjectTasks,
    'TaskTimings': TaskTimings
}
