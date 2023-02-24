def enq(data):
    global rear
    rear +=1
    queue[rear] = data
    # 호출할 때 포화상태 안전장치필요

def deq():
    global front
    front +=1
    return queue[front]
    #호출할 때 공백상태 안전장치필요

queue = [0]*10
front = -1
rear = -1

enq(1)
enq(2)
enq(3)

print(deq())
print(deq())
print(deq())
print(deq())
print(deq())
print(deq())

if front != rear:
    print(deq())
if front != rear:
    print(deq())
if front != rear:
    print(deq())
if front != rear:
    print(deq())
if front != rear:
    print(deq())
if front != rear:
    print(deq())


'''
교수님"
append(item)과 pop(0)을 사용하여 구현할 수도 있으나
규모가 큰 작업을 할 경우 속도가 매우 느려질 수 있어
함수를 만들거나 위와 같은 로직을 이용해 구현하는 걸 추천
'''