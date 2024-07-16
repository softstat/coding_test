def solution(numbers):
    products = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = numbers[i] * numbers[j]
            products.append(product)
    
    return max(products)
