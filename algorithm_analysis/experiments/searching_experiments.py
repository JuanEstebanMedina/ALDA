import os
import time
import inspect
import numpy as np
from ..algorithms import searching
from algorithm_analysis.algorithms import constants
from algorithm_analysis.random_data.generator import (
    random_list_of_ids,
    random_existing_value_from_list,
)


def get_searching_algorithms():
    """
    Retrieves all search functions from the searching module
    whose names end with '_search'.
    """
    return {
        name.replace("_", " ").title(): func
        for name, func in inspect.getmembers(searching, inspect.isfunction)
        if name.endswith("_search")
    }


def measure_execution_time(search_function, data, targets):
    """
    Returns the median execution time for a search function over given data and targets.
    """
    times = []

    for sample, target in zip(data, targets):
        start_time = time.perf_counter()
        search_function(sample, target)
        end_time = time.perf_counter()
        times.append((end_time - start_time) * constants.TIME_NS_MULTIPLIER)
        print(start_time, end_time, search_function.__name__)

    times.sort()
    return times[len(times) // 2]


def run_experiments(minimum_size, maximum_size, step, samples_by_size):
    """
    Run searching experiments for the given range of sizes and number of samples.
    """
    sizes = [i for i in range(minimum_size, maximum_size, step)]
    algorithms = get_searching_algorithms()
    results = {name: [] for name in algorithms}

    for size in sizes:
        print(f"Running experiments for size {size}...")

        data = [sorted(random_list_of_ids(size)) for _ in range(samples_by_size)]
        # targets = [sample[size // 2] for sample in data]
        targets = [sample[-1] + 1 for sample in data]
        # targets = [random_existing_value_from_list(sample) for sample in data]

        for name, func in algorithms.items():
            exec_time = measure_execution_time(func, data, targets)
            results[name].append(exec_time)
            print(
                f"{name} - Execution time: {exec_time / constants.TIME_NS_MULTIPLIER} seconds"
            )

    return sizes, results


def save_experiment_results(minimum_size, maximum_size, step, samples_by_size=10):
    """
    Save the results of the searching experiments to a file.
    """
    sizes, results = run_experiments(minimum_size, maximum_size, step, samples_by_size)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "results", "searching_results.npz")

    np.savez(save_path, sizes=sizes, **results)
    print("Results saved successfully at", save_path)


if __name__ == "__main__":
    save_experiment_results(100, 1001, 100, 5)
