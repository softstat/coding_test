def solution(bin1, bin2):
    # Convert binary strings to integers
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    
    # Perform the addition
    sum_num = num1 + num2
    
    # Convert the result back to a binary string
    result = bin(sum_num)[2:]  # bin() returns a string starting with '0b'
    
    return result
