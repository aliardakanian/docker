import socket
s=socket.socket()
ip=socket.gethostbyname("localhost")
print("client ip==",ip)
port=9999
s.connect((ip,port))
print ("connected! welcome")
s_msg=" "
while s_msg!="q":
        s_msg=s.recv(1024).decode()
        print("server message:",s_msg)
        msg=input("please write client message to server: ")
        s.send(msg.encode())
s.close()
