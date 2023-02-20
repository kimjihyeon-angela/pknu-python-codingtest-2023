# 백준 1253  좋은 수 찾기
import sys
input = sys.stdin.readline

N = int(input())
count = 0
A = list(map(int, input().split()))         # 한줄에 입력을 다 받을 때
A.sort()                                    # sort(revers=False..?) 역순 정렬

for k in range(N):
    find = A[k]
    i = 0                                   # i는 리스트 첫번째
    j = N-1                                 # j는 리스트의 마지막 번째 위치
    while i < j:                            # 두 인덱스가 만나면 while문 종료
        if A[i] + A[j] == find:             # 두 수의 합이 찾는 수랑 일치 
            if i != k and j != k:           # i, j는 k와 같은 위치가 되면 안됨
               count += 1
               break
            elif i == k:
                i += 1
            elif j == k:
                j-= 1 
        elif A[i] + A[j] < find:            # 두 수의 합이 find보다 작을 때 i를 증가시켜야 합의 수가 커짐
            i += 1
        elif A[i] + A[j] > find:            # 두 수의 합이 find보다 클 때 j를 감소시켜야 합의 수가 작아짐
            j -= 1

print(count)