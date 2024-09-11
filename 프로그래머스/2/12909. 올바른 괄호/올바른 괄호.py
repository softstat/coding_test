def solution(s):
    st = []
    
    for i in s:
        if i == "(":
            st.append(i)
        elif i == ")":
            if not st:
                return False
            st.pop()
    
    return len(st) == 0
