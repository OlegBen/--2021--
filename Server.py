import socket, time
from DBManager import DBManager

# Get host and port
host = socket.gethostbyname(socket.gethostname())
port = 8080

# Array where save all clients
clients = []

# Initial setup TCP/IP and start server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

# Data base manager
db = DBManager()

print("[ Server start ]")

# Flag that control server loop
quit = False

while not quit:
    try:
        # Listening clients
        data, addr = s.recvfrom(1024)
        
        # Add new client into clients list
        if addr not in clients:
            clients.append(addr)

        # Get current time
        currentTime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        # LOG on server
        print("[ " + addr[0] + " ] = [ " + str(addr[1]) + " ] = [ " + currentTime + " ]/", end="")

        log = data.decode("utf-8")
        print(log)

        # Check on new client ("Join")
        if "join chat" in log:
            # Get messages history
            savedMessages = db.getAllMessages()
            # Send saved messages to join client
            for message in savedMessages:
                s.sendto(message[0].encode("utf-8"), addr)

        # Send message all clients without sender
        for client in clients:
            if addr != client:
                s.sendto(data, client)

        # Save message on DB
        print("Here log: " + log)
        db.save(log, "Server")
    except:
        print("[ Server stop ]")
        # Clean DB then server stop
        db.cleanManager()
        quit = True

# Close server connection
s.close()