class Config():
    LOCAL_HOST = "127.0.0.1"
    SOCK_SIZE = 1024
    DEFAULT_PORT = 1337
    ENCODING = "utf-8"
    DATA = {
        "x": 0,
        "y": 0,
        "z": 0,
    }
    HOSTS = [
        # (LOCAL_HOST, DEFAULT_PORT)
        ("10.128.0.3", DEFAULT_PORT),
        ("10.128.0.6", DEFAULT_PORT),
        ("10.128.0.10", DEFAULT_PORT),
        ("10.128.0.12", DEFAULT_PORT),
    ]
