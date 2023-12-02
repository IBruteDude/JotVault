from db.db_engine import DBStorage
from json import load

db_config = load(open('db/db_config.json'))

main_storage = DBStorage(**db_config)
main_storage.load()
