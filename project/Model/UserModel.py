from Database.Database import Database
import re

class User:

    _table = "User"

    name: str
    username: str
    password: str
    email: str
    errors: dict = {}

    def __init__(self, name, username, password, email):
        self.name = "" if name == None else name.strip()
        self.username = "" if username == None else username.strip()
        self.password = "" if password == None else password
        self.email = "" if email == None else email.strip()

    def create(self) -> bool:

        try:

            database = Database()

            database.cursor.execute(f"INSERT INTO {self._table} (name, username, password, email) VALUES ('{self.name}', '{self.username}', '{self.password}', '{self.email}')")

            database.connection.commit()

            return True

        except Exception as errors:

            database.connection.rollback()

            database.connection.close()

            if "UNIQUE constraint failed" in errors.args[0]:

                if "username" in errors.args[0]:

                    self.errors.update(username="Username already exists.")

                if "email" in errors.args[0]:

                    self.errors.update(email="E-mail already exists.")

            else:

                self.errors.update(database=errors)

            raise ValueError(self.errors)

    def read(self) -> list:

        database = Database()

        database.cursor.execute(f"SELECT * FROM {self._table}")

        rows = database.cursor.fetchall()

        return rows

    def validateUser(self, validations: list = [], args: dict = {}):

        self.errors = {}

        if (not validations) == False:

            if "username" in validations or "all" in validations:

                self.validateUsername()

            if "email" in validations or "all" in validations:

                self.validateEmail()

            if "password" in validations or "all" in validations:

                confirmPassword = args.get("confirmPassword", False)

                self.validatePassword(confirmPassword)

        if (not self.errors) == False:

            raise ValueError(self.errors)

        return True


    def validateUsername(self) -> bool:

        pattern = r'^[^\s]{6,}$'

        if self.username == "":
            self.errors.update(username="Username is required.")
            return False

        elif len(self.username.strip()) < 6:
            self.errors.update(username="Username is too short. It must be at least 6 characters.")
            return False

        elif re.match(pattern, self.username) is None:
            self.errors.update(username="Username is not valid.")
            return False

        return True

    def validateEmail(self) -> bool:

        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if self.email == "":
            self.errors.update(email="E-mail is required.")
            return False

        elif re.match(pattern, self.email) is None:
            self.errors.update(email="E-mail is not valid.")
            return False

        return True

    def validatePassword(self, confirmPassword: str | bool = False) -> bool:

        if confirmPassword != False:

            if (confirmPassword == None or confirmPassword == "") and (self.password == ""):
                self.errors.update(password="Passwords are required.")
                return False

            elif confirmPassword != self.password :
                self.errors.update(password="Passwords don't match.")
                return False

        elif (self.password == ""):
            self.errors.update(password="Password is required.")
            return False

        return True
