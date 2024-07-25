def solution(num_list):
    product = 1 
    sum_elements = 0 
    for i in num_list:
        product *= i  
        sum_elements += i  
    if product < sum_elements**2:
        return 1
    else:
        return 0

