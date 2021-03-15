import socket, time

# Get host and port
host = socket.gethostbyname(socket.gethostname())
port = 8080

# Array where save all clients
clients = []

# Initial setup TCP/IP and start server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

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
        print(data.decode("utf-8"))

        # Send message all clients without sender
        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        print("[ Server stop ]")
        quit = True

# Close server connection
s.close()