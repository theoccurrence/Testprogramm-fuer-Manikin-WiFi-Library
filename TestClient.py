import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost', int(sys.argv[1]))
print('Open TCP stream on port ' + str(serverAddress))
sock.bind(serverAddress)
sock.listen(1)

while True:
    fullMessage = ''
    print('Waiting for connection ...')
    connection, clientAddress = sock.accept()
    try:
        while True:
            data = connection.recv(16)
            #print('received: ' + str(data))
            fullMessage += str(data)[2:len(str(data))-1]
            if data:
                connection.sendall(data)
            else:
                break
    except WindowsError as e:
        if e.winerror == 10054:
            pass
        else:
            print("An error occurred!" +'\n' + str(e))
    except Exception as e:
        print("An error occurred!" +'\n' + str(e))
    finally:
        connection.close()
        counter = 0
        for message in fullMessage.split(', '):
            counter += 1
            if(counter < 32):
                print('Message ' + str(counter) + ': ' + message)