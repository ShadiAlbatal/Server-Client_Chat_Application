import socket
import datetime
import time
import sys

def main():
    print("Client Side.")
    SOCKET = socket.socket()
    HOST = socket.gethostname()
    IP = socket.gethostbyname(HOST)
    name = input('Enter name: ')
    PORT = 1234
    SOCKET.connect((IP, PORT))
    print("Trying to connect...")
    SOCKET.send(name.encode())
    server_name = SOCKET.recv(1024)
    server_name = server_name.decode()
    print("Connecting....")
    for i in range(21):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        time.sleep(0.25)
    print("\nConnection Established.")
    print('Remember: You can Press Exit to leave the chat at anytime.')
    print("--------------------------------------------")
    print('Connected with: ' + server_name)
    print(str(datetime.datetime.now())+ "\n")
    while True:
        message = SOCKET.recv(1024)
        message = message.decode()
        print(server_name, ":", message)
        print(str(datetime.datetime.now())+ "\n")
        message = input("ME: ")
        print(str(datetime.datetime.now())+ "\n")
        if message == "Exit":
            last_message = "The other party left the Chat\n Press Exit to leave the chat room"
            SOCKET.send(last_message.encode())
            print(str(datetime.datetime.now()))
            SOCKET.close()
            print("\n")
            break
        SOCKET.send(message.encode())


if __name__ == "__main__":
    main()