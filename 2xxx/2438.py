######################
#
# - 문제 : 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# - URL : https://www.acmicpc.net/problem/2438
#
######################


if __name__ == "__main__":
    N = int(input().strip())

    for i in range(1, N + 1):
        tmp_str = ""

        for j in range(i):
            tmp_str += "*"

        print(tmp_str)
