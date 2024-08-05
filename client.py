import socket
import random
from datetime import datetime
from time import sleep, time
from consts import Config


class Client():
    def __init__(self, port: int = Config.DEFAULT_PORT):
        self.message = b""
        self.hosts = Config.HOSTS
        self.timer = 20
        self.start_time = time()
        self.timer_ticks = 5

    def log(self, msg: str):
        timestamp = datetime.now().time()
        print(f"CLIENT @ {timestamp} -> {msg}")

    def send(self):
        while True:
            for host in self.hosts:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    try:
                        self.message = bytes(self.choose_var(),
                                             Config.ENCODING)
                        sock.connect(host)
                        sock.sendall(self.message)
                        self.log(f"I'm sending {self.message}")
                        data = sock.recv(Config.SOCK_SIZE)
                        self.log(f'Client got back {data}')
                    except Exception as e:
                        self.log(e)
                    # except ConnectionRefusedError:
                    #     self.log(f"Refused conn for {host}")
            if self.timer <= (time() - self.start_time):
                break
            sleep(self.timer_ticks)

        for host in self.hosts:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                try:
                    self.message = b"snap"
                    sock.connect(host)
                    sock.sendall(self.message)
                    self.log("Starting snapshot")
                    data = sock.recv(Config.SOCK_SIZE)
                    self.log(f'Client got back {data}')
                except Exception as e:
                    self.log(e)
                # except ConnectionRefusedError:
                #     self.log(f"Refused conn for {host}")

    def choose_var(self):
        var = random.randint(0, 2)
        if (var == 0):
            return "x"
        elif (var == 1):
            return "y"
        return "z"


if __name__ == "__main__":
    client = Client()
    client.send()
