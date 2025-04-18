from solve import make_team

def main():
    '''
    테스트를 위한 코드입니다.
    '''

    n = int(input())
    players = []

    for i in range(n) :
        line = [x for x in input().split()]
        name = line[0]
        shoot = int(line[1])
        dribble = int(line[2])
        players.append([name, shoot, dribble])
    
    result = make_team(players)
    
    print(*result[0])
    print(*result[1])

if __name__ == '__main__':
    main()
