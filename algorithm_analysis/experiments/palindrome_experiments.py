import os
import time
import numpy as np
import inspect
from algorithm_analysis.algorithms import palindromes
from algorithm_analysis.random_data.generator import random_string
from algorithm_analysis.algorithms import constants


def get_palindrome_functions():
    return {
        name.replace("_", " ").title(): func
        for name, func in inspect.getmembers(palindromes, inspect.isfunction)
        if name.startswith("is_palindrome_")
    }


def generate_palindrome(length):
    half = random_string(length // 2)
    return half + (half[::-1] if length % 2 == 0 else random_string(1) + half[::-1])


def measure_execution_time(func, samples):
    times = []
    for s in samples:
        start = time.perf_counter()
        func(s)
        end = time.perf_counter()
        times.append(constants.TIME_MULTIPLIER * (end - start))
    return np.median(times)


def run_experiments(min_size, max_size, step, samples_by_size, mode="mixed"):
    sizes = list(range(min_size, max_size + 1, step))
    algorithms = get_palindrome_functions()
    results = {name: [] for name in algorithms}

    for size in sizes:
        print(f"Running size {size}...")

        samples = []
        for _ in range(samples_by_size):
            if mode == "palindrome":
                samples.append(generate_palindrome(size))
            elif mode == "non_palindrome":
                s = random_string(size)
                while s == s[::-1]:
                    s = random_string(size)
                samples.append(s)
            else:
                samples.append(
                    generate_palindrome(size)
                    if np.random.rand() > 0.5
                    else random_string(size)
                )

        for name, func in algorithms.items():
            time_ms = measure_execution_time(func, samples)
            results[name].append(time_ms)
            print(f"{name} - Time: {time_ms / constants.TIME_MULTIPLIER:.6f} s")

    return sizes, results


def save_experiment_results(min_size, max_size, step, samples_by_size=10, mode="mixed"):
    sizes, results = run_experiments(min_size, max_size, step, samples_by_size, mode)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "results", f"palindrome_results_{mode}.npz")
    np.savez(path, sizes=sizes, **results)
    print(f"Results saved to {path}")


if __name__ == "__main__":
    save_experiment_results(10, 101, 10, 7, mode="mixed")
