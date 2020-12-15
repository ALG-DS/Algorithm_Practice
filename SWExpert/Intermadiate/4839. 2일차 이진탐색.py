'''
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.

책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.
'''
def BiSearch(start, end, key):
    count = 0 # 검색 횟수
    middle = (start + end) // 2 # 가운뎃 페이지

    while middle != key: # 만약 가운뎃 페이지가 찾는 페이지가 아니라면 진행
        middle = (start + end) // 2 # 가운뎃 페이지 재설정 (2회차때부터 유의미)

        if key > middle: # 찾는 값이 가운뎃 페이지보다 크다면
            start = middle # 시작점은 다시 가운뎃 페이지
        elif key < middle: # 찾는 값이 가운뎃 페이지보다 작다면
            end = middle # 끝지점이 다시 가운뎃 페이지

        count += 1 # 이러나 저러나 검색횟수 1 증가

    return count # 검색횟수를 반환함

T = int(input())
winner = [0] * T # 승자를 저장할 리스트 초기화

if 1<= T <= 50: # T 제약조건

    for i in range(T): # T회 반복
        P, A, B = list(map(int, input().split())) # P, A, B를 입력 받음

        if 1 <= P <= 1000 and 1 <= A <= 1000 and 1 <= B <= 1000: # P, A, B의 제약조건 만족시 진행
            start = 1 # 시작페이지
            end = P # 끝 페이지
            # 검색 횟수가 적으면 승리
            
            if BiSearch(start, end, A) < BiSearch(start, end, B): 
                winner[i] = "A"
            elif BiSearch(start, end, A) > BiSearch(start, end, B):
                winner[i] = "B"
            else:
                winner[i] = 0

# 요구사항에 맞게 출력
for i in range(T):
    print("#{0} {1}".format(i+1, winner[i]))
