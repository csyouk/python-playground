import threading
import time

class RepeatEvery(threading.Thread):
    def __init__(self, interval, func, *args, **kwargs):
        threading.Thread.__init__(self)
        self.interval = interval  # seconds between calls
        self.func = func          # function to call
        self.args = args          # optional positional argument(s) for call
        self.kwargs = kwargs      # optional keyword argument(s) for call
        self.runable = True
    def run(self):
        while self.runable:
            self.func(*self.args, **self.kwargs)
            time.sleep(self.interval)
    def stop(self):
        self.runable = False

def greeting(hello):
    print(hello)

thread = RepeatEvery(3, greeting, "Hi guys")
print("starting")
thread.start()
thread.join(21)  # allow thread to execute a while...
thread.stop()
print('stopped')