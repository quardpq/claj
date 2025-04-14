import multiprocessing
import time

def process_chunk(chunk):
    return sum(chunk)

def parallel_sum(numbers, chunk_size=1000):
    chunks = [numbers[i:i + chunk_size] 
              for i in range(0, len(numbers), chunk_size)]

    with multiprocessing.get_context('spawn').Pool() as pool:
        results = pool.map(process_chunk, chunks)
    
    return sum(results)

def main():
    numbers = list(range(1, 1000001))

    start = time.time()
    sequential_sum = sum(numbers)
    seq_time = time.time() - start

    start = time.time()
    parallel_result = parallel_sum(numbers)
    par_time = time.time() - start

    print(f"Последовательная сумма: {sequential_sum}, время: {seq_time:.4f} сек")
    print(f"Параллельная сумма: {parallel_result}, время: {par_time:.4f} сек")
    print(f"Ускорение: {seq_time/par_time:.2f}x")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()