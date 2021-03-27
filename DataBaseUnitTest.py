from DBManager import DBManager

db = DBManager()

db.createDB()
db.save("Test message", "Oleg")
messages = db.getAllMessages()

for message in messages:
    if message[0] == "Test message":
        print(True)
    else:
        print(False)

db.cleanManager()