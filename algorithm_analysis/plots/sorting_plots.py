import os
import numpy as np
import matplotlib.pyplot as plt
from ..algorithms import constants


def plot_results():
    """
    Generates a performance plot for all sorting algorithms using absolute execution time.

    Each algorithm's execution time is plotted across different input sizes.
    The data is loaded from a .npz file generated during the experiment phase.

    This plot provides a direct comparison of execution times in seconds for all
    available algorithms, helping to visually identify which ones are more efficient
    in practice across varying input sizes.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))

    results_path = os.path.join(
        base_dir, "..", "experiments", "results", "sorting_results.npz"
    )

    data = np.load(results_path)
    sizes = data["sizes"]

    plt.figure(figsize=(10, 6))
    for key in data.files:
        if key != "sizes":
            times = data[key] / constants.TIME_MULTIPLIER
            plt.plot(sizes, times, marker="o", label=key)

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithm Performance")

    # plt.yscale("log")
    # plt.xscale("log")

    plt.legend()
    plt.grid()

    plots_path = os.path.join(base_dir, "results", "sorting_performance.png")
    plt.savefig(plots_path)

    plt.show()

    plot_relative_performance(data, sizes, base_dir)


def plot_relative_performance(data, sizes, base_dir):
    baseline_key = "Quick Sort"  # reference
    baseline = data[baseline_key] / constants.TIME_MULTIPLIER

    plt.figure(figsize=(10, 6))
    for key in data.files:
        if key != "sizes" and key != baseline_key:
            times = data[key] / constants.TIME_MULTIPLIER
            diff = ((times - baseline) / baseline) * 100
            plt.plot(sizes, diff, marker="o", label=f"{key} vs {baseline_key}")

    plt.xlabel("Input Size")
    plt.ylabel("Difference (%)")
    plt.title("Relative Performance to Quick Sort")
    plt.axhline(0, color="gray", linestyle="--")
    plt.legend()
    plt.grid()

    output_path = os.path.join(base_dir, "results", "sorting_relative_performance.png")
    plt.savefig(output_path)
    plt.show()


if __name__ == "__main__":
    plot_results()
