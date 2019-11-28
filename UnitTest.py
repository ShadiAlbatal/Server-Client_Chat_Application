import unittest
import socket
import datetime

class Test_server (unittest.TestCase):

    HOST = socket.gethostname()
    PORT = 12345

    def test_server(self):

        CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        CONNECTION.connect((self.HOST, self.PORT))

        MESSAGE = "Shadi"
        CONNECTION.send(MESSAGE.encode())
        rec = CONNECTION.recv(1024).decode()
        CONNECTION.close()

        self.assertEqual(MESSAGE, "Shadi")
        print(str(datetime.datetime.now()))


if __name__ == '__main__':
    unittest.main()