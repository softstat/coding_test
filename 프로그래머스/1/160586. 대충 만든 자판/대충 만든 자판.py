def solution(keymap, targets):
    # 문자가 최소 몇 번 눌려야 나오는지를 기록하는 사전 생성
    min_press = {}
    
    # keymap의 각 키에 대해 문자가 몇 번째에 나오는지 확인하여 사전에 기록
    for key_index, keys in enumerate(keymap):
        for i, char in enumerate(keys):
            # 최소 횟수를 저장
            if char not in min_press:
                min_press[char] = i + 1  # 0-based index니까 +1
            else:
                min_press[char] = min(min_press[char], i + 1)
    
    # 결과를 저장할 리스트
    result = []
    
    # targets의 각 문자열에 대해 필요한 최소 키 입력 수 계산
    for target in targets:
        total_presses = 0
        for char in target:
            if char in min_press:
                total_presses += min_press[char]
            else:
                # 만들 수 없는 문자열이면 -1 저장하고 break
                total_presses = -1
                break
        result.append(total_presses)
    
    return result
