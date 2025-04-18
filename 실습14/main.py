import csv
import json

def get_popular_speaking(n) :
    talks = []
    # 지시사항: ted.csv 파일을 열고 데이터를 읽어와 reader 변수에 저장하세요.
    # 처리된 파일의 각 줄을 불러와 강연 제목과 조회수를 튜플 형태로 talks 리스트에 추가하세요.
    
    
    # 지시사항: talks 리스트에서 조회 수가 n 이상인 강연만 필터링한 후, 이를 조회 수 기준으로 내림차순 정렬하여 반환하세요.
    
    

def main():
    n = int(input())
    print(get_popular_speaking(n))

if __name__ == "__main__":
    main()