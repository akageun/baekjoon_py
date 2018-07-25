######################
#
# - 문제 : 1, 2, 3 더하기
# - URL : https://www.acmicpc.net/problem/9095
# = DP 문제
#
######################


dp = [0 for i in range(11)]

arr_num = []


def init():
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2  # 1-1, 2
    dp[3] = 4  # 1-1-1, 1-2, 2-1, 3
    dp[4] = 7

    for i in range(5, 11):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]


if __name__ == "__main__":
    T = int(input().strip())  # Test Case

    for i in range(T):
        arr_num.append(int(input().strip()))

    init()

    for i in arr_num:
        print(dp[i])
