def solution(data, ext, val_ext, sort_by):
    # 각 필드에 대응하는 인덱스를 사전으로 정의
    field_indices = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    # ext에 해당하는 인덱스를 찾아 필터링
    ext_index = field_indices[ext]
    filtered_data = [item for item in data if item[ext_index] < val_ext]
    
    # sort_by에 해당하는 인덱스를 찾아 정렬
    sort_index = field_indices[sort_by]
    sorted_data = sorted(filtered_data, key=lambda x: x[sort_index])
    
    return sorted_data
