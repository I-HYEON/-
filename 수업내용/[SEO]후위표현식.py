# 우선순위 정보를 저장할 딕셔너리
# 중위표현식과 후위표현식을 저장할 리스트 두개
# 연산자를 저장할 스택을 준비한다.
우선순위 = {'*':3, '/':3, '+':2,'-':2,'(':1}

중위표현식 = []
후위표현식 = []
스택 = []

tc = input()  # 인풋을 문자열로 받아온다
for i in tc:
    if i == ' ':
        continue
    중위표현식.append(i)
    
for i in 중위표현식:
    if i == '(':
        스택.append(i)

    elif i in '+-*/':
        if not 스택:
            스택.append(i)
        else:
            if 우선순위[스택[-1]] >= 우선순위[i]:
                후위표현식.append(스택.pop())
                스택.append(i)
            else:
                스택.append(i)

    elif i == ')':
        while True:
            temp = 스택.pop()
            if temp == '(':
                break
            후위표현식.append(temp)

    else:
        후위표현식.append(i)

while 스택:
    후위표현식.append(스택.pop())

print(''.join(후위표현식))