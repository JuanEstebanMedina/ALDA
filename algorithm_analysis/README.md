# Algorithm Analysis

## Sorting Algorithm Comparison

This project focuses on the experimental analysis of different sorting algorithms. The objective is to compare their performance under various conditions and visualize the results using data plots.

### Implemented Sorting Algorithms
- **Bubble Sort**: A simple comparison-based algorithm with O(n²) complexity.
- **Insertion Sort**: A straightforward algorithm with O(n²) complexity.
- **Quick Sort**: An efficient sorting algorithm with an average complexity of O(n log n).
- **Merge Sort**: A divide-and-conquer algorithm with O(n log n) complexity.
- **Python's Built-in Sort**: Uses Timsort with O(n log n) complexity.

## Searching Algorithm Comparison

This project also includes the experimental analysis of different searching algorithms to compare their performance under various conditions.

### Implemented Searching Algorithms
- **Linear Search**: A simple search algorithm that checks each element in the list sequentially until the desired element is found or the list ends. It has a time complexity of O(n).
- **Binary Search**: A logarithmic search algorithm for sorted lists with O(log n) complexity.
- **Ternary Search**: A divide-and-conquer search algorithm for sorted lists with O(log₃ n) complexity.

## Palindrome Detection Algorithm Comparison

This project also includes experimental analysis of different palindrome detection algorithms to compare their performance and efficiency.

### Implemented Palindrome Detection Algorithms
- **Reverse String Comparison**: Checks if the normalized string is equal to its reverse.
- **Iterative Two-Pointer**: Uses two pointers from both ends to compare characters.
- **Recursive Comparison**: Recursively compares characters from both ends.
- **Stack-Based Comparison**: Uses a stack to compare the string with its reverse order.

All algorithms normalize the input by removing non-alphanumeric characters and converting to lowercase before checking for palindromes.

### Methodology
1. **Data Generation**: Random datasets of different sizes are generated to evaluate algorithm performance.
2. **Execution & Benchmarking**: Each algorithm is executed multiple times to measure execution time.
3. **Performance Visualization**: Execution times are plotted to compare efficiency across different input sizes.

### Repository Structure
```
algorithm_analysis/
│-- algorithms/
│   │   ├── sorting.py           # Sorting algorithm implementations
│   │   ├── searching.py         # Searching algorithm implementations
│   │   └── palindromes.py       # Palindrome detection algorithm implementations
│-- experiments/
│   │   ├── sorting_experiments.py   # Experiments with sorting algorithms
│   │   ├── searching_experiments.py # Experiments with searching algorithms
│   │   └── palindrome_experiments.py # Experiments with palindrome algorithms
│-- plots/
│   │   ├── sorting_plots.py     # Plot generation for sorting
│   │   ├── searching_plots.py   # Plot generation for searching
│   │   └── palindrome_plots.py  # Plot generation for palindrome analysis
│-- random_data/
│   │   └── generator.py         # Random data generator
│-- tests/
│   │   ├── test_sorting.py      # Unit tests for sorting
│   │   ├── test_searching.py    # Unit tests for searching
│   │   └── test_palindromes.py  # Unit tests for palindrome detection
│-- app.py                       # Main entry point
│-- README.md                    # Project documentation
```

## Running Experiments
To run the sorting experiments and generate plots, follow these steps:

- **Run the sorting experiments and generate plots**
   ```sh
   python -m algorithm_analysis.app --experiment sorting --sizes "min max step sample_size"
   python -m algorithm_analysis.app --experiment sorting --sizes "1000 10001 1000 7" # Example
   ```

- **Run the searching experiments and generate plots**
   ```sh
   python -m algorithm_analysis.app --experiment searching --sizes "min max step sample_size"
   python -m algorithm_analysis.app --experiment searching --sizes "1000 10001 1000 7" # Example
   ```

- **Run the palindrome experiments and generate plots**
   ```sh
   python -m algorithm_analysis.app --experiment palindrome --sizes "min max step sample_size"
   python -m algorithm_analysis.app --experiment palindrome --sizes "10 101 10 7" # Example
   ```

- **Or just use the temporary scripts provided in the `Scripts` directory**
   ```sh
   Scripts\run_sorting_analysis.bat
   Scripts\run_searching_analysis.bat
   Scripts\run_palindrome_analysis.bat
   ```

## Running Unit Tests
To run the unit tests, use the following command:
```sh
pytest algorithm_analysis/tests/
```

Also, there is a script to see the coverage of the project:
```sh
Scripts\coverage.bat
```

### Expected Results
- A set of plots showing the time complexity of different algorithms across varying input sizes.
- Insight into the efficiency of each algorithm under different conditions.

### Contributions
- **Contributor**: Juan Esteban Medina Rivas
- **Professor**: Rafael Alberto Niquefa Velasquez
- **Institution**: Universidad Escuela Colombiana de Ingeniería Julio Garavito

---
More algorithms and experiments could be added as the project progresses.

