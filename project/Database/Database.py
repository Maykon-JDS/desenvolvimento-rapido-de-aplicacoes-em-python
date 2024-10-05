import sqlite3

class Database:

    def __init__(self):
        self.connection = sqlite3.connect("project/rad.db")
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()