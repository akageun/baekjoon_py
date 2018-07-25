######################
#
# - 문제 : 구구단
# - URL : https://www.acmicpc.net/problem/2739
#
######################


if __name__ == "__main__":
    N = int(input().strip())

    start_num = 1
    end_num = 10

    for i in range(start_num, end_num):
        print("{0} * {1} = {2}".format(N, i, (N * i)))
