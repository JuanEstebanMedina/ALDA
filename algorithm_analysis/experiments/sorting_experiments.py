import os
import time
import inspect
import numpy as np
from ..algorithms import constants
from algorithm_analysis.algorithms import sorting
from algorithm_analysis.random_data.generator import random_list_of_ids


def get_sorting_algorithms():
    """
    Retrieves all sorting functions from the sorting module
    whose names end with '_sort'.
    """
    return {
        name.replace("_", " ").title(): func
        for name, func in inspect.getmembers(sorting, inspect.isfunction)
        if name.endswith("_sort")
    }


def measure_execution_time(sort_function, data):
    """
    Returns the median of the execution time measures for a sorting algorithm given in
    """
    times = []

    for sample in data:
        start_time = time.time()
        sort_function(sample.copy())
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]


def run_experiments(minimum_size, maximum_size, step, samples_by_size):
    """
    Run sorting experiments for the given range of sizes and step, and the number of samples per size.
    """
    sizes = [i for i in range(minimum_size, maximum_size, step)]
    algorithms = get_sorting_algorithms()

    results = {name: [] for name in algorithms}

    for size in sizes:
        print(f"Running experiments for size {size}...")

        data = [random_list_of_ids(size) for _ in range(samples_by_size)]

        for name, func in algorithms.items():
            exec_time = measure_execution_time(func, data)
            results[name].append(exec_time)
            print(
                f"{name} - Execution time: {exec_time / constants.TIME_MULTIPLIER:.6f} seconds"
            )

    return sizes, results


def save_experiment_results(minimum_size, maximum_size, step, samples_by_size=10):
    """
    Save the results of the sorting experiments to a file.
    """
    sizes, results = run_experiments(minimum_size, maximum_size, step, samples_by_size)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "results", "sorting_results.npz")

    np.savez(save_path, sizes=sizes, **results)
    print("Results saved successfully at", save_path)


if __name__ == "__main__":
    save_experiment_results(100, 1001, 100, 5)
