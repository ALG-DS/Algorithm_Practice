'''
두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.
파이썬의 경우 딕셔너리를 이용할 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M

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
#1 2
#2 1
#3 3
'''
T = int(input()) # T 받기
for i in range(T): # T 회 반복
    str1 = input() # str1 입력
    str2 = input() # str2 입력
    str1_index = list(set(str1)) # str1의 인덱스
    temp = [] # 등장 횟수 저장할 리스트
    for j in str1_index: # str1의 인덱스가
        temp.append(str2.count(j)) # str2에 몇번 카운팅 되는지
    print("#{0} {1}".format(i+1, max(temp) )) # 요구에 맞게 프린트
