import socket
import threading
import queue
import random
import os 
import urllib.request
import urllib.parse
import subprocess
import time
import rsa

"""
def menus():
    os.environ['PATH'] += os.pathsep + os.getcwd()
    print(f'[ MENUS ]')
    file_menu = os.listdir('menus')
    for i, menus in enumerate(file_menu):
        print(f'{i}_ {menus}')
    usr = int(input('*_> '))
    if usr < 0 or usr >= len(file_menu):
        print('Input Error!')
        return menus()
    else:
        c_menu = file_menu[usr]
        file_path = os.path.join('menus',file_menu[usr])
        subprocess.run(file_path, shell=True)

def download_progress(start, count, block_size, total_size):
    '''Show the download progress.'''
    percent = count * block_size * 100 / total_size
    duration = time.time() - start
    speed = total_size / 1024 / duration
    print(f'{percent:.2f}% downloaded, {speed:.2f}KB/s, elapsed time: {duration:.2f} seconds')
        

def rip_menu():
    usr = input(f'''
                    [Target IP :: {addr}] :: [ Main MENU ]
                    1 > Enter link of your menu
                    2 > Enter path of your menu
                    * > ''')
    if usr == '1':
        url = input('Enter url > ')
        parsed_url = urllib.parse.urlparse(url)
        default_filename = parsed_url.path.split('/')[-1]
        name = input('Rename the file (Optional) > ')
        if not name:
            name = default_filename
        try:
            # start the timer
            start = time.time()
            if not os.path.exists('menus'):
                os.makedirs('menus')
            # Open the file for writing
            fd = os.open(f'menus/{name}', os.O_CREAT | os.O_WRONLY | os.O_EXCL)
            tfp = open(fd, 'wb')
            filepath = tfp.name
            # Download the file
            urllib.request.urlretrieve(url, filepath, reporthook=lambda count, block_size, total_size: download_progress(start, count, block_size, total_size))
            # Close the file
            os.close(fd)
            # End the timer
            end = time.time()
            return menus()
                
        except ConnectionError as e:
            print(f'Connection Error [{e}]')
            print('NOTE For Option 2: You can manually download the file and copy it to menus folder.')
    elif usr == '2':
        return menus()
"""               

public_key, private_key = rsa.newkeys(1024)
public_partner = None

IP = 'localhost'
PORT = 9191
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen()
client,_=server.accept()
client.send(public_key.save_pkcs1("PEM"))
public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

def send_message(c):
    while True:
        message = input(f'/{client}/~_> ')
        c.send(rsa.encrypt(message.encode(), public_partner))

def receive_message(c):
    while True:
        print(f'\n/{c}/~_> {rsa.decrypt(c.recv(1024), private_key).decode()}')

threading.Thread(target=send_message, args=(client,)).start()
threading.Thread(target=receive_message, args=(client,)).start()


"""
def crash():
    IP = '103.94.69.20'
    PORT = int(random.randint(100, 9999))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((IP, PORT))
        s.listen(1)
        conn, addr = s.accept()
    except ConnectionRefusedError:
        return crash()

def scan_ports():
    SERVER_IP = str(input('Targets IP address > '))
    print(f'\n[Scanning ports] :: [IP - {SERVER_IP}]')
    q = queue.Queue()

    # Storing port numbers in queue
    for i in range(1, 1000):
        q.put(i)

    def scan():
        while not q.empty():
            port = q.get()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:    
                    s.connect((SERVER_IP, port))
                    print(f'\n> PORT [{port}] is open for [{SERVER_IP}]')
                except :
                    pass
            q.task_done()
                    
    # Create number of threads to use
    for i in range(30):
        t = threading.Thread(target=scan, daemon=True)
        t.start()
    q.join()
    print('Scan finished')
    
def menu():
    usr = input('''
                OPTION$
                -------
                1. Scan Port
                2. Crash Target PC
                -------
                > ''')
    if usr == '1':
        scan_ports()
    elif usr == '2':
        crash()
    else:
        pass
 """
