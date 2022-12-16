import socket
s=socket.socket()
s.bind((socket.gethostname(),1000))
s.listen()
while True:
    c,add=s.accept()
    print(add)
    c.send(bytes("hi client","utf-8").decode())

    s.close()
