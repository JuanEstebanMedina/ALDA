import os
import numpy as np
import matplotlib.pyplot as plt
from algorithm_analysis.algorithms import constants


def plot_palindrome_results(mode="mixed"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(
        base_dir, "..", "experiments", "results", f"palindrome_results_{mode}.npz"
    )
    data = np.load(path)
    sizes = data["sizes"]

    plt.figure(figsize=(10, 6))
    for key in data.files:
        if key != "sizes":
            times = data[key] / constants.TIME_MULTIPLIER
            plt.plot(sizes, times, marker="o", label=key)

    plt.xlabel("Input Size (string length)")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Palindrome Detection Performance - {mode.title()} Inputs")
    plt.legend()
    plt.grid()

    output_path = os.path.join(base_dir, "results", f"palindrome_plot_{mode}.png")
    plt.savefig(output_path)
    plt.show()


if __name__ == "__main__":
    plot_palindrome_results("mixed")
