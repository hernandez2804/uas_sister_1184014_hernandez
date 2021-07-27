import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.connect((host,port))
print("Menyambungkan Ke server")
message = s.recv(1024)
message = message.decode()
print("Pesan Dari server : ", message)
while 1:
    message = s.recv(1024)
    message = message.decode()
    print("Server : ",message)
    new_message = input("Masukan Pesan :")
    new_message = str(new_message).encode()
    s.send(new_message)
    print("Pesan terkirim")
    message = s.recv(1024)
    message = message.decode()
    print("Client_2: ", message)
    
