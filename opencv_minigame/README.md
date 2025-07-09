# OpenCV Face Game

A simple experimental game using Python and OpenCV: detect your face with a webcam and score points by matching objects on the screen.

## Features
- Real-time webcam capture
- Face detection with Haar cascade (`faces.xml`)
- Score & life system

## How to run

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Download [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) as `faces.xml` and put it in the project folder.
3. Run:
    ```bash
    python main.py
    ```

## Requirements

- Python 3.7+
- opencv-python
- numpy

---
