# 아스키(ASCII)코드 & str.isalpha() & ord()

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        # python ord() 함수 이용하기
        # "a" -> 0
        # "b" -> 1
        # "c" -> 2
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

print(find_alphabet_occurrence_array("hello my name is sparta"))