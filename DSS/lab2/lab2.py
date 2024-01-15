import threading
import queue
import json
import random
import time

# Shared queue with a maximum capacity of 10 items
max_size = 10
shared_queue = queue.Queue(maxsize=max_size)

# Lock for synchronization
lock = threading.Lock()

# Producer function 1
def producer1():
    while True:
        data = {'producer': 1, 'value': random.randint(1, 100)}
        json_data = json.dumps(data) # Serialize object to a JSON formatted string
        with lock:
            if shared_queue.qsize() < max_size:
                shared_queue.put(json_data)
                print(f"Producer 1 processed: {data}")
            else:
                print(f"Queue is full. Skipping production!")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate random wait time before producing the next item

# Producer function 2
def producer2():
    while True:
        data = {'producer': 2, 'value': random.randint(1, 100)}
        json_data = json.dumps(data) # Serialize object to a JSON formatted string
        with lock:
            if shared_queue.qsize() < max_size:
                shared_queue.put(json_data)
                print(f"Producer 2 processed: {data}")
            else:
                print(f"Queue is full. Skipping production!")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate random wait time before producing the next item

# Consumer function
def consumer():
    while True:
        with lock:
            if not shared_queue.empty():
                json_data = shared_queue.get()
                data = json.loads(json_data) # Deserialize JSON formatted string to an object
                print(f"    Consumer processed: {data}")
            else:
                print("Queue is empty.")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate random wait time before processing the next item

# Create producer threads
producer_thread1 = threading.Thread(target=producer1)
producer_thread2 = threading.Thread(target=producer2)

# Create consumer thread
consumer_thread = threading.Thread(target=consumer)

# Start the threads
producer_thread1.start()
producer_thread2.start()
consumer_thread.start()

# Main thread will wait for the producer and consumer threads to finish
producer_thread1.join()
producer_thread2.join()
consumer_thread.join()
