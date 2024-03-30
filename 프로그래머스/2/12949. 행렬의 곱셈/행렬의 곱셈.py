
def solution(arr1,arr2):
    r1,r2 = len(arr1),len(arr2)  
    c1,c2 = len(arr1[0]),len(arr2[0])
    ret = [[0]*c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(r2):
            for k in range(c1):
                ret[i][j] += arr1[i][k]*arr2[k][j]
    return ret