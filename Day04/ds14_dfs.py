# 깊이 우선 탐색
class Graph:
    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)] # 2차원배열

# 전역변수
G1 = None
stack = []      # dfs를 위한 스택
visitedAry = [] # 방문 기록
A, B, C, D = 0, 1, 2, 3
# 메인코드
if __name__ == '__main__':
    G1 = Graph(4)   
    G1.graph[A][C] = 1 ; G1.graph[A][D] = 1
    G1.graph[B][C] = 1
    G1.graph[C][A] = 1; G1.graph[C][B] = 1; G1.graph[C][D] = 1
    G1.graph[D][A] = 1; G1.graph[D][C] = 1
    
    print('G1 무방향 그래프')
    for item in G1.graph:
        print(item)    

    current = A        # 시작 정점
    stack.append(current)
    visitedAry.append(current)  # 스택, 방문기록에 A넣음

    while(len(stack) != 0):     # 스택이 0이 되면 끝
       next = None
       for vertext in range(G1.SIZE):
        if G1.graph[current][vertext] == 1: # 엣지가 있으면
            if vertext in visitedAry : # 이미 방문한 경우 pass
                pass
            else: # 방문한 적 없는 경우 다음 정점으로 지정
                next = vertext
                break   # for문 완전 빠져나감
        
        if next != None: # 다음 방문할 정점이 있으면
            current = next
            stack.append(current)
            visitedAry.append(current)
        else: # 다음 방문할 정점이 없는 경우
            current = stack.pop() # 스택에서 제일 위에값 꺼내옴

    print('방문순서 -->', end=' ')
    for i in visitedAry:
        print(chr(ord('A')+i), end=' -> ')
    

