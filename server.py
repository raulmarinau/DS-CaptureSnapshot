import socket
import random
import threading
import json
from datetime import datetime
from consts import Config


class ThreadedServer():
    def __init__(self, port: int = Config.DEFAULT_PORT):
        self.data = Config.DATA
        self.port = port
        self.is_recording = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((Config.LOCAL_HOST, port))

    def log(self, msg: str):
        timestamp = datetime.now().time()
        print(f"SERVER @ {timestamp} -> {msg}")

    def accept(self):
        self.sock.listen(4)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            self.log(f"Handling new conn for {address}")
            threading.Thread(target=self.listen,
                             args=(client, address)).start()

    def listen(self, client, addr):
        while True:
            try:
                decoded_data = client.recv(Config.SOCK_SIZE).decode(Config.ENCODING)  # noqa: E501
                if decoded_data == "snap":
                    self.log(f"Sending current state {self.data}")
                    self.log("No more updates")
                    response = bytes(json.dumps(self.data), Config.ENCODING)
                    self.is_recording = True
                    client.send(response)
                elif decoded_data != "":
                    if not self.is_recording:
                        self.data[decoded_data] = random.randint(1, 9)
                        self.log(f"Updating data to {self.data}")
                        response_string = f"update {decoded_data}"
                        response = bytes(response_string, Config.ENCODING)
                        client.send(response)
                    else:
                        self.log(f"Incoming message during snapshot {decoded_data} from {addr}")  # noqa: E501
                        response_string = f"incoming {decoded_data} from {addr}"  # noqa: E501
                        response = bytes(response_string, Config.ENCODING)
                        client.send(response)
                        # could send the messages to an external observer
                        # for now they only reply to the client that tried
                        # to connect to the server what should be sent
                        # to the observer
            except Exception as e:
                self.log(e)
                self.log(f"Closing conn to {client}")
                client.close()
                return False


if __name__ == "__main__":
    try:
        ThreadedServer().accept()
    except KeyboardInterrupt:
        print("\n Closed by CTRL+C")
