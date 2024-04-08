######Import for Watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import signal
import subprocess
import time
from random import randint
import os

#### Git Commands
def git_Script(c):
    value = randint(5, 7)
    time.sleep(value)
    commit_text = f"a20Tk{c}"
    file1 = subprocess.run(["bash", "script.sh", commit_text])

class MyEventHandler(FileSystemEventHandler):
    counter = 0
    file_cache = {}
   
    def on_modified(self, event):
        # print(self.file_cache)
        seconds = int(time.time())
        key = (seconds, event.src_path)
        if key in self.file_cache:
            return
        elif event.is_directory:
            # print(event)
            git_Script(self.counter)
            self.counter+=1
        self.file_cache[key] = True
        
        ###Terminate current session to empty file_cache
        if self.counter >= 10:
            #send control-c to terminal
            os.kill(os.getpid(), signal.SIGINT) #it also worked



observer = Observer()
path = "."
observer.schedule(MyEventHandler(), path, recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()



