from faker import Faker
from sqlalchemy.exc import IntegrityError
import random

from db import classes, main_storage
from utils.db_instance_gen import class_generators

if __name__ == "__main__":
    for clsname, cls in classes.items():
        for _ in range(10):
            try:
                main_storage.new(cls(**class_generators[clsname]()))
                main_storage.save()
            except IntegrityError:
                main_storage.session.rollback()
            except Exception as e:
                main_storage.session.rollback()
                print('-' * 80)
                print(f'[{e.__class__.__name__}] - {e}')
    main_storage.close()
