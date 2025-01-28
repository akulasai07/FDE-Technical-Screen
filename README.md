# Robotic Package Sorter

## Objective

This project is part of Thoughtful’s robotic automation factory. The goal is to implement a function for a robotic arm to dispatch packages to the correct stack based on their volume and mass.

## Sorting Rules

Packages are sorted into three stacks based on the following criteria:

- **Bulky**:
  - The package volume (Width × Height × Length) is **≥ 1,000,000 cm³**, or
  - Any dimension (Width, Height, or Length) is **≥ 150 cm**.
- **Heavy**:
  - The package mass is **≥ 20 kg**.

### Stack Categories

1. **STANDARD**: Packages that are neither bulky nor heavy.
2. **SPECIAL**: Packages that are either bulky or heavy.
3. **REJECTED**: Packages that are both bulky and heavy.

## Function Implementation

The function `sort(width, height, length, mass)` is implemented in Python. It takes four arguments:

- `width`: The package width in centimeters.
- `height`: The package height in centimeters.
- `length`: The package length in centimeters.
- `mass`: The package mass in kilograms.

The function returns one of the following strings:

- `"STANDARD"`
- `"SPECIAL"`
- `"REJECTED"`

## Usage

1. Clone the repository or download the script.
2. Run the script in a Python environment.
3. Use the `sort` function with the desired package dimensions and mass.

### Example Usage
```python
print(sort(200, 200, 200, 30))  # Expected: REJECTED (bulky and heavy)
print(sort(100, 100, 100, 10))  # Expected: SPECIAL (bulky but not heavy)
print(sort(300, 100, 50, 15))   # Expected: SPECIAL (bulky but not heavy)
print(sort(100, 100, 100, 25))  # Expected: REJECTED (bulky and heavy)
print(sort(10, 100, 100, 2))    # Expected: STANDARD (neither bulky nor heavy)
