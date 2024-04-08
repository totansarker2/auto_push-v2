######Import for Watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import signal
import subprocess
import time
from random import randint
import os

git_home_path = "../career_hub"
watch_path = "../career_hub/src"
script_path = "../auto_push/script.sh"

#### Git Commands
def git_Script(c):
    value = randint(5, 7)
    time.sleep(value)
    commit_text = f"a20Tk{c}"
    subprocess.call(f'bash {script_path} {commit_text}', shell=True, cwd=git_home_path)

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
observer.schedule(MyEventHandler(), watch_path, recursive=True) # monitor recursively to sub directories
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()



