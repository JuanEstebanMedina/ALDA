# Algorithm Analysis

## Sorting Algorithm Comparison

This project focuses on the experimental analysis of different sorting algorithms. The objective is to compare their performance under various conditions and visualize the results using data plots.

### Implemented Sorting Algorithms
- **Bubble Sort**: A simple comparison-based algorithm with O(n²) complexity.
- **Insertion Sort**: A straightforward algorithm with O(n²) complexity.
- **Quick Sort**: An efficient sorting algorithm with an average complexity of O(n log n).
- **Merge Sort**: A divide-and-conquer algorithm with O(n log n) complexity.
- **Python's Built-in Sort**: Uses Timsort with O(n log n) complexity.

### Methodology
1. **Data Generation**: Random datasets of different sizes are generated to evaluate algorithm performance.
2. **Execution & Benchmarking**: Each sorting algorithm is executed multiple times to measure execution time.
3. **Performance Visualization**: Execution times are plotted to compare efficiency across different input sizes.

### Repository Structure
```
algorithm_analysis/
│── algorithms/
│   ├── sorting.py          # Implementations of sorting algorithms
│── tests/
│   ├── test_sorting.py     # Unit tests for sorting functions
│── experiments/
│   ├── sorting_analysis.py # Performance benchmarking and plotting
│── plots/                  # Generated plots for analysis
│── README.md               # Project documentation
```


## Running Experiments
To run the sorting experiments and generate plots, follow these steps:

- **Run the sorting experiments and generate plots**
   ```sh
   python -m algorithm_analysis.app --experiment sorting --sizes "min max step sample_size"
   python -m algorithm_analysis.app --experiment sorting --sizes "1000 10001 1000 7" # Example
   ```

- **Or just use the temporary script provided in `Scripts` directory**
   ```sh
   Scripts\run_sorting_analysis.bat
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
- A set of plots showing the time complexity of different sorting algorithms across varying input sizes.
- Insight into the efficiency of each algorithm under different conditions.

### Contributions
- **Contributor**: Juan Esteban Medina Rivas
- **Professor**: Rafael Alberto Niquefa Velasquez
- **Institution**: Escuela Colombiana de Ingeniería Julio Garavito

---
More algorithms and experiments could be added as the project progresses.

