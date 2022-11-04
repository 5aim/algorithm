finding_target = 15 # 아래 숫자들에서 14가 들어있으면 True 없으면 False를 출력.
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# 우선 최솟값과 최댓값을 변수로 놓아야 함.
def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2 # 소숫점 이하는 나타나지 않으므로 current_guess도 index로 사용가능.
    find_count = 0 # 시간 복잡도 측정
    
    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2

    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)  # True 