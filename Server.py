import socket
import datetime
from time import sleep
import time
import sys
import unittest
from test.support import HOST
import threading

def main():
    print("Server Side.")
    SOCKET = socket.socket()
    HOST = socket.gethostname()
    IP = socket.gethostbyname(HOST)
    port = 1234
    SOCKET.bind((HOST, port))
    name = input('Enter name: ')
    SOCKET.listen(5)
    print("Open for new connection.")
    connection, ADDRESS = SOCKET.accept()
    for i in range(21):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        sleep(0.25)
    client_name = connection.recv(1024)
    client_name = client_name.decode()
    print(str(datetime.datetime.now()))
    print('connected to: ' + client_name)
    print('You can Press Exit to leave the chat at anytime.')
    connection.send(name.encode())
    while True:
        message = input('ME: ')
        if message == "Exit":
            last_message = "The other party left the Chat\n Press Exit to leave the chat room"
            connection.send(last_message.encode())
            print(str(datetime.datetime.now()))
            connection.close()
            print("\n")
            break
        connection.send(message.encode())
        message = connection.recv(1024)
        message = message.decode()
        print(client_name, ';', message)
        print("                 " + str(datetime.datetime.now()))

class CreationTestCase(unittest.TestCase):
    
    def setUp(self):
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def testObjectCreation(self):
        self.assertEqual(self.SOCKET.gettimeout(), None,"timeout not disabled by default")


if __name__ == "__main__":
    main()
    