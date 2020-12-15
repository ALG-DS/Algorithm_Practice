'''
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.

노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
두 노드 S와 G가 서로 연결되어 있지 않다면, 0을 출력한다.

[입력 예]
3
6 5 V E
1 4
1 3
2 3
2 5
4 6
1 6 S G
7 4 V E
1 6
2 3
2 6
3 5
1 5 S G
9 9 V E
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9 S G

[출력 예]
#1 2
#2 4
#3 3
'''

'''
6 5
1 3
1 4
2 3
2 5
4 6
1 6

7 4
1 6
2 3
2 6
3 5
1 5
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
# def BFS(S, G):
#     count = 0
#     visited[S] = True

#     while len(node[S]) > 0:
#         lst.append(node[S].pop(0))

#     S = search(S)

#     if visited[S] == False:
#         if S != G:
#             return BFS(S, G) + count
#         else:
#             return 1

# def search(S):
#     if visited[S] == False and len(lst):
#         return S
#     else:
#         lst.pop(0)
#         S = lst.pop(0)
#         search(S)

# T = 1 # int(input())

# for t in range(1, T+1):
#     V, E = list(map(int, input().split()))
    
#     node = {}
#     for i in range(1, V+1):
#         node[i] = []

#     for e in range(E):
#         i, j = list(map(int, input().split()))
#         # dictionary로 이어진 노드를 표시함
#         node[i].append(j)
#         node[j].append(i)


#     S, G = list(map(int, input().split()))
#     lst = []
#     visited = [False for _ in range(E+1)]
#     result = BFS(S, G)

#     print("#{0} {1}".format(t, result))

def BFS(start_node):
    global result
    Q.append(start_node)
    visited[start_node] = 1

    while Q:
        start_node = Q.pop(0)
        for next_node in range(1, v+1):
            if MyMap[start_node][next_node] and not visited[next_node]:
                Q.append(next_node)
                visited[next_node] = 1
                distance[next_node] = distance[start_node]+1
                if next_node == end_node:
                    result = distance[next_node]
                    return
    return  # 간선이 연결되지 않은 경우


TC = 1 #int(input())
for tc in range(1, TC+1):
    v, e = map(int, input().split())
    MyMap = [[0]*(v+1) for _ in range(v+1)]  # 계산의 편의를 위해, 앞 뒤로 0을 하나씩 더
    visited = [0] * (v+1)
    distance = [0] * (v+1)
    # 간선표시
    for i in range(e):
        start, end = map(int, input().split())
        MyMap[start][end] = 1
        MyMap[end][start] = 1
    #시작노드, 도착노드
    start_node, end_node = map(int, input().split())

    Q = []
    result = 0
    BFS(start_node)
    print(f'#{tc} {result}')
