
import socket, time

# Get host and port
host = socket.gethostbyname('localhost')
port = 1502

# Array where save all clients
clients = []

# Initial setup and start server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print("Server start")

# Close server connection
s.close()

print("Server stop")