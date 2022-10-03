# # 최대 알파벳 찾기


input = "hello my name is sparta"

# # 각 알파벳마다 문자열을 돌면서 몇 글자 나왔는지 확인해서 그 숫자가 저장한 알파벳 빈도수보다 크면 그 값을 저장하고 제일 큰 알파벳으로 저장하는 방법.

# def find_max_occurred_alphabet(string):
#     alphabet_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
#     max_occurrence = 0
#     max_alphabet = alphabet_array[0]

#     for alphabet in alphabet_array:
#         occurrence = 0
#         for char in string:
#             if char == alphabet:
#                 occurrence += 1

#         if occurrence > max_occurrence:
#             max_occurrence = occurrence
#             max_alphabet = alphabet

#     return max_alphabet


# result = find_max_occurred_alphabet(input)
# print(result)


# 각 알파벳 빈도수를 변수에 저장한다음 각 문자열을 돌면서 해당 문자가 알파벳인지 파악하고 알파벳을 인덱스 화 시켜서 알파벳의 빈도수를 업데이트하는 방법.

def find_max_occurred_alphabet(string):
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

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        # index 0 -> alphabet_occurrence 3
        alphabet_occurrence = alphabet_occurrence_array[index]
        
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index
        
    # print(max_alphabet_index)

    # a -> 0
    # a -> ord(a) -> 97 - ord(a) = 0

    # 0 -> a
    # 0 -> 0 + ord(a) -> 97 -> chr(97) -> a

    return chr(max_alphabet_index + ord("a"))

result = find_max_occurred_alphabet(input)
print(result)