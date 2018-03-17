def solution(A, B, K):
    na = A // K
    nb = B // K
    la = 0
    if not na % K:
        la = 1
    return nb - na + la
