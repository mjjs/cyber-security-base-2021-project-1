from message import Message
from user import User

class MessageStore:
    def __init__(self, connection):
        self._connection = connection

    def get_messages(self):
        cursor = self._connection.cursor()
        rows = cursor.execute("SELECT * FROM messages;")

        messages = [
                Message(message_id, title, body, User(user_id, "", False))
                for (message_id, title, body, user_id) in rows
                ]

        self._connection.commit()
        cursor.close()

        return messages

    def add_message(self, title, body, user):
        cursor = self._connection.cursor()
        cursor.execute(f"INSERT INTO messages(title, body, user_id) VALUES('{title}', '{body}', '{user.get_id()}')")

        self._connection.commit()
        cursor.close()

        return Message(cursor.lastrowid, title, body, user)

    def delete_message(self, message):
        cursor = self._connection.cursor()
        cursor.execute(f"DELETE FROM messages WHERE id = '{message.id}'")

        self._connection.commit()
        cursor.close()
