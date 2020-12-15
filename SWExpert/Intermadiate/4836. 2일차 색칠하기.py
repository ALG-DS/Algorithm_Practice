'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
주어진 정보에서 같은 색인 영역은 겹치지 않는다.

예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
2
2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
color = 1 (빨강), color = 2 (파랑)

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력 예]
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2

[출력 예]
#1 4
#2 5
#3 7
'''

T = int(input())
for i in range(T): # T회 반복
    N = int(input()) # N개의 숫자 입력
    coord1 = [] # 빨간색 좌표
    coord2 = [] # 파란색 좌표
    for j in range(N): # N번 반복
        r1, c1, r2,  c2, color = list(map(int, input().split()))
        # 빨간색일때
        if color == 1: 
            # 입력 받은 좌표로 모든 빨간색 좌표 생성
            for k in range(r1, r2+1):
                for l in range(c1, c2+1):
                    # 만약 기존 빨간색과 겹친다면 좌표 생성 하지 않음
                    if [k,l] in coord1: pass
                    else: coord1.append([k,l])
        # 파란색일때
        elif color == 2:
            # 입력 받은 좌표로 모든 파란색 좌표 생성
            for k in range(r1, r2+1):
                for l in range(c1, c2+1):
                    # 만약 기존 파란색과 겹친다면 좌표 생성 하지 않음
                    if [k,l] in coord2: pass
                    else: coord2.append([k,l])
    purple = []
    # 빨간색 좌표들에 대해서
    for k in coord1:
        # 만약 그 좌표가 파란색에도 있다면
        if k in coord2:
            # 그건 보라색일 것
            purple.append(k)
    # 요구에 맞게 출력
    print("#{0} {1}".format(i+1, len(purple)))
