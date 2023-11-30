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
        return self.__dict__
    
    def __str__(self):
        """String representation of the BaseModel class"""
        return "{:s}-{:s}: {}".format(self.__class__.__name__, self.id,
                                      self.__dict__)


class Folder(StorageBase, Base):
    __tablename__ = 'folders'

    id = Column(CHAR(36), primary_key=True)
    title = Column(VARCHAR(256), nullable=False)
    parent_id = Column(CHAR(36), ForeignKey('folders.id', onupdate='CASCADE', ondelete='CASCADE'))

    parent_folder = relationship('Folder', remote_side=[id], backref='child_folders')


class User(StorageBase, Base):
    __tablename__ = 'users'

    id = Column(CHAR(36), primary_key=True)
    first_name = Column(VARCHAR(35), nullable=False)
    last_name = Column(VARCHAR(35), nullable=False)
    user_name = Column(VARCHAR(64), nullable=False)
    email = Column(VARCHAR(256), nullable=False)
    pfp_url = Column(VARCHAR(75), nullable=False)
    password = Column(VARBINARY(64), nullable=False)


class Task(StorageBase, Base):
    __tablename__ = 'tasks'

    id = Column(CHAR(36), primary_key=True)
    title = Column(VARCHAR(256), nullable=False)
    description = Column(VARCHAR(2048), nullable=False)
    status = Column(Enum('todo', 'doing', 'done', name='task_status'), default='todo')
    user_id = Column(CHAR(36), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))

    user = relationship('User', backref='tasks')


class Note(StorageBase, Base):
    __tablename__ = 'notes'

    id = Column(CHAR(36), primary_key=True)
    title = Column(VARCHAR(256), nullable=False)
    content_url = Column(VARCHAR(75), nullable=False)
    status = Column(Enum('pinned', 'normal', 'archived', 'trashed', name='note_status'), default='normal')
    user_id = Column(CHAR(36), ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))
    folder_id = Column(CHAR(36), ForeignKey('folders.id', onupdate='CASCADE', ondelete='CASCADE'))

    user = relationship('User', backref='notes')
    folder = relationship('Folder', backref='notes')


class NotesChangelog(StorageBase, Base):
    __tablename__ = 'notes_changelog'

    id = Column(CHAR(36), primary_key=True)
    time_stamp = Column(DATETIME, nullable=False)
    offset = Column(String(256), nullable=False)
    modification = Column(Enum('addition', 'deletion', name='modification_type'), nullable=False)
    modified_data = Column(VARCHAR(1024), nullable=False)
    note_id = Column(CHAR(36), ForeignKey('notes.id', onupdate='CASCADE', ondelete='CASCADE'))

    note = relationship('Note', backref='changelog')


class Project(StorageBase, Base):
    __tablename__ = 'projects'

    id = Column(CHAR(36), primary_key=True)
    title = Column(VARCHAR(256), nullable=False)


class ProjectNotes(StorageBase, Base):
    __tablename__ = 'project_notes_assoc'

    project_id = Column(CHAR(36), ForeignKey('projects.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    note_id = Column(CHAR(36), ForeignKey('notes.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)

    project = relationship('Project', backref='notes_assoc')
    note = relationship('Note', backref='projects_assoc')


class ProjectTasks(StorageBase, Base):
    __tablename__ = 'project_tasks_assoc'

    project_id = Column(CHAR(36), ForeignKey('projects.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    task_id = Column(CHAR(36), ForeignKey('tasks.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)

    project = relationship('Project', backref='tasks_assoc')
    task = relationship('Task', backref='projects_assoc')


class TaskTimings(StorageBase, Base):
    __tablename__ = 'task_timestamps'

    task_id = Column(CHAR(36), ForeignKey('tasks.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    start = Column(DATETIME, nullable=False)
    end = Column(DATETIME, nullable=False)

    task = relationship('Task', backref='timestamps')

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


# Replace 'sqlite' with 'mysql' in the connection string for MySQL
engine = create_engine('mysql://user:password@localhost/database_name')
Base.metadata.create_all(engine)
