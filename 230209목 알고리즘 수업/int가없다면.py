#int를 쓰지 않고 atoi함수로 정수로 바꾸기
def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x)-ord('0')
    return i

#string을 쓰지 않고 itoa함수로 문자열로 바꾸기