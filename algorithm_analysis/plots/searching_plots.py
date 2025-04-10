import os
import numpy as np
import matplotlib.pyplot as plt
from ..algorithms import constants


def plot_results():
    """
    Generates performance plots for all searching algorithms using absolute execution time.

    Loads data from a .npz file generated during the experiment phase and plots execution
    time vs input size for each algorithm.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))

    results_path = os.path.join(
        base_dir, "..", "experiments", "results", "searching_results.npz"
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
    plt.title("Searching Algorithm Performance")
    plt.legend()
    plt.grid()

    plots_path = os.path.join(base_dir, "results", "searching_performance.png")
    plt.savefig(plots_path)
    plt.show()

    plot_relative_performance(data, sizes, base_dir)


def plot_relative_performance(data, sizes, base_dir):
    """
    Plots the relative performance of each searching algorithm compared to Linear Search,
    handling potential division by zero.
    """
    baseline_key = "binary Search"
    baseline = data[baseline_key] / constants.TIME_NS_MULTIPLIER

    plt.figure(figsize=(10, 6))

    for key in data.files:
        if key != "sizes" and key != baseline_key:
            times = data[key] / constants.TIME_NS_MULTIPLIER

            with np.errstate(divide="ignore", invalid="ignore"):
                diff = np.where(
                    baseline != 0, ((times - baseline) / baseline) * 100, np.nan
                )

            plt.plot(sizes, diff, marker="o", label=f"{key} vs {baseline_key}")

    plt.xlabel("Input Size")
    plt.ylabel("Difference (%)")
    plt.title("Relative Performance to Linear Search")
    plt.axhline(0, color="gray", linestyle="--")
    plt.legend()
    plt.grid()

    output_path = os.path.join(
        base_dir, "results", "searching_relative_performance.png"
    )
    plt.savefig(output_path)
    plt.show()


if __name__ == "__main__":
    plot_results()
