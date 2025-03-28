# ALDA Project Repository

## Overview
This repository serves as a central hub for all projects related to the course. It includes documentation, code, and configurations necessary for setting up, developing, and maintaining Python-based projects.

## Project Structure
The repository follows a structured organization to facilitate navigation and maintainability:

```
ALDA/
├── algorithm_analysis/
│   ├── algorithms/          # Algorithm implementations
│   ├── experiments/         # Complexity measurement scripts
│   │   └── results/         # Saved experiment results
│   ├── plots/               # Performance analysis visualizations
│   │   └── results/         # Output plot images
│   ├── tests/               # Unit tests
│   ├── app.py               # Algorithm analysis execution
│   └── README.md            # Algorithm-specific documentation
├── env/                     # Virtual environment
├── notebooks/               # Jupyter notebooks
├── Scripts/                 # To run code and coverage
├── .gitignore               # Ignored files and directories
├── README.md                # General documentation
└── requirements.txt         # Dependencies (e.g., NumPy, Matplotlib)
```

## Setting Up the Project
Follow these steps to set up the environment and dependencies for any project in this repository:

1. **Clone the repository**
   ```sh
   git clone https://github.com/JuanEstebanMedina/ALDA.git
   cd ALDA
   ```

2. **Set up a virtual environment**
   ```sh
   python -m virtualenv env
   ```

3. **Activate the virtual environment**
   - On Windows (Command Prompt):
     ```sh
     .\env\Scripts\activate
     ```
   - On Windows (PowerShell):
     ```sh
     .\env\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```sh
     source env/bin/activate
     ```

4. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Contributors

- Juan Esteban Medina Rivas - Course Participant

## Professor

- Rafael Alberto Niquefa Velasquez - Escuela Colombiana de Ingeniería Julio Garavito

## Development Guidelines
- Follow best coding practices and maintain code readability.
- Use `black` for code formatting:
  ```sh
  black .
  ```
- Write meaningful commit messages and use branches for new features.
- Ensure all unit tests pass before pushing changes:
  ```sh
  pytest tests/
  ```

## Issues and Contributions
- Report any issues in the GitHub issue tracker.
- Pull requests should be reviewed before merging into the main branch.
