import sqlalchemy as sa
from db_classes import (
    Base, classes,
    Folder, User, Task, Note, NotesChangelog,
    Project, ProjectNotes, ProjectTasks, TaskTimings
)

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def __init__(self, *args, **kwargs):
        if not (
                kwargs.get('user') and kwargs.get('pwd') and\
                kwargs.get('host') and kwargs.get('db')
            ):
            raise KeyError("missing db url parameters")
        self.__engine = create_engine(
            "mysql+mysqldb://{user}:{pwd}@{host}/{db}".format(**kwargs))

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def load(self):
        """loads all stored objects from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """discard the currently open session"""
        self.__session.remove()

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def get(self, cls, id):
        """find an object based on its class and id if found"""
        return self.__session.query(cls).get(id)

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def all(self, cls=None):
        """create a dictionary of models currently in database"""
        queried_dict = {}

        if cls is None:
            for cls in classes.values():
                db_query = self.__session.query(cls).all()
                for record in db_query:
                    queried_dict[f'{cls.__name__}.{record.id}'] = record
            return queried_dict

        db_query = self.__session.query(cls).all()
        for record in db_query:
            queried_dict[f'{cls.__name__}.{record.id}'] = record
        return queried_dict

    def count(self, cls=None):
        """count the stored instances of a given class, or of all classes"""
        if cls is not None:
            return self.__session.query(cls).count()
        total = 0
        for cls in classes.values():
            total += self.__session.query(cls).count()
        return total
