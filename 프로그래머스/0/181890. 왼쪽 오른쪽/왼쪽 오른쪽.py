def solution(str_list):
    for idx, value in enumerate(str_list):
        if value == "l":
            return str_list[:idx]
        elif value == "r":
            return str_list[idx + 1:]
    return []


