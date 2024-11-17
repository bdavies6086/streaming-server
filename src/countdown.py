import threading

timer = None

lock = threading.Lock()

def start(countdown, callback):
    global timer
    with lock:
        if(timer != None):
            timer.cancel()
        timer = threading.Timer(countdown, callback)
        timer.start()
