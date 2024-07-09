import re

def solution(s):
    # Replace any digit followed by 'Z' with '+'
    s = re.sub(r'\dZ', '+', s)
    
    # Split the modified string into parts
    parts = s.split()
    
    # Initialize an empty list to hold the valid numbers
    numbers = []
    
    # Iterate through each part
    for part in parts:
        if part == '+' or part == 'Z':
            # If '+' or 'Z' is found, remove the last number from the list (if any)
            if numbers:
                numbers.pop()
        else:
            try:
                # Otherwise, add the number to the list
                numbers.append(int(part))
            except ValueError:
                # Handle any part that cannot be converted to an integer
                continue
    
    # Sum up the numbers in the list
    return sum(numbers)