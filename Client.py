import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    client_input = input()
    client.sendto(client_input.encode('utf-8'), ('127.0.0.1', 2333))
    response = client.recv(1024)
    print('来自服务器的消息：', bytes(response).decode('utf-8'))
