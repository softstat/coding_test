def solution(n):
    sol = []
    for i in str(n):
        sol.append(i)
    sol.sort(reverse=True)
    ch = ''.join(sol)
    return int(ch)
