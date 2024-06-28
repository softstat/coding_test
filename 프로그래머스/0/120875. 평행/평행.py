def solution(dots):
    def slope_equal(p1, p2, p3, p4):
        return (p2[1] - p1[1]) * (p4[0] - p3[0]) == (p4[1] - p3[1]) * (p2[0] - p1[0])
    
    # Unpack the dots
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = dots
    
    # Check all pairs of lines
    if slope_equal((x1, y1), (x2, y2), (x3, y3), (x4, y4)):
        return 1
    if slope_equal((x1, y1), (x3, y3), (x2, y2), (x4, y4)):
        return 1
    if slope_equal((x1, y1), (x4, y4), (x2, y2), (x3, y3)):
        return 1
    
    return 0

dots = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(solution(dots))  
