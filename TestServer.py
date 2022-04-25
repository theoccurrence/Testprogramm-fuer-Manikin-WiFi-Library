import socket
import sys
import random
import time

startTime = time.time()

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverAddress = ('localhost', int(sys.argv[1]))
        print('Connecting to ' + str(serverAddress))
        sock.connect(serverAddress)
        messageID = 256
        for x in range(31):
            messageID += 1
            payload = int('000000'+bin(random.randint(0,3))[2:].zfill(2) \
                +'000000'+ bin(random.randint(0,3))[2:].zfill(2) \
                +'0000'+ bin(random.randint(0,15))[2:].zfill(4) \
                +'0000'+ bin(random.randint(0,15))[2:].zfill(4) \
                +'00000000' \
                +'0000'+ bin(random.randint(0,15))[2:].zfill(4) \
                +'0000'+ bin(random.randint(0,15))[2:].zfill(4) \
                +'0000'+ bin(random.randint(0,15))[2:].zfill(4),2)
            message = 'F' + hex(messageID)[2:] + '8' + hex(payload)[2:].zfill(16) + ', '
            print('Sende ' + message)
            sock.sendall(str(message).encode())
            
    except Exception as e:
        print("An error occurred!" +'\n' + str(e))

    time.sleep(1.0 - ((time.time() - startTime) % 1.0)) 