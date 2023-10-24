import os
import shutil
import random
import time

# Define the directory to simulate file creation
SIMULATED_DIR = '/path/to/monitored/directory'

# Function to simulate file creation with different dates
def simulate_file_creation():
    for i in range(1, 11):
        # Generate a random timestamp within the last 10 days
        timestamp = time.time() - random.randint(1, 10) * 24 * 3600
        file_name = f'file_{i}.txt'
        file_path = os.path.join(SIMULATED_DIR, file_name)
        with open(file_path, 'w') as file:
            file.write(f'This is {file_name} created at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))}')

simulate_file_creation()
