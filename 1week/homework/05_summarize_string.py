# 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.
# 중간에 없는 알파벳이 있을 수도 있음


def summarize_string(target_string):

    n = len(target_string)
    count = 0
    result_str = ''

    for i in range(n - 1):
        if target_string[i] == target_string[i + 1]:
            count += 1
        else:
            result_str += target_string[i] + str(count + 1) + '/'
            count = 0

    result_str += target_string[n - 1] + str(count + 1)

    return result_str


input_str = "acccdeee"

print(summarize_string(input_str))