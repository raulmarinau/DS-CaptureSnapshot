# DS-CaptureSnapshot

Python script for a network client that continuously sends messages to a list of hosts for a certain duration and then initiates a snapshot.

After the duration ends, it sends a "snap" message to all hosts to start a snapshot.

`consts.py` defines the list of IPs
`runtime.py` starts the server as a daemon accepting connections