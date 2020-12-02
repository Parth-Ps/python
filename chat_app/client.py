import socket


def Main():
    host = '127.0.0.1'
    port = 5001
    mysocket = socket.socket()
    mysocket.connect((host, port))
    message = input("Enter the message: ")
    while message != 'q':
        mysocket.send(message.encode())
        data = mysocket.recv(1024).decode()
        print("Serve says:" + data)
        message = input("Enter the message: ")

    mysocket.close()


if __name__ == '__main__':
    Main()
