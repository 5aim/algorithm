input = 20

# 소수 : 약수가 1과 자기 자신뿐인 자연수를 의미
# 20이 입력된다면 아래와 같이 반환 [2, 3, 5, 7, 11, 13, 17, 19]
# range() 함수를 사용

def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)

# 2, 3, 4, 5, 6, 7, 8, 9, ... 19까지 한 번씩 다 나누면서 나머지가 0인지 확인하는데 2와 3으로 나누어 떨어지지 않는다면, 2 X 3 인 6으로도 당연히 안 나누어 떨어진다. 즉, 2부터 n-1 까지 모든 수 로 나누어 떨어지지 않는지 확인하는 것이 아니라 2부터 n-1 까지 모든 소수 로 나누어 떨어지지 않는지 알아보도록 개선해보자.