#!/bin/bash

# Define the README file name
README_FILE="README.md"

# Write content to the README file
cat <<EOL > $README_FILE
# Robotic Package Sorter

## Objective

This project is part of Thoughtful's robotic automation factory. It involves implementing a function for a robotic arm to dispatch packages to the correct stack based on their volume and mass.

## Sorting Rules

- A package is **bulky** if:
  - Its volume (Width × Height × Length) is ≥ 1,000,000 cm³, or
  - Any dimension (Width, Height, or Length) is ≥ 150 cm.
- A package is **heavy** if:
  - Its mass is ≥ 20 kg.

### Dispatch Stacks

1. **STANDARD**: Packages that are neither bulky nor heavy.
2. **SPECIAL**: Packages that are either bulky or heavy.
3. **REJECTED**: Packages that are both bulky and heavy.

## Function Implementation

The `sort(width, height, length, mass)` function is implemented in Python. It returns the name of the stack where the package should be dispatched (`"STANDARD"`, `"SPECIAL"`, or `"REJECTED"`).

## Usage

1. Clone the repository or download the Python script.
2. Run the Python script to test the function with different package dimensions and masses.

### Example
```python
print(sort(200, 200, 200, 30))  # Output: "REJECTED"
print(sort(100, 100, 100, 10))  # Output: "STANDARD"
print(sort(300, 100, 50, 15))   # Output: "SPECIAL"
