# 재귀함수의 문제점 및 해결책
'''
재귀함수의 가장 큰 문제점은 효율성이 좋지 못하다는 점인데,
이미 계산되었던 값일지라도 의미없이 다시 계산을 반복하기 때문이다.
아래 팩토리얼을 구하는 두 함수는 100!을 구하는 함수를 천 번 반복할 경우 2.4배 가량의 시간 차이가
발생한다
'''
#for문을 이용해 함수를 구현하는 경우
def facto_for(n):
    if n == 0 or n == 1:
        return 1

    ans = 1
    for i in range(1,n+1):
        ans = ans * i
    return ans

#재귀를 이용해 함수를 구현하는 경우
def facto_recursion(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * facto_recursion(n-1)

#구하는 데 걸리는 시간을 찍어보자. timeit을 임포트해서 시작.
from timeit import *
t1 = Timer("facto_for(100)", "from __main__ import facto_for")
t2 = Timer("facto_recursion(100)", "from __main__ import facto_recursion")
print("facto_for(100) * 1000 times : ",t1.timeit(number = 1000),"seconds")
print("facto_recursion(100)* 1000 times : ",t2.timeit(number=1000),"seconds")

'''
그래서 위와 같은 문제점을 해결하기 위해 동적계획법에서 활용되는 메모이제이션을 사용해야 한다.
DP(동적계획법)는 큰 문제를 해결하기 위해 작은 문제들을 해결해나가야 하는데, 그 작은 문제들의 결과값은
변하지 않아야 한다. 그리고 그 결과값이 변하지 않는 작은 문제들이 자꾸 반복해서 일어나게 된다.

메모이제이션은 자꾸만 반복되지만 그 결과값은 변하지 않는 작은 문제들의 결과값을 저장하는 것을 의미한다.
메모이제이션을 통해 이미 결과값이 기록되는 특정 문제가 반복될 때, 불필요한 계산은 패스하고 기록되어
있는 값만 불러오면 아주 빠르게 해결할 수 있다. 재귀함수 또한 큰 문제를 해결하기 위해 탈출 조건을
만날때까지 작은 문제들을 풀어나가야 하고, 그 과정 중에 반복되는 작은 문제들이 있을 수 있다.

피보나치의 n번째 수를 구하는 함수에 메모이제이션 개념을 도입하면 다음과 같이 코드를 짤 수 있다.
'''

dic = {} # memoization을 위한 딕셔너리를 함수 외부에 선언

def fibonacci(n):
    if n in dic:
        return dic[n]

    if n == 0 :
        dic[0] = 0
        return 0
    elif n == 1:
        dic[1] = 1
        return 1
    else:
        dic[n] = fibonacci(n-1) + fibonacci(n-2)
        return dic[n]

'''
만약, 위 코드가 지저분하다고 느껴지면
다음과 같이 n이 0 일때와 1일 때를 dictionary에 미리 넣어두면 된다.
'''
dic_2 = {0:0, 1:1}

def fibonacci_2(n):
    if n in dic_2:
        return dic[n]

    dic[n] = fibonacci_2(n-1) + fibonacci_2(n-2)
    return dic[n]

'''
이해한것 같다면
팩토리얼 함수를 메모이제이션을 활용해 구현해보자
'''
dict = {1:1}

def factorial(n):
    if n in dict:
        return dict[n]

    dict[n] =  n * factorial(n-1)
    return dict[n]

print(factorial(4)) #24로 잘 출력되는 것을 확인할 수 있다!