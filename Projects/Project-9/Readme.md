# Sales Data Analyzer

A Python-based **Sales Data Analyzer** that uses Pandas, NumPy, Matplotlib, and Seaborn to load, explore, clean, manipulate, visualize, and save sales data.

## Features

* Load CSV dataset
* Explore dataset
* Display first and last 5 rows
* Display column names
* Display data types
* Display dataset information
* Perform DataFrame operations
* Add new columns
* Delete columns
* Rename columns
* Sort data
* Select columns
* Handle missing data
* Fill missing numerical values with mean
* Remove rows containing missing values
* Replace missing values with a specific value
* Generate different visualizations
* Bar Plot
* Line Plot
* Scatter Plot
* Pie Chart
* Histogram
* Stack Plot
* Save visualizations as PNG, JPG, or JPEG

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

## Project Structure

```text
Sales-Data-Analyzer/
│
├── sales_data_analyzer.py
├── sales_data.csv
├── README.md
└── plots/
```

## Installation

Make sure Python is installed on your computer.

Install the required libraries using:

```bash
pip install pandas numpy matplotlib seaborn
```

## How to Run

Run the Python program:

```bash
python sales_data_analyzer.py
```

## Main Menu

```text
========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Data Visualization
6. Save Visualization
7. Exit
==========================================================
```

## Dataset

The program accepts a **CSV file** as input.

Example:

```text
sales_data.csv
```

When the program asks for the dataset path, enter:

```text
sales_data.csv
```

## Visualization

The project supports the following plots:

### Bar Plot

Used to compare values between different categories.

### Line Plot

Used to show trends and changes in data.

### Scatter Plot

Used to identify relationships between two numerical columns.

### Pie Chart

Used to show the proportion of different categories.

### Histogram

Used to show the frequency distribution of numerical data.

### Stack Plot

Used to compare multiple numerical values over an index.

## Missing Data Handling

The program provides different options for missing values:

* Display rows containing missing values
* Fill numerical missing values with the mean
* Remove rows containing missing values
* Replace missing values with a specific value

## Example Workflow

```text
1. Load Dataset
        ↓
2. Explore Data
        ↓
3. Perform DataFrame Operations
        ↓
4. Handle Missing Data
        ↓
5. Data Visualization
        ↓
6. Save Visualization
        ↓
7. Exit
```

## Output

The program displays results directly in the terminal and opens graphs using Matplotlib.

Saved visualizations can be stored as:

```text
plot.png
plot.jpg
plot.jpeg
```

## Author

**Hardvi Bhatti**

## License

This project is created for educational and academic purposes.
