import threading
from multiprocessing import Value

counter = Value('i', 0)
lock = threading.Lock()

def increment_counter():
    with lock:
        counter.value += 1

threads = []
for _ in range(10):
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Итоговое значение счетчика: {counter.value}")