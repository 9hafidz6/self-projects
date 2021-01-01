#this is a client file that
import os
import sys
import time
from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
from Crypto import Random
from base64 import b64encode
from base64 import b64decode
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import threading
import socket
from functions import receive_message, send_message  

TAG = ["INFO", "ERROR", "SUCCESS"]
HOST = "localhost"
PORT = 9000
KEY = b'0123456789abcdef'

def threaded_client():
    #connect via TCP
    print(f"{TAG[0]}: creating TCP socket")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    try:
        sock.connect(server_address)
    except socket.error as e:
        print(f"{TAG[1]}: unable to connect to server, {e}")
    print(f"{TAG[2]}: connected to server")

    connected = True

    while connected:
        message = input(f"input message here: ")
        send_message(sock, KEY, message)

        plaintext = receive_message(sock, KEY)
        print(f"{plaintext}")

        if plaintext == "exit":
            connected = False

        time.sleep(0.1)
    
#====================================================================================================================================

def main():
    print(f"{TAG[0]}: starting TCP client")

    t1 = threading.Thread(target=threaded_client(), args=())

    t1.start()

    t1.join()

if __name__ == '__main__':
    main()