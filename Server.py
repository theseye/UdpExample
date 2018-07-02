import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 2333))
while True:
    data, address = server.recvfrom(1024)
    print('客户端地址：', address)
    print('来自客户端的消息：', bytes(data).decode('utf-8'))
    server.sendto('你好客户端'.encode('utf-8'), address)
