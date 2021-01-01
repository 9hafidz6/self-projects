#this is a server file that
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
HOST = "localhost" #host to connect to
PORT = 9000 #port to connect to
KEY = b'0123456789abcdef'


def Threaded_server():
    #connect via TCP
    print(f"{TAG[0]}: creating TCP socket: ")
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(f"{TAG[0]}: starting on host {HOST} and port {PORT}")
    try:
        sock.bind((HOST,PORT))
    except socket.error as e:
        print(f"{TAG[1]}: {e}")
    sock.listen(1)
    print(f"{TAG[0]}: waiting for connection...")
    connection, client_address = sock.accept()
    print(f"{TAG[2]}: connected to {client_address}")
    
    #do something here
    connected = True
    while connected:
        #send and receive from client
        plaintext = receive_message(connection, KEY)
        print(f"{plaintext}")
        
        message = input(f"input message here: ")
        send_message(connection, KEY, message)

        if plaintext == "exit":
            connected = False
        
        time.sleep(0.1)
    
    connection.close()

#====================================================================================================================================

def main():
    # test = Random.get_random_bytes(10)
    # print(test)
    print(f"{TAG[0]}: starting server(s)")

    # #test encrpyt and decrypt using pycryptodome
    # key = b'0123456789abcdef'
    # plaintext = b'test'
    # cipher = AES.new(key, AES.MODE_CBC)
    # ct_bytes = cipher.encrypt(pad(plaintext, AES.block_size))   
    # iv = b64encode(cipher.iv).decode('utf-8')
    # ciphertext = b64encode(ct_bytes).decode('utf-8')
    # print(f"{ciphertext}\n{iv}")

    # iv2 = b64decode(iv)
    # ct2 = b64decode(ciphertext)
    # cipher2 = AES.new(key, AES.MODE_CBC, iv2)
    # pt = unpad(cipher2.decrypt(ct2), AES.block_size)
    # print(f"{pt.decode()}")

    t1 = threading.Thread(target=Threaded_server(), args=())

    t1.start()

    t1.join()

if __name__ == '__main__':
    main()