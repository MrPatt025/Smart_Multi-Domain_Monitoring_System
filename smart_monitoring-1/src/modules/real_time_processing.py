from queue import Queue
import asyncio
import threading

class RealTimeProcessor:
    def __init__(self):
        self.data_queue = Queue()

    def start(self):
        threading.Thread(target=self.process_data, daemon=True).start()

    def add_data(self, data):
        self.data_queue.put(data)

    def process_data(self):
        while True:
            if not self.data_queue.empty():
                data = self.data_queue.get()
                self.handle_data(data)

    def handle_data(self, data):
        # Process the incoming data
        print(f"Processing data: {data}")
        # Add your data processing logic here

    async def async_process_data(self):
        while True:
            if not self.data_queue.empty():
                data = self.data_queue.get()
                await self.handle_data_async(data)

    async def handle_data_async(self, data):
        # Asynchronous data processing logic
        print(f"Async processing data: {data}")
        # Add your async data processing logic here