from messagestore import MessageStore
from userstore import UserStore
from sqlite3 import connect
from flask import g

DEFAULT_DATABASE_NAME = "db.sqlite3"
DATABASE_INIT_FILE = "create_tables.sql"

def get_db():
    db = getattr(g, "_database", None)

    if db is None:
        database = Database("db.sqlite3")

        db = g._database = database

    return db

class Database:
    def __init__(self, dbname = DEFAULT_DATABASE_NAME):
        self._db = connect(dbname)
        self.userstore = UserStore(self._db)
        self.messagestore = MessageStore(self._db)

    def close(self):
        self._db.close()

    def initialize(self):
        print("Initializing database")
        create_tables_sql_file = open(DATABASE_INIT_FILE, "r")
        sql = create_tables_sql_file.read()
        create_tables_sql_file.close()

        cursor = self._db.cursor()
        cursor.executescript(sql)
        self._db.commit()
        cursor.close()
        print("Database initialized")
