import time
import socket

from random import randint

HOST = "127.0.0.1"
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        random_number1 = randint(1, 100)
        random_number2 = randint(101, 200)
        s.sendall(f'{random_number1},{random_number2}'.encode())
        print(f"Sending: {random_number1},{random_number2}")
        time.sleep(5)