'''
사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다. 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다. 게임 룰은 다음과 같다.
1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.
그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.

두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다.
다음은 4명이 카드를 비교하는 경우로, 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다. 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는 바꾸지 않는다.
N명이 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만드시오.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 인원수 N과 다음 줄에 N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100
카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 1등의 번호를 출력한다.

[입력 예]
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3

[출력 예]
#1 3
#2 5
#3 1
'''
def RPCWinner(a, b):
    # 1, 2, 3 각각 가위 바위 보
    if a == 1:
        if b == 1: return a
        elif b == 2: return b
        elif b == 3: return a
    elif a == 2:
        if b == 1: return a
        elif b == 2: return a
        elif b == 3: return b
    elif a == 3:
        if b == 1: return b
        elif b == 2: return a
        elif b == 3: return a

def TrackWinner(i, j):
    if i == j:
        return i
    
    # 정복분할 방법 활용
    m = (i+j)//2
    left = TrackWinner(i, m)
    right = TrackWinner(m+1, j)

    # 가위바위보를 이긴 플레이어의 정보를 추출
    if players[left] == RPCWinner(players[left], players[right]): return left
    else: return right
        
T = int(input())
for t in range(T):
    N = int(input())
    RPC = list(map(int, input().split()))
    
    # N명의 플레이어가 각각 뽑은 숫자카드를 가진다.
    players = {}
    for i in range(N):
        players[i+1] = RPC[i]

    print( "#{0} {1}".format(t+1, TrackWinner(1, N)) )
    