'''두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
ABC
ZZZZZABCZZZZZ
두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
ABC
ZZZZAZBCZZZZZ
문자열이 일치하지 않으므로 0을 출력.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력 예]
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW

[출력 예]
#1 1
#2 0
#3 1
'''
T = int(input()) # T 입력
for j in range(T): # T 회 반복 입력
    str1 = input() # 비교문자열
    str2 = input() # 피비교문자열
    N = len(str1)
    M = len(str2)
    count = 0 # 일치 문자열 갯수 카운트
    new_index = N-1 # str1과 비교하기위해 str2를 같은 크기로 슬라이싱하기 위해 선언

    while new_index < M: # 슬라이싱 인덱스가 str2의 길이를 넘어가면 종료
        same_letter = 0 # 같은 문자가 있는지 여부
        idx = 0 # 보이어-무어 알고리즘에 따라 몇 개의 위치를 이동할지 결정
        order = -1 # str1의 각 문자들의 위치를 결정하기 위한 변수, index("A")로 하면 ABA의 경우 1만을 반환하기에 만들어준 변수
        # str1과 같은 크기로 자른 str2가 일치하면
        if str2[(new_index+1 - N):(new_index+1)] == str1: 
            count += 1 # 하나 세고
            idx = N # str1 크기만큼 우측이동
        # str1과 같은 크기로 자른 str2가 일치하지 않으면
        else:
            # str1의 마지막 문자빼고 비교
            for i in str1[:-1]: 
                order += 1 # str1의 각 문자요소들의 index를 저장
                # str1의 order번째 요소가 슬라이싱된 str2에 있다면
                if i in str2[(new_index+1 - N):(new_index+1)]:
                    idx = N-1 - order # str2상에서 N-1 - order만큼 우측이동해서 다시 비교
                    same_letter += 1 # 같은 문자가 존재한다는 것을 알려줌
                # 같은 문자가 하나도 발견되지 않았다면
                elif same_letter == 0:
                    idx = N # N만큼 그냥 이동해
        new_index += idx # 오른쪽으로 idx만큼 이동해서 다시 슬라이싱
    print("#{0} {1}".format(j+1, count))