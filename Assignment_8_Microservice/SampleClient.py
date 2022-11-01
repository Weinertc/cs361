#   Using modified code from https://realpython.com/python-sockets/

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

userInput = input("What kind of Car would you like to see (year, model, color): ")

#   Send the car information via socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Sending Request... ")
    s.sendall(str.encode(userInput))
    data = s.recv(1024).decode()

print(f"Received from the server: {data!r}")