'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
10 1 9 2 8 3 7 4 6 5
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.
'''
import math

T = int(input()) 
arr = [[]]*T # 요구된 양식에 맞게 출력하기 위해 2차원 배열 선언

for i in range(T): # T회 반복
    if 1<= T <=50: # T의 제약조건
        N = int(input()) # N 입력

        if 10 <= N <= 100: # N 제약조건
            a = list(map(int, input().split())) # a 입력
            a.sort() # 사용자 임의 정렬을 쉽게 하기 위해 a 정렬
            
            if len(a) == N: # a의 개수와 N이 같다면 앞으로 진행
                '''
                ex)
                a       2   3   5   7   1   4   6   <- 원래 순서
                a'      1   2   3   4   5   6   7   <- 오름차순 정렬
                
                k       0   0   1   1   2   2   3
                N_new   N-1 0   N-1 0   N-1 0   N-1
                index   N-1 0   N-2 1   N-3 2   N-4 <- 요구사항에서 주어진 순서
                에 착안하여 변수 설정
                '''
                N_new = [0]*N 
                k = [0]*N 
                index = [0]*N 
                temp_arr = [0]*N 

                for j in range(N): # N 만큼 반복
                    k[j] = math.floor(j/2) # k에는 N/2의 몫의 값
                    if j % 2 == 0: # 만약 j가 짝수면
                        N_new[j] = N-1
                        index[j] = N_new[j] - k[j]
                    elif j % 2 == 1: # 만약 j가 홀수면
                        N_new[j] = 0
                        index[j] = k[j]
                    # temp_arr에는 조건에 맞는 정렬 리스트
                    temp_arr[j] = (a[index[j]])
                # 이후 출력을 위해 2차원 배열에 요구사항대로 정렬된 리스트 할당
                arr[i] = temp_arr


# 양식에 맞게 출력
for i in range(T):
    print("#{0}".format(i+1), end=" ")
    end = len(arr[i])
    if end > 10:
        end = 10
    
    for j in range(end):
        print("{0}".format(arr[i][j]), end=" ")
    print()

