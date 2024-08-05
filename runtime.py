import threading
from time import sleep
from client import Client
from server import ThreadedServer


if __name__ == "__main__":
    try:
        rt_server = ThreadedServer()
        rt_client = Client()
        threading.Thread(target=rt_server.accept, daemon=True).start()
        sleep(5)
        threading.Thread(target=rt_client.send).start()
    except Exception as e:
        print(e)
