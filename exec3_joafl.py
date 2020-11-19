print("*** ONLY to play: Local IP ***")
import socket
IP1 = socket.gethostbyname(socket.gethostname()) # local IP adress of your computer
print(IP1)
a_file = open("exec3_localIP.txt", "w")
print(IP1, file=a_file)
a_file.close()


print("*** List of IPs ***")
ltIPs = ['127.0.0.1', '192.168.1.1', '192.168.1.2', '192.168.1.3', '255.255.255.0']
ltIPs_list = [x for x in ltIPs if '192.168.1.' in x]
print(ltIPs_list)
b_file = open("exec3_portList.txt", "w")
print(ltIPs_list, file=b_file)
b_file.close()


print("*** Numeros inteiros ***")
# Python3 Program to Create list  
# with integers within given range  
  
def createList(r1, r2): 
    return [item for item in range(r1, r2+1)] 
      
# Driver Code 
r1, r2 = 1, 1024
listInteger = createList(r1, r2)
print("see the file")
b_file = open("exec3_ipList.txt", "w")
print(listInteger, file=b_file) 
b_file.close()