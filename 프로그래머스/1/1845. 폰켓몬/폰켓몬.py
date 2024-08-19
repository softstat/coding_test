def solution(nums):
    unique_elements = set(nums)
    max_selectable = len(nums) // 2
    return min(len(unique_elements), max_selectable)
