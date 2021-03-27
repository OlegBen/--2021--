import sqlite3

class DBManager:
    db = sqlite3.connect('messages.db')
    sql = db.cursor()

    def createDB(self):
        self.sql.execute("""CREATE TABLE IF NOT EXISTS messages (
            message TEXT,
            login TEXT
        )""")
        self.db.commit()

    def save(self, message, login):
        self.sql.execute(f"INSERT INTO messages VALUES (?, ?)", (message, login))

    def getAllMessages(self):
        self.sql.execute("SELECT message FROM messages")
        savedMessages = self.sql.fetchall()
        return savedMessages

    def cleanManager(self):
        self.sql.execute("DROP TABLE IF EXISTS messages")
        self.db.close()
