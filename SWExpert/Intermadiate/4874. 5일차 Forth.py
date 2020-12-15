
'''
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다. 
3 4 + .
Forth에서는 동작은 다음과 같다.
숫자는 스택에 넣는다.
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.
Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.

출력
4 2 / .
2

4 3 - .
1

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
나눗셈의 경우 항상 나누어 떨어진다.

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

[입력 예]
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .

[출력 예]
#1 84
#2 error
#3 168
'''
T = int(input())
# 사칙연산
operators = {"+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: a // b} # 몫으로 받아와야 pass!!!

for t in range(T):
    stack = []
    operating = input().split()
    # 받아온 문자 요소들에 대해
    for i in operating:
        # 사칙연산에 속하고
        if i in operators.keys():
            # 이미 두개 이상의 피연산자가 스택에 존재한다면 연산 실행
            if len(stack) >= 2:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(operators[i](a, b))
            # 없다면 error
            else:
                result = 'error'
                break
        # . 을 만났고
        elif i == '.':
            # stack에 1개를 초과하는 숫자가 있을 시 error
            if len(stack) > 1:
                result = 'error'
            # 아니라면 result에 남은 숫자 반환
            else:
                result = stack.pop()
        # 나머지는 모두 stack에 저장(수에 대해서만 해야하지만 편의상 이렇게 해도 무방, 필요시 .isdigit() 사용 가능)
        else:
            stack.append(i)
    print('#{0} {1}'.format(t+1, result))

# divided by 0 은 문제가 안됨
# 숫자만으로 스택이 구성되는 것이 문제가 되는 것도 아님
# stack에 바로 .이 들어오는 것이 문제도 아님