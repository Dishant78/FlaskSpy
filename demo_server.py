import socket

HOST = "0.0.0.0"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"[*] Listening on {HOST}:{PORT}")

while True:
    client, addr = server.accept()
    print(f"[*] Accepted connection from: {addr}")

    request = client.recv(1024)
    print(f"[*] Received: {request}")

    response = """\
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Server is working!</h1>
"""
    client.sendall(response.encode())  
    client.close()