# 백준 1541 - 잃어버린 괄호
answer = 0
A = list(map(str, input().split('-'))) # - 기준으로 잘라서 문자열로 리스트

def mySum(i):                          # - 로 나눈 각 수식 문자열 합 구하기 함수
    result = 0
    temp = str(i).split('+')           # + 기준으로 수식 자르기
    
    for k in temp:
        result += int(k)               # 문자열로 결과 나옴 => 안더해지는 것은 아님 => 문자열 더해지는 것으로 숫자 더하기와 다름
    
    return result

for s in range(len(A)):
    temp = mySum(A[s])

    if s == 0:
        answer += temp                # 맨 처음 값이기 때문
    else:
        answer -= temp

print(answer)