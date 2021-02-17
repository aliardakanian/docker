import socket
s=socket.socket()
ip=socket.gethostbyname("localhost")
print("server ip=",ip)
port=9999
s.bind((ip,port))
s.listen()
print ("wait for client")
c,addr=s.accept()
print ("client added")
print("client address=",addr)
c_msg=" "
while c_msg!="q":
	msg=input("please write your message to client")
	c.send(msg.encode())
	print("your client message:",c.recv(1024).decode())
c.close()
