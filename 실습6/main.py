# 단어와 빈도수의 쌍으로 이루어진 튜플을 받아, 빈도수를 리턴합니다.
def get_freq(pair):
    return pair[1]

def filter_by_text(text) :
    # 주어진 규칙에 맞추어 filter_by_text()함수를 구현해주세요.
    # corpus.txt에 있는 텍스트를 읽어와서 corpus라는 리스트에 추가해봅시다.
    corpus = []
    with open("corpus.txt") as file:
        # line에는 corpus.txt 파일의 문장이 한줄씩 불러와집니다.
        for line in file:
            # 지시사항: '/'기준으로 문장을 쪼갠 후, strip 함수를 이용해 공백을 제거하세요.
            
            
            # 지시사항: corpus라는 리스트에 (단어, 빈도수) 튜플을 추가하세요. 이때 빈도수는 정수형(int)로 변환하세요.
            
            
    
    # 지시사항: corpus에 있는 데이터 중, text로 시작하는 단어만을 추려서 result라는 리스트에 저장하세요.
    
    
    
    # 지시사항: 찾은 영어 단어를 빈도수를 기준으로 내림차순으로 정렬하여 20개만 "출력"하세요. 
    # 기준 값은 get_freq 함수로, reverse 인자는 내림차순(True)으로 설정하세요.
    
    
    
    
# 아래는 테스트를 위한 코드입니다. 수정하지 마세요!
# 입력과 출력을 수행하는 코드입니다.
t = input()
filter_by_text(t)