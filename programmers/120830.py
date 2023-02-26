def solution(n, k):
    service_k = n // 10
    return n * 12_000 + (max(k - service_k, 0)) * 2_000
