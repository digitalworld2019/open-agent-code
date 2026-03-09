import sqlite3
import os

class UserService:

    def __init__(self, db_path="users.db"):
        self.conn = sqlite3.connect(db_path)

    def login(self, username, password):
        cursor = self.conn.cursor()

        # ❌ SQL Injection vulnerability
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

        cursor.execute(query)
        user = cursor.fetchone()

        if user:
            return True
        return False

    def backup_database(self, backup_file):
        # ❌ Command Injection vulnerability
        cmd = f"cp users.db {backup_file}"
        os.system(cmd)

    def create_user(self, username, password):
        cursor = self.conn.cursor()

        # ❌ Plaintext password storage
        cursor.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, password)
        )
        self.conn.commit()