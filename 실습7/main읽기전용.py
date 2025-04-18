from myQueue import Queue

def main():
    queue = Queue()

    '''
    테스트를 위한 코드입니다.
    '''
    n = int(input())
    
    for i in range(n) :
        temp = [int(v) for v in input().split()]
        x = int(temp[0])
        if x == 1 :
            queue.push(temp[1])
        elif x == 2 :
            queue.pop()
        elif x == 3 :
            print(queue.size())
        elif x == 4 :
            print(queue.empty())
        elif x == 5 :
            print(queue.front())
        elif x == 6 :
            print(queue.back())


if __name__ == "__main__":
    main()
