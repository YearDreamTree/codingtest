# 연결 리스트 노드를 정의하는 클래스입니다.
class LinkedListElement :
    def __init__(self, val, p, n) :
        self.value = val
        self.myPrev = p
        self.myNext = n

'''
Deque 클래스를 구현하세요.
'''

class Deque:
    # 아래의 method들을 작성하세요.
    def __init__(self) :
        # 지시사항: 문제의 조건대로 값들을 담을 수 있게끔 Deque 클래스의 생성자를 정의하세요.
        

    def push_front(self, n) :
        # 지시사항: 덱에 정수 n을 맨 앞에 넣습니다.
        

    def push_back(self, n) :
        # 지시사항: 덱에 정수 n을 맨 뒤에 넣습니다.
        

    def pop_front(self) :
        # 지시사항: 덱에서 가장 앞에 있는 정수를 제거합니다. 만약 덱에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        

    def pop_back(self) :
        # 지시사항: 덱에서 가장 뒤에 있는 정수를 제거합니다. 만약 덱에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다.
        

    def size(self) :
        # 지시사항: 덱에 들어 있는 정수의 개수를 return 합니다.
        

    def empty(self) :
        # 지시사항: 덱이 비어있다면 1, 아니면 0을 return 합니다.
        

    def front(self) :
        # 지시사항: 덱의 가장 앞에 있는 정수를 return 합니다. 만약 덱에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        

    def back(self) :
        # 지시사항: 덱의 가장 뒤에 있는 정수를 return 합니다. 만약 덱에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        