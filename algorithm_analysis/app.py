import argparse
from algorithm_analysis.experiments.sorting_experiments import save_experiment_results
from algorithm_analysis.plots.sorting_plots import plot_results

# from algorithm_analysis.experiments.search_experiments import save_search_results


def parse_sizes_arg(s):
    if s is None:
        return None
    parts = s.replace(",", " ").split()
    if len(parts) != 4:
        raise ValueError("You must provide exactly 4 values: min max step samples")
    return tuple(map(int, parts))


def run_menu():
    print("Welcome to Algorithm Analyzer")
    print("1. Run sorting experiments")
    print("2. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        user_input = input("Enter min,max,step,samples (comma or space separated): ")
        try:
            parts = user_input.replace(",", " ").split()
            min_size, max_size, step, samples = map(int, parts)
            save_experiment_results(
                minimum_size=min_size,
                maximum_size=max_size,
                step=step,
                samples_by_size=samples,
            )
            plot_results()
        except ValueError:
            print("Invalid input. Please enter 4 numbers separated by space or comma.")
    else:
        print("Bye!")


def main():

    minimum_size = 10000
    maximum_size = 100000
    step = 5000
    samples_by_size = 7

    parser = argparse.ArgumentParser(description="Algorithm Analysis App")
    parser.add_argument(
        "--experiment",
        type=str,
        choices=["sorting", "search"],
        help="Experiment to run",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="experiments/results/sorting_results.npz",
        help="Output file path",
    )
    parser.add_argument(
        "--sizes",
        type=str,
        default=f"{minimum_size},{maximum_size},{step},{samples_by_size}",
        help="Comma- or space-separated list of 4 values: min,max,step,samples",
    )

    args = parser.parse_args()

    if args.experiment:
        match args.experiment:
            case "sorting":
                try:
                    min_size, max_size, step, samples = parse_sizes_arg(args.sizes)
                    save_experiment_results(
                        minimum_size=min_size,
                        maximum_size=max_size,
                        step=step,
                        samples_by_size=samples,
                    )
                    plot_results()
                except Exception as e:
                    print(f"Invalid --sizes input: {e}")
    else:
        run_menu()


if __name__ == "__main__":
    main()
