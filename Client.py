import socket, threading, time

# Flag that client quit from chat
shutdown = False
# Flag that client enter to chat
join = False

# Listening and get data from other client
def receving(name, sock):
    while not shutdown:
        try:
            while True:
                # Listening other clients
                data = sock.recv(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except:
            pass

# Setup client host and port
host = socket.gethostbyname(socket.gethostname())
port = 0

# Server addres
server = ('127.0.0.1', 8080)

# Initial setup TCP/IP and start client server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

# Set 0 to allow client leave from chat without errors
s.setblocking(0)

# Get client name
name = input("Name: ")

# Thread for client listener
rt = threading.Thread(target=receving, args=("RecvThread", s))
rt.start()

while shutdown == False:
    if join == False:
        # Client first enter in chat
        s.sendto(("[" + name + "] => join chat ").encode("utf-8"), server)
        join = True
    else:
        try:
            # Wait when client send message
            message = input("")
            if message != "":
                # Send client message to server
                s.sendto(("[" + name + "]: " + message).encode("utf-8"), server)
            
            time.sleep(0.2)
        except:
            s.sendto(("[" + name + "] <= left chat ").encode("utf-8"), server)
            shutdown = True

# Close client connection
rt.join()
s.close()
