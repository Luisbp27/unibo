import os
import time
import logging
import daemon
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set up logging
logging.basicConfig(filename='/path/to/daemon.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define the directory to be monitored
MONITORED_DIR = '/path/to/monitored/directory'

# Define the event handler for file system events
class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_name = event.src_path
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        logging.info(f'New file detected: {file_name} (created at {timestamp})')

# Function to start the daemonized process
def start_daemon():
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=MONITORED_DIR, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Daemon context to detach the process from the terminal
with daemon.DaemonContext():
    start_daemon()
