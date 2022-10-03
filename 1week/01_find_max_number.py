input = [3, 5, 6, 1, 2, 4]


## 이중 반복문을 통한 방법

# def find_max_num(array):
#     for num in array:
#         for compare_num in array:
#             if num < compare_num:
#                 break
#         else:
#             return num

# result = find_max_num(input)
# print(result)


## 지정변수를 통한 방법

# def find_max_num(array):
#     max_num = array[0]
#     for num in array:
#         if num > max_num:
#             max_num = num

#     return max_num

# result = find_max_num(input)
# print(result)