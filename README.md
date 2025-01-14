# Directory Size Visualizer

## Overview
The Directory Size Visualizer is a Python script that calculates the sizes of immediate subdirectories in a given directory and visualizes the size distribution using a pie chart. It supports user-defined thresholds to filter small directories, either by size in megabytes (MB) or by percentage of the total directory size.

## Features
- **Recursive Size Calculation**: Calculates the total size of all files in each subdirectory, including nested subdirectories.
- **Threshold Filtering**: Users can specify thresholds in MB or percentages to group smaller subdirectories into an "Other" category for better visualization.
- **Interactive Input**: Accepts user input for the directory path, threshold type, and value.
- **Human-Readable Output**: Displays subdirectory sizes in an easy-to-read format (e.g., MB, GB).
- **Pie Chart Visualization**: Generates a clear and proportional pie chart of subdirectory sizes.

## Requirements
- Python 3.7 or later
- `matplotlib` library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/directory-size-visualizer.git
   cd directory-size-visualizer
   ```
2. Install the required library:
   ```bash
   pip install matplotlib
   ```

## Usage
1. Run the script:
   ```bash
   python directory_visualizer.py
   ```
2. Provide the required inputs:
   - **Directory Path**: The path of the directory to analyze.
   - **Threshold Type**: Choose `MB` for size in megabytes or `%` for percentage.
   - **Threshold Value**: Enter the threshold value.

### Example
```
Enter the directory path to analyze: C:\MyDirectory
Enter the threshold type ('MB' for size in megabytes or '%' for percentage): %
Enter the threshold value (in %): 5
```
This will analyze the directory `C:\MyDirectory` and group subdirectories smaller than 5% of the total size into an "Other" category.

## Output
- **Terminal Output**: Displays the sizes of all immediate subdirectories in a human-readable format.
  ```
  Immediate subdirectory sizes:
  Subdir1: 500.00 MB
  Subdir2: 1.20 GB
  Other: 200.00 MB
  ```
- **Pie Chart**: Visualizes the size distribution of immediate subdirectories.

## Contribution
Feel free to fork the repository and submit pull requests for additional features or improvements. Suggestions and feedback are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
