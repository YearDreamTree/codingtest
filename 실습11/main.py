elicehotel_8 = "EliceHotel_8.txt"
elicehotel_9 = "EliceHotel_9.txt"

# EliceHotel_8.txt과EliceHotel_9.txt를 딕셔너리로 저장하기 위해 활용할 txtToDict함수를 정의합니다.
def txtToDict(filename): 
    userDict = {}
    with open(filename) as file:
        for line in file:
            # line에는 corpus.txt 파일의 문장이 한줄씩 불러와집니다.
            # 지시사항: 적절한 함수를 이용하여 Line을 ":" 기준으로 쪼개고, 앞뒤 공백을 제거하세요.
            
            # 지시사항: 날짜를 키로, 방문객을 값으로 딕셔너리 userDict에 저장하는 코드를 작성하세요.
            

        return userDict 

# 2개의 txt 파일명을 입력받아 두 월 모두 방문한 손님을 탐색하는 함수 commonGuest를 정의합니다.
def commonGuest(filename1, filename2):
    # txtToDict 함수를 활용하여 txt파일을 딕셔너리로 저장합니다.
    eliceHotel8 = txtToDict(filename1)
    eliceHotel9 = txtToDict(filename2)

    # 지시사항: 딕셔너리 eliceHotel8, eliceHotel9에 공통으로 포함된 값(방문객)을 집합(set)형태로 반환하세요.


    

print(commonGuest(elicehotel_8, elicehotel_9))