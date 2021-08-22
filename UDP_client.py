import socket

print('=====================================================================================================================')
print('This is a FIEK-UDP Client program.')
print('The client is ready to communicate with server.')
print('=====================================================================================================================')
print('')
print("Do you want to set the server and port you want to use?")
pergjigja=input().upper()
if(pergjigja=="YES"):
    print("Set the server name:")
    servername=input().lower()
    print("Set the port number")
    p=input()
    port=int(p)
else:
    servername='localhost'
    port=12000

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as clientsocket:
    while True:
        print('Operation (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, SQRT, IOSVERSION)?')
        var=input().upper().encode()
        if var=='':
            break
        clientsocket.sendto(var, (servername, port))
        message, address= clientsocket.recvfrom(128)
        print(repr(message.decode()))
