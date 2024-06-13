
# Firearm Analysis Project

## Overview

This project aims to analyze firearm background checks in the United States. It processes and examines data on firearm permits, handguns, and long guns by state and year, providing insights into trends and patterns across different states.

## Features

- Read and clean data from CSV files
- Process date information for better analysis
- Group data by state and year for aggregated insights
- Identify states and years with the highest number of firearm permits and sales
- Conduct temporal analysis to understand trends over time
- Perform state-wise analysis and handle outliers
- Merge data with population information for relative comparisons
- Generate choropleth maps for visual representation of firearm data

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Steps

1. Clone the repository or download the project files:
    ```bash
    git clone https://github.com/Paulpott500/datascienceprogramming/firearm_analysis_project.git
    cd firearm_analysis_project
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install the package in editable mode:
    ```bash
    pip install -e .
    ```

## Usage

### Running the Analysis

You can run the main script directly:

```bash
python main.py
```

Alternatively, use the console script defined in `setup.py`:

```bash
firearm_analysis
```

### Running Individual Functions

The `main.py` script is designed to run all functions sequentially. However, you can also run individual functions by calling them directly in a Python interpreter or another script.

### Example

```python
from main import read_csv, clean_csv, ...

# Read data
firearm_data = read_csv('data/nics-firearm-background-checks.csv')

# Clean data
firearm_data_cleaned = clean_csv(firearm_data)
# Continue with other functions...
```

## Data

### Firearm Background Checks

- **File**: `data/nics-firearm-background-checks.csv`
- **Source**: [Kaggle](https://www.kaggle.com/datasets/pedropereira94/nics-firearm-background-checks)
- **Description**: This dataset contains information on background checks for firearm permits, handguns, and long guns by date and state.

### State Populations

- **File**: `data/us-state-populations.csv`
- **Source**: [Gist](https://gist.githubusercontent.com/bradoyler/0fd473541083cfa9ea6b5da57b08461c/raw/fa5f59ff1ce7ad9ff792e223b9ac05c564b7c0fe/us-state-populations.csv)
- **Description**: This dataset contains the population of different US states as of 2014.

## Output

The script generates various outputs, including:

- Console logs for each step
- Plots showing trends over time
- Informative messages identifying states with the highest firearm activity
- Adjusted data after handling outliers

## Tests

### Running Tests

To run tests and check coverage, follow these steps:

1. Ensure `pytest` is installed:
    ```bash
    pip install pytest
    ```

2. Run the tests:
    ```bash
    pytest
    ```

3. Check test coverage (if coverage is configured):
    ```bash
    pytest --cov=firearm_analysis_project
    ```

### Test Coverage

The test coverage report provides details on which parts of the code are tested and the extent of the tests. Ensure that your tests cover a wide range of scenarios to maintain code quality.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please contact the project maintainer:

- Name: Your Name
- Email: your.email@example.com
- GitHub: [yourusername](https://github.com/Paulpott500/datascienceprogramming/firearm_analysis_project)

---

Thank you for your interest in the Firearm Analysis Project! We hope it provides valuable insights into firearm background checks in the United States.
