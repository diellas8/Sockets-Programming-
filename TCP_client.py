import socket

print('=====================================================================================================================')
print('This is a FIEK-TCP Client program')
print('The client is ready to communicate with server.')
print('=====================================================================================================================')
print('')
print("Do you want to set the server and port you want to use?")
answer=input().upper()
if(answer=="YES"):
    print("Set the server name:")
    servername=input().lower()
    print("Set the port number")
    p=input()
    port=int(p)
else:
    servername='localhost'
    port=13000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as clientsocket:
    clientsocket.connect((servername,port))
    while True:
        print('Operation (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, SQRT, IOSVERSION)?')
        var=input().upper().encode()
        if var=='':
            break
        clientsocket.sendall(var)
        r=clientsocket.recv(128).decode()
        print(repr(r))

