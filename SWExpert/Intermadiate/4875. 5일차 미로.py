'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

[입력 예]
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

[출력 예]
#1 1
#2 1
#3 0
'''
# maze에서 시작점 2 를 찾기 위한 함수
def StartPoint(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return [i, j]

# Depth-First Search, 시작점의 x, y 좌표를 처음 받아옴
def DFS(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 방문 기록을 가진 visited
    if not visited[x][y]:
        visited[x][y] = True

        # 우, 좌, 하, 상의 순서로 탐색을 실시
        for ddx, ddy in zip(dx, dy):
            # x, y 좌표를 갱신하여
            x_p = x + ddx
            y_p = y + ddy
            # 미로를 벗어나지 않는 범위에서
            if  0 <= x_p < N:
                if 0 <= y_p < N:
                    # 갱신된 x, y 좌표에 도착점 3이 있다면
                    if maze[x_p][y_p] == '3':
                        # 이번 DFS는 True
                        return True
                    # 갱신된 x, y 좌표가 이전에 방문한 적이 없다면
                    elif not visited[x_p][y_p]:
                        # DFS로 한번더 가서 탐색
                        keep = DFS(x_p, y_p)
                        # DFS 탐색에서 돌아와서 keep에 True가 있다면
                        # 그 이전 DFS에 True 반환
                        if keep: return True
      
T = int(input())
for t in range(T):
    N = int(input())

    # 방문 정보를 가진 행렬 선언
    visited = [[False for i in range(N)] for j in range(N)]

    # 미로 생성
    maze = []
    for _ in range(N):
        maze.append(input())
        # maze.append(list(int(input())))
    # 시작점(2) 찾기
    x, y = StartPoint(maze)
    # 미로에 1인 부분은 벽으로 미리 방문한 것(True)으로 가정하여 진행
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '1':
                visited[i][j] = True

    # 입구(2)와 출구(3)를 이을 수 있다면 1 반환
    if DFS(x, y): result = 1
    else: result = 0

    print("#{0} {1}".format(t+1, result))
    