import socket
import requests

HOST = '192.168.124.34'
POST = 8001

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, POST))
        s.sendall(b'hello')
        data = s.recv(1024)
        print(f"recieved: {repr(data)}")


if __name__ == '__main__':
    main()

