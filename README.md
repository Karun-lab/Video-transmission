# Video Transmission using Socket and OpenCV

This repository contains a Python project for transmitting video over a local network using sockets and OpenCV. The project consists of two main scripts: `client.py` and `server.py`.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/).

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Karun-lab/Video-transmission.git
```

### Usage

1. Open a terminal and navigate to the project directory.

2. Run the server script:

```bash
python server.py
```

3. Open another terminal and run the client script:

```bash
python client.py
```

4. The server and client will establish a connection, and the video transmission will begin.

### Customization

- You can adjust the video resolution and frames per second (FPS) in the `server.py` and `client.py` scripts according to your preferences.


## Code Structure

### `server.py`

The server script initializes a socket, accepts connections from clients, and continuously sends video frames.

### `client.py`

The client script connects to the server, receives video frames, and displays them using OpenCV.

### Comments

Both scripts are thoroughly commented to aid understanding.
