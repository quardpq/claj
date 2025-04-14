import threading
import queue
import time

class Agent:
    def __init__(self, initial_state):
        self.state = initial_state
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()
    
    def _run(self):
        while True:
            func = self.queue.get()
            if func is None:  
                break
            self.state = func(self.state)
            self.queue.task_done()
    
    def send(self, func):
        self.queue.put(func)
    
    def stop(self):
        self.queue.put(None)
        self.thread.join()

agent = Agent(0)

agent.send(lambda x: x + 1)
agent.send(lambda x: x * 2)
agent.send(lambda x: x + 10)

time.sleep(0.1)

print(f"Текущее состояние агента: {agent.state}")

agent.stop()