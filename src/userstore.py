from user import User

class UserStore:
    def __init__(self, connection):
        self._connection = connection

    def add_user(self, username, password, is_admin):
        cursor = self._connection.cursor()
        cursor.execute(f"INSERT INTO users(username, password, is_admin) VALUES('{username}', '{password}', '{is_admin}')")

        self._connection.commit()
        cursor.close()

        return User(cursor.lastrowid, username, is_admin)

    def get_users(self):
        cursor = self._connection.cursor()
        rows = cursor.execute("SELECT * FROM users;")
        self._connection.commit()

        users = [User(user_id, username, is_admin) for (user_id, username, _, is_admin) in rows]

        cursor.close()

        return users

    def delete_user_by_id(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute(f"DELETE FROM users WHERE id = '{user_id}'")

        self._connection.commit()
        cursor.close()

    def switch_admin_status(self, user_id):
        user = self.get_user_by_id(user_id)

        new_val = "False" if user.is_admin else "True"

        cursor = self._connection.cursor()
        cursor.execute(f"UPDATE users SET is_admin = {new_val} WHERE id = '{user_id}'")

        self._connection.commit()
        cursor.close()

    def get_user_by_id(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")

        self._connection.commit()
        row = cursor.fetchone()

        if row is None:
            cursor.close()
            return None

        (user_id, username, _, is_admin) = row

        cursor.close()

        return User(user_id, username, is_admin)

    def get_user_by_username_and_password(self, username, password):
        cursor = self._connection.cursor()
        cursor.execute(
                f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"
                )

        row = cursor.fetchone()
        self._connection.commit()

        if row is None:
            cursor.close()
            return None

        cursor.close()

        return User(row[0], row[1], row[3])
