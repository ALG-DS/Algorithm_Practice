'''
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.
반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
CAA 연속 문자 AA를 지운다.
C 1글자가 남았으므로 1을 리턴한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

[입력 예]
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX

[출력 예]
#1 1
#2 4
#3 11
'''
def LetsPopSameLetters(string): # 같은 문자를 pop시켜 제거시킬 함수
    n = len(string) # string의 길이 n
    lst_str = [] # stack
    for i in range(n): # n회 반복
        m = len(lst_str) # 스택의 길이를 그때 그때 업데이트
        lst_str.append(string[i]) # 스택에 string의 요소를 하나씩 들여보냄
        if m >= 1: # stack이 하나 이상일때 비교
            if lst_str[m] == lst_str[m-1]: # 지금 받아온 요소와 그 직전의 요소가 같다면
                [lst_str.pop() for _ in range(2)] # 둘이 팝시켜서 없애버림
    return len(lst_str) # 최종적으로 스택에 남은 문자를 return

T = int(input()) # T 입력
for t in range(T): # t회 반복
    string = input() # string 입력
    print("#{0} {1}".format(t+1, LetsPopSameLetters(string))) # 요구에 맞게 출력