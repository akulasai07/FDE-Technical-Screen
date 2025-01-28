def sort(width, height, length, mass):
    
    # Calculate the volume of the package
    volume = width * height * length

    # Determine if the package is bulky or heavy
    is_bulky = volume >= 1_000_000 or any(dim >= 150 for dim in [width, height, length])
    is_heavy = mass >= 20

    # Dispatch the package to the correct stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Test cases to verify the function
if __name__ == "__main__":
    print(sort(200, 200, 200, 30))  # Expected: REJECTED (bulky and heavy)
    print(sort(100, 100, 100, 10))  # Expected: SPECIAL (bulky but not heavy)
    print(sort(300, 100, 50, 15))   # Expected: SPECIAL (bulky but not heavy)
    print(sort(100, 100, 100, 25))  # Expected: REJECTED (bulky and heavy)
    print(sort(10, 100, 100, 2))    # Expected: STANDARD (neither bulky nor heavy)
