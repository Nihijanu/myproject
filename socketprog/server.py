import socket
s=socket.socket()
print("connecting")
s.bind((socket.gethostname(),1000))
s.listen(3)
print("waiting for connection")
while True:
    clie, add=s.accept()
    print(add)
    clie.send(bytes("hi client","utf-8"))
    clie.close()
