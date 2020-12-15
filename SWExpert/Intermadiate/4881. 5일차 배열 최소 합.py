'''
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
 
예를 들어 다음과 같이 배열이 주어진다.
2 1.2
5.8 5
7 2 2.
이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.

입력
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

출력
#1 8
#2 14
#3 9
'''

def findMinSum(x, y):
    m = 9 * N
    result = m
    dx = [1, 0]
    dy = [1, 0, -1]
    if 0 <= x < N and 0 <= y < N:
        if visited[x][y] == False:
            for i in range(x, N): visited[i][y] = True
            for j in range(y, N): visited[x][j] = True

            for ddx in dx:
                for ddy in dy:
                    if result <= m:
                        m = result
                        result = a[x][y] + findMinSum(x+ddx, y+ddy)
                    else:
                        result = a[x][y] + findMinSum(x+ddx, y+ddy)
                    return result
    else:
        return 0

T = 1 # int(input())
for t in range(T):
    N = 3
    a = []
    # for _ in range(N):
    #     a.append(list(map(int, input().split())))
    a = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]

    visited = [[False for i in range(N)] for j in range(N)]
    print(findMinSum(0,0))
    #print("#{0} {1}".format(t+1, findMinSum()))

# 
# 4881 D2 배열 최소 합
 
def dfs(idx, _sum):
    global min_result
    if idx == N:
        if _sum < min_result:
            min_result = _sum
        return
    #가지치기
    if _sum >= min_result:
        return
    for i in range(N):
        #갔던 세로줄은 사용불가하게 바꾸기
        if use_check[i]:
            use_check[i] = False
            dfs(idx+1, _sum + map_list[idx][i])
            use_check[i] = True
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    use_check = [True for _ in range(N)]
    min_result = 987654321 
    dfs(0, 0)
    print("#{} {}".format(t, min_result))