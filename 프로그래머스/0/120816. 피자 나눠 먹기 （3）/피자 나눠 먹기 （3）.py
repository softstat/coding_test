def solution(slices, n):
    total_slices_needed = n
    pizzas_needed = (total_slices_needed + slices - 1) // slices
    return pizzas_needed

