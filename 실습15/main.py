# 엘리스 토끼의 기록입니다.
eliceCommandLog = ["@2457","!4679476","@24562457","!3657","@5897","!2547","#679647"]

# 모자 장수의 기록입니다.
hatSellerCommandLog = ["@356883","@35673","@247987","@35683469","!4697","!972563","!32670"]

# 주어진 지시사항에 맞추어 checkLog() 함수를 구현하세요.
def checkLog(log1, log2):
    for i in range(len(log1)):
        #eliceCommandLog에 회피기술 사용 기록이 있는지 확인하는 조건문입니다.
        if log1[i].startswith('#'):
            return f"엘리스 토끼, {i+1}"
        
        #hatSellerCommandLog에 회피기술 사용 기록이 있는지 확인하는 조건문입니다.
        elif log2[i].startswith('#'):
            return f"모자 장수, {i+1}"



# 올바른 작동을 확인하기 위한 코드입니다.
print(checkLog(eliceCommandLog,hatSellerCommandLog))