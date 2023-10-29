import time
import os
import daemon

# Define the directory to monitor
MONITOR_DIR = '/Users/luisbarcap/Documents/GitHub/unibo/DSS/lab5'

def generate_test_file(test_file_name, creation_time):
    test_file_path = os.path.join(MONITOR_DIR, test_file_name)
    with open(test_file_path, 'w') as file:
        file.write("This is a test file")
    os.utime(test_file_path, (creation_time, creation_time))
    print(f"Created test file: {test_file_path}")

def create_test_files():
    # Create test files with specific creation dates
    generate_test_file("file1.txt", time.time())  # Current time (today)
    generate_test_file("file2.txt", time.time() - (24 * 60 * 60))  # 1 day ago

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
        create_test_files()  # Create the test file when the daemon starts
        monitor_directory()

if __name__ == "__main__":
    run_daemon()
