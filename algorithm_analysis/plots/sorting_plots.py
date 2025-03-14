import os
import numpy as np
import matplotlib.pyplot as plt


def plot_results():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    results_path = os.path.join(base_dir, "..", "experiments", "sorting_results.npz")

    data = np.load(results_path)
    sizes = data["sizes"]

    plt.figure(figsize=(10, 6))
    for key in data.files:
        if key != "sizes":
            plt.plot(sizes, data[key], marker="o", label=key)

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithm Performance")

    # plt.yscale("log")
    # plt.xscale("log")

    plt.legend()
    plt.grid()

    plots_path = os.path.join(base_dir, "sorting_performance.png")
    plt.savefig(plots_path)

    plt.show()


if __name__ == "__main__":
    plot_results()
