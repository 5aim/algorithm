# facebook 기출문제
# 숫자사이에 연산자 x, + 를 넣어 결과적으로 가장 큰 수를 구하기

input = [0, 3, 5, 6, 1, 2, 4]

def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        # 1보다 작거나 같으면 값을 multiply_num에 더해주고
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        # 그게 아니라면 곱하기식으로 multiply_num을 올려준다.
        else:
            multiply_sum *= number
    return multiply_sum

result = find_max_plus_or_multiply(input)
print(result)