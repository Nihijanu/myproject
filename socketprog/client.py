import socket
c=socket.socket()
c.connect((socket.gethostname(),1000))


c.close()