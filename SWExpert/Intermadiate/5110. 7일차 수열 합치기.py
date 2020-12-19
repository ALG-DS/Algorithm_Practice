'''
여러 개의 수열을 정해진 규칙에 따라 합치려고 한다. 다음은 3개의 수열이 주어진 경우의 예이다.
 

수열 1
2 3 4 5

수열 2
4 8 7 6

수열 3
9 10 15 16

수열 4
1 2 6 5

수열 2의 첫 숫자 보다 큰 수자를 수열 1에서 찾아 그 앞에 수열 2를 끼워 넣는다.
2 3 4 '4 8 7 6' 5

합쳐진 수열에 대해, 수열 3의 첫 숫자보다 큰 숫자를 찾아 그 앞에 수열 3을 끼워 넣는다. 큰 숫자가 없는 경우 맨 뒤에 붙인다.
2 3 4 4 8 7 6 5 '9 10 15 16'

마지막 수열까지 합치고 나면, 맨 뒤의 숫자부터 역순으로 10개를 출력한다.
'1 2 6 5' 2 3 4 4 8 7 6 5 9 10 15 16

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 수열의 개수 M, 이후 M개의 줄에 걸쳐 1000이하의 자연수로 구성된 수열이 주어진다. 4<=N<=1000, 1<=M<=1000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 완성된 수열의 맨 뒤부터 10개의 숫자를 역순으로 출력한다.

[입력 예]
3
4 4
2 3 4 5
4 8 7 6
9 10 15 16
1 2 6 5
5 5
273 415 58 798 251
675 193 494 506 365
479 390 224 334 387
107 402 569 422 183
88 709 994 206 916
10 10
178 778 659 231 274 123 788 16 483 404
36 14 602 74 287 689 730 703 611 339
445 468 126 821 946 212 218 143 999 923
288 792 249 142 996 999 570 757 141 921
98 87 800 892 401 244 661 179 403 985
474 315 694 816 838 525 288 94 609 6
789 433 474 883 927 841 242 233 286 749
7 667 875 986 107 957 887 520 430 649
721 206 65 776 328 807 845 908 382 836
707 811 790 652 805 190 407 257 668 307

[출력 예]
#1 16 15 10 9 5 6 7 8 4 4
#2 251 798 365 506 494 193 675 387 334 224
#3 404 483 16 788 123 274 231 659 778 178
'''

T = int(input())

for t in range(1, T+1):
    # N 수열의 길이, M 수열의 갯수
    N, M = map(int, input().split())

    # 모든 리스트들을 저장
    lst = []
    for m in range(M):
        lst.append(list(map(int, input().split())))
    
    # 리스트가 둘 이상 있으면 비교 진행
    while len(lst) > 1:
        # 비교에 성공했는지 여부를 저장하기위해 -1로 초기화 (비교 후에도 -1이면 맨 뒤로 보내서 append)
        idx = -1

        # 
        for i in range(len(lst[0])):
            if lst[0][i] > lst[1][0]:
                idx = i
                # 끼워 넣기
                lst[0][idx:idx] = lst[1]
                # 끼워넣고 나면 비교 리스트 삭제
                lst.pop(1)
                break
        # 비교에 실패했다면 맨 뒤로 보내서 append
        if idx == -1:
            for j in lst[1]:
                lst[0].append(j)
            # 넣고 나면 비교리스트 삭제
            lst.pop(1)

    result = lst[0][:]
    joined_result = ' '.join(map(str, result[::-1][:10]))

    print("#{0} {1}".format(t, joined_result))


'''
# 5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기
 
 
class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new
 
    if lst.head is None:
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]: break
            cur = cur.next
        if cur is None: # 뒤에 # 순서주의
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur.prev is None: # 앞에 
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else: # 중간에 추가
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)
 
def printList(lst):  # 연결리스트 출력
    if lst.head is None:
        return
    cur = lst.tail
    cnt = 10
    while cnt: # 역방향
        print(cur.data, end=' ')
        cur = cur.prev
        cnt -= 1
    print()
 
# import sys
# sys.stdin = open('input.txt')    
 
for tc in range(1,int(input())+1):
    n,m=map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(m)) # 2차원배열로 받기
    mylist = LinkedList()
    for i in range(m):
        addList(mylist, arr[i])
    print(f'#{tc}', end=' ')
    printList(mylist)

'''