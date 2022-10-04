# 반복되는 알파벳을 찾아서 그 중 첫번째 알파벳을 반환해라.
# 03_find_max_occurred_alphabet 참고
# method : isalpha(), ord(), chr()

input = "adcadcadcadc"

def find_not_repeating_first_character(string):
    # alphabet array indexing.
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1


    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        
        # 왜 1이냐면 반복되지 않기 때문에 index에 1로 저장될 것이기 때문
        # index에 아스키코드값을 추가해서 몇번째 알파벳인지 찾아야서 append함.
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    # 안에 값이 있으면 바로 반환하도록 해서 첫번째 알파벳을 출력하자
    for char in string:
        if char in not_repeating_character_array:
            return char

    return "_"

result = find_not_repeating_first_character(input)
print(result)