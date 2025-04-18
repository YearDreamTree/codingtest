# 지시사항을 참고하여 코드를 작성하세요.
def hot_cold(emotion):
    # 주어진 지시사항에 맞추어 hot_cold()함수를 구현하세요.
    hot_index = emotion.index("열정")
    cold_index = emotion.index("냉정")

    start = min(hot_index, cold_index)
    end = max(hot_index, cold_index)

    between = emotion[start + 1: end]
    return between.count("사랑")
    

# 값을 확인하기 위한 코드입니다. 값을 변경해가며 테스트해 보세요!
print(hot_cold(['냉정', '사랑', '사랑', '사랑', '열정', '사랑', '사랑']))

냉정 사랑 사랑 사랑 열정
0    1   2   3   4

인덴스 [1:4] 즉 [start +1]부터 [end -1]