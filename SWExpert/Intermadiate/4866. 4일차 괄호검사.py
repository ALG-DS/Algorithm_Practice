'''
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
 
예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다. 

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다. 

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력 예]
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())

[출력 예]
#1 1
#2 1
#3 0
'''
def well_closed(string):
    brackets = {"left" : ['(', '{', '['], "right" : [')', '}', ']']} # 왼쪽 괄호, 오른쪽 괄호를 dictionary형태로 저장
    lst = [] # stack
    for i in string: # 문자열에 있는 모든 문자에 대해
        if i in (brackets['left'] + brackets['right']): # 그 문자가 괄호라면
            lst.append(i) # stack에 추가
            if i in brackets['right']: # 근데 그게 오른쪽 괄호고
                if len(lst) > 1: # stack에 이미 하나 이상의 괄호가 있고
                    if brackets['left'][brackets['right'].index(lst[-1])] == lst[-2]: # 그에 대칭되는 왼쪽 괄호가 바로 직전에 있었다면
                        [lst.pop() for _ in range(2)] # 새로 받은 오른쪽 괄호랑 왼쪽 괄호 함께 제거
    if len(lst) == 0: # 다 돌리고 나서 스택이 비어있다면 성공적
        return 1
    else: # 아니라면 괄호가 안닫힌 문장
        return 0

T = int(input())
for t in range(T):
    string = input()
    print("#{0} {1}".format(t+1, well_closed(string)))