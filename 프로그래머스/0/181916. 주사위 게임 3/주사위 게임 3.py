def solution(a, b, c, d):
    if a == b == c == d:
        return 1111 * a
    elif a == b == c or a == b == d or a == c == d or b == c == d:
        # Cases where three numbers are the same
        if a == b == c:
            return (10 * a + d) ** 2
        elif a == b == d:
            return (10 * a + c) ** 2
        elif a == c == d:
            return (10 * a + b) ** 2
        else:
            return (10 * b + a) ** 2
    elif (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
        # Cases where two pairs of numbers are the same
        if a == b and c == d:
            return (a + c) * abs(a - c)
        elif a == c and b == d:
            return (a + b) * abs(a - b)
        else:
            return (a + b) * abs(a - b)
    elif a == b:
        return c * d
    elif a == c:
        return b * d
    elif a == d:
        return b * c
    elif b == c:
        return a * d
    elif b == d:
        return a * c
    elif c == d:
        return a * b
    else:
        return min(a, b, c, d)

