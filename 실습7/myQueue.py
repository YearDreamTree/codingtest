# 연결 리스트 노드를 정의하는 클래스입니다.
class LinkedListElement :
    def __init__(self, val, p, n) :
        self.value = val
        self.myPrev = p
        self.myNext = n

'''
Queue 클래스를 구현하세요.
'''

class Queue:
    # 연결 리스트를 이용하여 다음의 method들을 작성하세요.
    def __init__(self) :
        # 지시사항: 큐 myQueue을 만듭니다.
        

    def push(self, n) :
        # 지시사항: queue에 정수 n을 넣습니다.
        

    def pop(self) :
        # 지시사항: queue에서 가장 앞에 있는 정수를 제거합니다. 
        # 만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        

    def size(self) :
        # 지시사항: queue에 들어 있는 정수의 개수를 return 합니다.
        

    def empty(self) :
        # 지시사항: queue이 비어있다면 1, 아니면 0을 return 합니다.
        

    def front(self) :
        # 지시사항: queue의 가장 앞에 있는 정수를 return 합니다. 
        # 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        

    def back(self) :
        # 지시사항: queue의 가장 뒤에 있는 정수를 return 합니다. 
        # 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        