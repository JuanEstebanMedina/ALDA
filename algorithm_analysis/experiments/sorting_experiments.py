import os
import time
import numpy as np
from algorithm_analysis.algorithms.sorting import (
    bubble_sort,
    insertion_sort,
    quick_sort,
)
from algorithm_analysis.random_data.generator import random_list_of_ids


def measure_execution_time(sort_function, data):
    start_time = time.perf_counter()
    sort_function(data)
    end_time = time.perf_counter()
    return end_time - start_time


def run_experiments():
    # sizes = [100, 500, 1000, 5000, 10000]
    sizes = [i for i in range(100, 2001, 100)]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort,
    }

    results = {alg: [] for alg in algorithms}

    for size in sizes:
        print(f"Running experiments for size {size}...")
        data = random_list_of_ids(size)

        for name, func in algorithms.items():
            data_copy = data.copy()
            exec_time = measure_execution_time(func, data_copy)
            results[name].append(exec_time)
            print(f"{name}: {exec_time:.6f} seconds")

    return sizes, results


def save_experiment_results():
    sizes, results = run_experiments()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "sorting_results.npz")
    np.savez(save_path, sizes=sizes, **results)
    print("Results saved successfully at", save_path)


if __name__ == "__main__":
    save_experiment_results()
