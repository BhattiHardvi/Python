# NumPy Analyzer

A Python-based **NumPy Analyzer** that allows users to create and work with 1D, 2D, and 3D NumPy arrays. The program provides options for indexing, slicing, mathematical operations, combining and splitting arrays, searching, sorting, filtering, and statistical calculations.

## Features

* Create 1D arrays
* Create 2D arrays
* Create 3D arrays
* Perform indexing operations
* Perform slicing operations
* Addition of arrays
* Subtraction of arrays
* Multiplication of arrays
* Division of arrays
* Dot product
* Matrix multiplication
* Combine arrays using vertical stacking
* Split arrays into multiple sections
* Search for a specific value
* Sort arrays in ascending order
* Sort arrays in descending order
* Filter values based on a condition
* Calculate sum
* Calculate mean
* Calculate median
* Calculate standard deviation
* Calculate variance

## Technologies Used

* Python
* NumPy

## Project Structure

```text
NumPy-Analyzer/
│
├── numpy_analyzer.py
└── README.md
```

## Installation

Make sure Python is installed on your computer.

Install NumPy using:

```bash
pip install numpy
```

## How to Run

Run the Python program using:

```bash
python numpy_analyzer.py
```

## Main Menu

```text
Welcome to the NumPy Analyzer!
================================

Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

## Array Creation

The program supports three types of arrays:

### 1D Array

The user enters elements separated by spaces.

Example:

```text
10 20 30 40 50
```

Output:

```text
[10 20 30 40 50]
```

### 2D Array

The user enters the number of rows, columns, and elements.

Example:

```text
Rows: 2
Columns: 3
Elements: 1 2 3 4 5 6
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

### 3D Array

The user enters depth, rows, columns, and elements.

The elements are reshaped into a 3D NumPy array.

## Indexing and Slicing

The program provides indexing and slicing operations.

### Indexing

Used to access a particular element from an array.

Example:

```python
array[1]
```

### Slicing

Used to access a range of elements.

Example:

```python
array[1:4]
```

For a 2D array:

```python
array[0:2, 1:3]
```

## Mathematical Operations

The program supports:

* Addition
* Subtraction
* Multiplication
* Division
* Dot Product
* Matrix Multiplication

For array operations, the second array must have the required size or dimensions.

## Combine and Split Arrays

### Combine Arrays

Two 2D arrays can be combined using vertical stacking.

```python
np.vstack((array1, array2))
```

### Split Array

An array can be divided into multiple sections using:

```python
np.array_split(array, sections)
```

## Search, Sort, and Filter

### Search

The program searches for a particular value using:

```python
np.where(array == value)
```

### Sort

Arrays can be sorted in:

* Ascending order
* Descending order

### Filter

The program displays values greater than a user-provided value.

Example:

```python
array[array > 50]
```

## Aggregates and Statistics

The program calculates:

### Sum

```python
np.sum(array)
```

### Mean

```python
np.mean(array)
```

### Median

```python
np.median(array)
```

### Standard Deviation

```python
np.std(array)
```

### Variance

```python
np.var(array)
```

## Example Workflow

```text
Create NumPy Array
        ↓
Indexing / Slicing
        ↓
Mathematical Operations
        ↓
Combine / Split
        ↓
Search / Sort / Filter
        ↓
Aggregates / Statistics
        ↓
Exit
```

## Error Handling

The program checks for common errors such as:

* Array not created
* Invalid number of elements
* Invalid array dimensions
* Division by zero
* Invalid user choice
* Invalid matrix multiplication dimensions

## Author

**Hardvi Bhatti**

## License

This project is created for educational and academic purposes.
