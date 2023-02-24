'''
큐의 선입선출 구조

먼저 들어온 원소를 front
가장 나중에 들어온 원소를 rear
이 둘을 관리한다.

큐에서는 삽입, 삭제를 인큐,디큐라고 지칭한다.(기본연산)

큐의 사용을 위해 필요한 주요 연산은 다음과 같다.
- 인큐
- 디큐
- createQueue() 공백 상태의 큐를 생성
- isEmpty() 큐가 공백 상태인지를 확인
- isFull() 큐가 포화상태인지를 확인
- Qpeek() 큐의 front에서 원소를 삭제없이 반환

기본 연산 과정
1. 공백 큐 생성(크기가 정해진 리스트 형태)
2. front 는 디큐위치, rear는 인큐위치인데 시작할 때 -1로 초기화하여 시작
3. 인큐 연산
 -  rear를 증가시키고 원소 a를 저장
 -  rear를 하나더 증가시켜서 원소 b를 저장
4. 디큐 연산
 -  front를 하나 증가시켜서 꺼냄
5. 즉, 인큐든 디큐든 인덱스를 하나 증가시켜서 그 인덱스가 가리키는 자리에서 처리
6. front와 rear가 같은 자리라는 건 빈 큐라는 의미로 이를 이용해 공백 상태인지 알수있음
7. 포화상태는 rear == n -1을 통해 알 수 있음

선형큐? 원형큐?

주요 연산 코드 구현 - 삽입 enQueue(item)
마지막 원소 뒤에 새로운 원소를 삽입하기 위해 rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장
'''
def enQueue(item):
    global rear
    if isFull() : print("Queue_Full")
    else:
        rear <- rear + 1
        Q[rear] <- item

'''
주요 연산 코드 구현 - 삭제 deQueue()
가장 앞에 있는 원소를 삭제하기 위해 front 값을 하나 증가시켜 큐에 남아있게 될 첫번째 원소 이동
새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능함(이거 무슨소리지???)
'''
def deQueue():
    if(isEmpty()) then Queue_Empty();
    else:
        front <- front + 1
        return Q[front]