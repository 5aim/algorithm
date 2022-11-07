# 문자열 슬라이싱 [0:0] 을 사용해서 재귀함수 다시 풀어보기

input = "abcba"

def is_palindrome(string):
    # 소주만병만주소
    # 주만병만주
    # 만병만
    # 병
    if len(string) <= 1:
        return True

    # 탈출조건
    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

print(is_palindrome(input))