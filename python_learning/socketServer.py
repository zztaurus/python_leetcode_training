import socket

HOST = '192.168.124.34'
PORT = 8001


def main():
    # 使用 ipv4, 基于 tcp 协议
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1) # backlog: 它指定了系统在拒绝新连接之前允许的未接受连接数。如果未指定，系统将选择一个合理的默认值
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)



if __name__ == '__main__':
    main()

