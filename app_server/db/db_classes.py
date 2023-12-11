from uuid import uuid4
import datetime as dt

from sqlalchemy import Column, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.types import String, CHAR, VARCHAR, VARBINARY, DATETIME, Enum, TEXT
from sqlalchemy.orm import declarative_base, relationship

from utils.hash_algo import hash_password

Base = declarative_base()

class StorageBase:
    db_attrs = ()
    def __init__(self, *args, **kwargs):
        if kwargs.get('id'):
            del kwargs['id']
        if kwargs:
            self.__dict__.update(kwargs)

    def dict_repr(self):
        copy = self.__dict__.copy()
        del copy['_sa_instance_state']
        return copy

    def update(self, dic):
        from db import main_storage
        if dic.get('id') is not None:
            del dic['id']
        for key in self.__dict__:
            value = dic.get(key)
            if key is not None:
                setattr(self, key, value)
        main_storage.save()

    def __str__(self):
        """String representation of the BaseModel class"""
        return "{:s}-{:s}: {}".format(self.__class__.__name__, self.id,
                                      self.__dict__)


class Folder(StorageBase, Base):
    __tablename__ = 'folders'

    db_attrs = ('id', 'title', 'parent_id', 'user_id')

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    title = Column(VARCHAR(256), nullable=False)
    parent_id = Column(CHAR(36), ForeignKey('folders.id', onupdate='CASCADE', ondelete='CASCADE'))
    user_id = Column(CHAR(36), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))

    user = relationship('User', back_populates='folders')
    notes = relationship('Note', back_populates='folder', remote_side=[id])
    child_folders = relationship('Folder', back_populates='parent_folder', remote_side=[id])
    parent_folder = relationship('Folder', back_populates='child_folders', remote_side=[parent_id])


class User(StorageBase, Base):
    __tablename__ = 'users'

    db_attrs = ('id', 'first_name', 'last_name',
                'user_name', 'email', 'pfp_url', 'password')
    def __init__(self, *args, **kwargs):
        ''' Ensure the user's password is hashed '''
        super().__init__(self, *args, **kwargs)
        self.password = hash_password(self.password)

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    first_name = Column(VARCHAR(35), nullable=False)
    last_name = Column(VARCHAR(35), nullable=False)
    user_name = Column(VARCHAR(64), nullable=False)
    email = Column(VARCHAR(256), nullable=False)
    pfp_url = Column(VARCHAR(256))
    password = Column(VARBINARY(64), nullable=False)

    notes = relationship('Note', back_populates='user')
    tasks = relationship('Task', back_populates='user')
    folders = relationship('Folder', back_populates='user')
    projects = relationship('Project', back_populates='user')


class Task(StorageBase, Base):
    __tablename__ = 'tasks'

    db_attrs = ('id', 'title', 'description',
                'status', 'color', 'user_id', 'project_id')

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    title = Column(VARCHAR(256), nullable=False)
    description = Column(VARCHAR(2048), nullable=False)
    status = Column(Enum('todo', 'doing', 'done', name='task_status'), default='todo')
    color = Column(CHAR(6), default='FFFFFF')
    start = Column(DATETIME, nullable=False, default=dt.datetime.now)
    end = Column(DATETIME, nullable=False, default=dt.datetime.now)

    user_id = Column(CHAR(36), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))
    project_id = Column(CHAR(36), ForeignKey('projects.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)

    project = relationship('Project', back_populates='tasks', uselist=False)
    user = relationship('User', back_populates='tasks')

class Note(StorageBase, Base):
    __tablename__ = 'notes'

    db_attrs = ('id', 'title', 'content', 'status',
                'color', 'user_id', 'folder_id', 'project_id')

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    title = Column(VARCHAR(256), nullable=False)
    content = Column(TEXT, nullable=False)
    status = Column(Enum('pinned', 'normal', 'archived', 'trashed', name='note_status'), default='normal')
    color = Column(CHAR(6), default='FFFFFF')
    user_id = Column(CHAR(36), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))
    folder_id = Column(CHAR(36), ForeignKey('folders.id', onupdate='CASCADE', ondelete='CASCADE'))
    project_id = Column(CHAR(36), ForeignKey('projects.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)

    user = relationship('User', back_populates='notes')
    folder = relationship('Folder', back_populates='notes')
    changelog = relationship('NotesChangelog', back_populates='note')
    project = relationship('Project', back_populates='notes', uselist=False)


class NotesChangelog(StorageBase, Base):
    __tablename__ = 'notes_changelog'

    db_attrs = ('id', 'time_stamp', 'offset',
                'modification', 'modified_data', 'note_id')

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    time_stamp = Column(DATETIME, nullable=False)
    offset = Column(String(256), nullable=False)
    modification = Column(Enum('addition', 'deletion', name='modification_type'), nullable=False)
    modified_data = Column(VARCHAR(1024), nullable=False)
    note_id = Column(CHAR(36), ForeignKey('notes.id', onupdate='CASCADE', ondelete='CASCADE'))

    note = relationship('Note', back_populates='changelog')


class Project(StorageBase, Base):
    __tablename__ = 'projects'

    db_attrs = ('id', 'title', 'user_id')

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    title = Column(VARCHAR(256), nullable=False)
    user_id = Column(CHAR(36), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))

    user = relationship('User', back_populates='projects')
    notes = relationship('Note', back_populates='project')
    tasks = relationship('Task', back_populates='project')

classes = {
    'Folder': Folder,
    'User': User,
    'Task': Task,
    'Note': Note,
    'NotesChangelog': NotesChangelog,
    'Project': Project,
}
