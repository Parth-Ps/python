import socket


def Main():
    host = '127.0.0.1'
    port = 5001
    mysocket = socket.socket()
    mysocket.bind((host, port))
    mysocket.listen(1)
    conn, addr = mysocket.accept()
    print("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("client says: " + str(data))
        data = input("Enter the message: ")
        conn.send(data.encode())
    conn.close()


if __name__ == '__main__':
    Main()
