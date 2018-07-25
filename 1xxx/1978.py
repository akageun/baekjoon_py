######################
#
# - 문제 : 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# - URL : https://www.acmicpc.net/problem/1978
#
######################
import sys


def is_prime(num):
    if num is 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


if __name__ == "__main__":
    input_num = int(input().strip())

    arr = list(map(int, input().strip().split(" ")))

    if input_num != len(arr):
        sys.exit(0)

    result_cnt = 0  # 소수의 갯수

    for num in arr:
        if is_prime(num):
            result_cnt += 1

    print(result_cnt)
