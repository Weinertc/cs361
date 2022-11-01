My code does require that GoogleImageSearch is installed via "pip install Google-Images-Search" 
more info on the libary found here https://pypi.org/project/Google-Images-Search/

To REQUEST data from the microservice: Send data string to service, via s.sendall(str.encode(userInput))

Example: 
userInput = input("What kind of Car would you like to see (year, model, color): ")
**user enters: "2012 Camery" 

##   Send the car information via socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(str.encode(userInput)) -> request sent to server


To RECEIVE data from the microservice: the photo shouldimmediately download to imageDownloads folder in current directory. 
(a folder should be created if one is not already present)
I also did include a simple response from the server to validate that the message was recived correctly, 
that can be checked with a simple "data  = s.recv(1024).decode()"

