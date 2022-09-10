import socket
import json
from config import *
import threading

class Client:
    def __init__(self, addr, connection):
        self.addr = addr
        self.connection = connection

    def auth(self):
        pass

    def listen(self):
        pass

    def send_sql(self):
        pass

class Server:
    def __init__(self, host, port, max_clients):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(max_clients)
        self.connected_clients = {} # addr: Client class instance
        print('Server configured')

    def listen_for_clients(self):
        while True:
            conn, addr = sock.accept()
            print('[DEBUG] New socket client', addr)
            addr_format = f"{addr[0]}:{addr[1]}"
            self.connected_clients[addr_format] = Client(addr_format, conn)
            threading.Thread(target=lambda: self.connected_clients[addr_format].listen()).start()

if __name__ == "__main__":
    serv = Server(SOCKET_HOST, SOCKET_PORT, SOCKET_MAX_CLIENTS)
    serv.listen_for_clients()