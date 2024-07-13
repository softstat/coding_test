def solution(s):
    # Count the occurrences of each character
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Collect characters that appear only once
    unique_chars = [char for char in char_count if char_count[char] == 1]
    
    # Sort the unique characters alphabetically
    unique_chars.sort()
    
    # Return the sorted characters as a single string
    return ''.join(unique_chars)

