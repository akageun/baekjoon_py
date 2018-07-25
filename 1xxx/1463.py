######################
#
# - 문제 : 1로 만들기
# - URL : https://www.acmicpc.net/problem/1463
#
# - 동적 계획법 : DP는 특정 범위까지의 값을 구하기 위해서 그것과 다른 범위까지의 값을 이용하여 효율적으로 값
# - https://www.youtube.com/watch?v=K15qLnKKrow&t=717s
#
######################

import math
import sys

if __name__ == "__main__":
    X = int(input().strip())

    num_arr = [0 for i in range(X + 1)]

    if 1 > X or X > math.pow(10, 6):  # 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.
        sys.exit(0)

    for i in range(2, X + 1):
        num_arr[i] = num_arr[i - 1] + 1  # +1을 하는 이유는 3번 1을 뺀다.

        if i % 3 == 0:
            num_arr[i] = min(num_arr[i], num_arr[int(i / 3)] + 1)

        if i % 2 == 0:
            num_arr[i] = min(num_arr[i], num_arr[int(i / 2)] + 1)

        print(num_arr[i], i)

    print(num_arr[X])
