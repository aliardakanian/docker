import socket
s=socket.socket()
ip="localhost"
port=9999
s.connect((ip,port))
print ("connected! welcome")
while True:
    print("server message=",s.recv(1024).decode())
    msg=input("your client message >>>")
    s.send(msg.encode())