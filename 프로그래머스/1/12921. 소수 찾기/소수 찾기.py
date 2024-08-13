def solution(n):
    if n < 2:
        return 0
    
    # n+1 크기의 배열을 생성하고 True로 초기화
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아니므로 False로 설정
    
    # 2부터 √n까지의 숫자에 대해 작업 수행
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:  # i가 소수라면
            for j in range(i*i, n + 1, i):  # i의 배수를 모두 False로 설정
                sieve[j] = False
    
    # True 값의 개수(소수의 개수)를 반환
    return sum(sieve)

