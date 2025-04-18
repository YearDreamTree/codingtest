from myDeque import Deque

def main():
    deque = Deque()

    '''
    테스트를 위한 코드입니다.
    '''
    n = int(input())
    
    for i in range(n) :
        temp = [int(v) for v in input().split()]
        x = int(temp[0])
        if x == 1 :
            deque.push_front(temp[1])
        elif x == 2 :
            deque.push_back(temp[1])
        elif x == 3 :
            deque.pop_front()
        elif x == 4 :
            deque.pop_back()
        elif x == 5 :
            print(deque.size())
        elif x == 6 :
            print(deque.empty())
        elif x == 7 :
            print(deque.front())
        elif x == 8 :
            print(deque.back())


if __name__ == "__main__":
    main()
