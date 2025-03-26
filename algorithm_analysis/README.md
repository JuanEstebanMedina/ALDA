# Algorithm Analysis

## Sorting Algorithm Comparison

This project focuses on the experimental analysis of different sorting algorithms. The objective is to compare their performance under various conditions and visualize the results using data plots.

### Implemented Sorting Algorithms
- **Bubble Sort**: A simple comparison-based algorithm with O(n²) complexity.
- **Merge Sort**: A divide-and-conquer algorithm with O(n log n) complexity.
- **Quick Sort**: An efficient sorting algorithm with an average complexity of O(n log n).
- **Other algorithms may be included for additional comparisons.**

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

### How to Run
1. **Install dependencies**
   ```bash
   poetry install  # If using poetry
   pip install -r requirements.txt  # If using a requirements file
   ```
2. **Run the sorting analysis**
   ```bash
   python algorithm_analysis/experiments/sorting_analysis.py
   ```
3. **Run unit tests**
   ```bash
   pytest algorithm_analysis/tests/
   ```

### Expected Results
- A set of plots showing the time complexity of different sorting algorithms across varying input sizes.
- Insight into the efficiency of each algorithm under different conditions.

### Contributions
- **Contributor**: Juan Esteban Medina Rivas
- **Professor**: Rafael Alberto Niquefa Velasquez
- **Institution**: Escuela Colombiana de Ingeniería Julio Garavito

---
More algorithms and experiments will be added as the project progresses.

