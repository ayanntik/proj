import socket
def train_collision_detection(line1, speed1, direction1, line2, speed2, direction2):
    if line1 != line2:
        return 'All clear', 'green'
    if direction1 != direction2:
        return 'WARNING: COLLISION', 'red'
    if speed1 >= speed2:
        return 'Train 2 has to slow down and stop', 'yellow'
    if speed1 < speed2:
        return 'WARNING: COLLISION', 'red'
    return 'Unknown situation', 'green'

def start_server():
    host = '127.0.0.1'
    port = 5050
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print('Server listening on {}:{}'.format(host, port))
    while True:
        client_socket, addr = server_socket.accept()
        print('Connection established from:', addr)
        # Ask questions regarding line and direction
        data = client_socket.recv(1024).decode()
        if(data):
            line1, direction1, line2, direction2, speed1, speed2 = data.split(',')
            print(data)
    speed1 = int(speed1)
    speed2 = int(speed2)
    result, color = train_collision_detection(line1, speed1, direction1, line2, speed2, direction2)
    response = f'{result},{color}'
    client_socket.send(response.encode())
    client_socket.close()
    print("Client from ",addr," disconnected")
    server_socket.close()
start_server()