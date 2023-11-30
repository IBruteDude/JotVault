from db_engine import DBStorage
from json import load

db_config = load(open('db_config.json'))

main_storage = DBStorage(**db_config)
main_storage.load()
