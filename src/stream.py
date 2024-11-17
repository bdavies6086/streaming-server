import cv2
from src.frame import crop
from src.countdown import start
import atexit
import threading

cap = cv2.VideoCapture(0)
channel = 0
faceCascade = cv2.CascadeClassifier('./face.xml')
streaming = False

lock = threading.Lock()

if not cap.isOpened():
    print("Error opening capture device")
    exit()

def get_channel():
    global channel
    return channel

def set_channel(index, time):
    with(lock):
        start(time, close_stream)
        global channel, streaming
        channel = index
        streaming = True

def close_stream():
    with(lock):
        print("Closing stream")
        global streaming
        streaming = False

def gen_frames(config):
    global channel, streaming
    while streaming:
        _, frame = cap.read()
        height, width, _ = frame.shape

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        faces = faceCascade.detectMultiScale(gray)
        for face in faces:
            x1, y1, w, h = face
            x2 = x1 + w
            y2 = y1 + h
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        xOffset, croppedWidth, yOffset, croppedHeight = crop(width, height, config.get('ROWS'), config.get('COLUMNS'), channel)
            
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', frame[yOffset:croppedHeight,xOffset:croppedWidth])[1].tobytes())

def cleanup():
    cap.release()

atexit.register(cleanup)