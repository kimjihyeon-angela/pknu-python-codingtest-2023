# python-codingtest-2023
파이썬 코딩테스트 리포지토리

## 1일차
1. 코딩테스트 소개
2. 코딩테스트 학습
    - 자료구조 - 배열/리스트
    - 구간합

## 2일차
1. 코딩테스트 소개
2. 코딩테스트 학습
    - 자료구조 다시
        - 연결리스트
        - 스택
        - 큐
        - pythonds 스택 확인

## 3일차
1. 코딩 테스트 학습
    - 자료 구조
        - 큐
        - pythonds 큐 확인
        - 이진트리
            - 삭제는 연결리스트 삭제와 유사
        - 그래프

## 4일차
1. 코딩테스트 학습
    - 자료구조
        - 그래프 - DFS
        - 재귀호출
        - 정렬소개

## 5일차
1. 코딩테스트 학습
    - 자료구조
        - 정렬
        - 검색
        - 다이나믹 프로그래밍

## 6일차
1. 코딩테스트 학습
    - 자료구조
        - deque (덱)
    - 코딩테스트 알고리즘
        - 백준
        - 프로그래머스
```python
# 백준 11003 최솟값 찾기
from collections import deque

N, L = map(int,input().split())
mydeque = deque()
now = list(map(int, input().split())) 

# 새 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거해 시간복잡도 줄임
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')
```



