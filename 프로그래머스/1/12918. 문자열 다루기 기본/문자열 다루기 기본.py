def solution(s):
    if isinstance(s, str) and len(s) in (4, 6) and s.isdigit():
        return True
    else:
        return False

