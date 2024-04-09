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
sleep_time  = 7

#### Git Commands
def git_Script(c):
    commit_text = f"a20Tk{c}"
    subprocess.call(f'bash {script_path} {commit_text}', shell=True, cwd=git_home_path)

class PausingObserver(Observer):
    def dispatch_events(self, *args, **kwargs):
        if not getattr(self, '_is_paused', False):
            super(PausingObserver, self).dispatch_events(*args, **kwargs)

    def pause(self):
        self._is_paused = True

    def resume(self):
        time.sleep(randint(7, 10))
        self.event_queue.queue.clear() ##clear all the queued events ##multiple event call problem solved
        self._is_paused = False

class MyEventHandler(FileSystemEventHandler):
    counter = 0
    def on_modified(self, event):
        print("modified triggered\n")
        observer.pause()
        observer.resume()

        git_Script(self.counter)
        self.counter+=1

        ###Terminate current session
        if self.counter >= 10:
            #send control-c to terminal
            os.kill(os.getpid(), signal.SIGINT) #it also worked


observer = PausingObserver()
observer.schedule(MyEventHandler(), watch_path, recursive=True) # monitor recursively to sub directories
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()



