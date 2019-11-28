import socket
import datetime
import sys
import time


def main():
    print("Server Side.")
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = socket.gethostname()
    IP = socket.gethostbyname(HOST)
    port = 1234
    SOCKET.bind((HOST, port))
    name = input('Enter name: ')
    SOCKET.listen(5)
    print("Open for new connection...")
    connection, ADDRESS = SOCKET.accept()
    print("Connecting....")
    for i in range(21):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        time.sleep(0.25)
    print("\nConnection Established.")
    print('Remember: You can Press Exit to leave the chat at anytime.')
    print("--------------------------------------------")

    client_name = connection.recv(1024)
    client_name = client_name.decode()
    print('connected to: ' + client_name)
    print(str(datetime.datetime.now()))
    print("\n")
    connection.send(name.encode())
    while True:
        message = input('ME: ')
        print(str(datetime.datetime.now())+ "\n")
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
        print(client_name, ':', message)
        print(str(datetime.datetime.now())+ "\n")


if __name__ == "__main__":
    main()
    