import time
import os
import daemon

# Define the directory to monitor
MONITOR_DIR = '/Users/luisbarcap/Downloads'

def monitor_directory():
    while True:
        new_files = [f for f in os.listdir(MONITOR_DIR) if os.path.isfile(os.path.join(MONITOR_DIR, f))]
        for file in new_files:
            file_path = os.path.join(MONITOR_DIR, file)
            # Get the creation time of the file
            file_creation_time = os.path.getctime(file_path)
            print(f"New file detected: {file} (created at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_creation_time))})")
        time.sleep(10)  # Sleep for 10 seconds before checking again

def run_daemon():
    with daemon.DaemonContext():
        monitor_directory()

if __name__ == "__main__":
    run_daemon()
