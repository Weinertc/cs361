#   Scoket Code made with the aid of https://realpython.com/python-sockets/
#   google image search code made with the help of https://pypi.org/project/Google-Images-Search/
#   inport the needed library > pip install Google-Images-Search
from google_images_search import GoogleImagesSearch
import socket

#   For Socket communication
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

#   For google image Seach using my API 
gis = GoogleImagesSearch('AIzaSyA6ylp4G_Q9VV3yTOeQGkUfi3PFQBkO24U', 'b265b111a4fe14e88')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Here is what the Client Sent: {data}")
            #   Now get the google images using google_image_search
            _search_params = {
                'q': data,
                'num': 1,
                'fileType': 'jpg|gif|png',
            }
            print("Lets download a photo")
            gis.search(search_params=_search_params, path_to_dir='imageDownloads')
            
            conn.sendall(str.encode(data))


