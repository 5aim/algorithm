# 입력숫자가 리스트 안에 존재하는지 찾는 문제를 통한 시간복잡도 이해하기
# 알고리즘은 입력값의 분포에 따라서 성능이 변화할 수 있다.

input = [3, 5, 6, 1, 2, 4]

def is_number_exist(number, array):
    for element in array:  # array의 길이만큼 아래 연산이 실행
        if number == element:  # 비교 연산 1번 실행
            return True  # N * 1 = N 만큼

result = is_number_exist(3, input)
print(result)