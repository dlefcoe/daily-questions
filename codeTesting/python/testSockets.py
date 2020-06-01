'''

file to test the sockets module

'''



import socket
import threading

PORT = 5050
hostname = socket.gethostname()
SERVER = socket.gethostbyname(hostname)
ADDR = (SERVER, PORT)

print('the host name is', hostname)
print('the server is', SERVER)

# create server (socket) and bind to address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    ''' function that runs for each client '''
    print(f'[new connection] {addr} connected')
    
    connected = True
    while connected:
        msg = conn.rev()

def start():
    '''
    listed for and handle connections

    pass to handle_client function
    '''
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[active connections] {threading.activeCount() -1}')

    

print('[starting] server is starting ...')
start()

