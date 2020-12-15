'''
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력 예]
입력
3
6 5 # E V
1 4
1 3
2 3
2 5
4 6
1 6 # S G
7 4 # E V
1 6
2 3
2 6
3 5
2 5 # S G
9 9 # E V 
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9 # S G

[출력 예]
#1 1
#2 1
#3 1
'''
'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6 
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''

def DSF(v):
    visited[v] = False
    for i in graph[v]:
        if visited[i]:
            DSF(i)

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    stack= []
    graph = [[] for _ in range(V+1)]
    visited = [True for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b) # 단방향 그래프이므로 하나만 추가한다.
    start, end = map(int, input().split())
    DSF(start)
    result = 1

    if visited[end]:
        result = 0
    print("#{} {}".format(t+1, result))


'''
### 마코프 체인 runtime error
# V : 노드의 개수
# E : 간선의 개수
import numpy as np

T = int(input())
for t in range(T):
    V, E = list(map(int, input().split()))
    marcov_1 = np.zeros(shape = (V,V))
    marcov_2 = marcov_1
    for i in range(E):
        x, y = list(map(int, input().split()))
        marcov_1[x-1][y-1] = marcov_1[y-1][x-1] = 1
    
    S, G = list(map(int, input().split()))
    for i in range(V):
        if marcov_2[S-1][G-1] != 0:
            result = 1
            break
        elif np.sum(marcov_2) == 0:
            result = 0
            break
        else:
            result = 0
        marcov_2 = np.dot(marcov_1, marcov_2)

    print("#{0} {1}".format(t+1, result))
    '''

'''
선용 알고리즘
'''
'''
def DFS(START):
    visited[START] = True#방문리스트에 시작노드를 넣어준다.
    result = 0
    if START in my_map: # 시작하는 노드가 있다면. 즉 없으면 result는 0으로 반환한다
        for NEXT in my_map[START]:#S에서 연결되는 노드들을 하나씩 NEXT에 넣어서 G와 맞는지 비교한다.
            if not visited[NEXT]:#방문리스트에 NEXT에 해당하는 값이 false라면
                if NEXT == G:
                    return 1 # S,G가 연결이 가능하기 때문에 1을 반환시켜준다.
                elif not result: # 결과가 안났다면 계속 탐색
                    result += DFS(NEXT)#S의 노드에서 이어지는 노드에서 도착노드(G)까지 이어질 수 있는 확인
    return result

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    
    my_map = {} # 딕셔너리
    visited = [False for _ in range(V + 1)]#노드애서 연결된 도착 노드의 리스트
    result = 0
    
    for _ in range(E):
        Start, End = map(int, input().split())
        if Start not in my_map:#시작노드에서 도착하는 노드의 리스트를 value값으로 넣는다
            my_map[Start] = [End]
        else:
            my_map[Start].append(End)
        
    S, G = map(int, input().split())
    print('#{} {}'.format(test_case, DFS(S)))
    '''