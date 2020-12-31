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

def encrypt_message(plaintext, key):
    print(f"{TAG[0]}: encrypting message")
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))    
    iv = b64encode(cipher.iv).decode('utf-8')
    ciphertext = b64encode(ct_bytes).decode('utf-8')
    # print(f"{ciphertext}\n{iv}")

    return iv, ciphertext

def decrypt_message(iv, ciphertext, key):
    print(f"{TAG[0]}: decrypting message")
    iv2 = b64decode(iv)
    ct2 = b64decode(ciphertext)
    cipher2 = AES.new(key, AES.MODE_CBC, iv2)
    pt = unpad(cipher2.decrypt(ct2), AES.block_size)
    # print(f"{pt.decode()}")

    return pt

def send_message(connection, key, message):
    print(f"{TAG[0]}: sending message")
    iv, encrypted_message = encrypt_message(message, key)
    iv_message = (f"{iv}|{encrypted_message}")

    connection.send(iv_message.encode())

def receive_message(connection, key):
    print(f"{TAG[0]}: receiving message")
    message = connection.recv(1024).decode('utf-8')
    #split by '|' to get iv nd ciphertext
    iv, ciphertext = str(message).split('|')

    plaintext = decrypt_message(iv, ciphertext, key)
    plaintext = plaintext.decode('utf-8')
    return plaintext

#====================================================================================================================================

def main():
    print(f"{TAG[0]}: starting TCP client")

    t1 = threading.Thread(target=threaded_client(), args=())

    t1.start()

    t1.join()

if __name__ == '__main__':
    main()