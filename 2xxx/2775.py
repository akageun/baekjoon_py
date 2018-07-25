######################
#
# - 문제 : 반상회를 주최하려고 한다.
# - URL : https://www.acmicpc.net/problem/2775
#
######################


apart = [[0] * 14 for i in range(15)]  # 14*14 배열 생성


def find_people(k, n):
    if n == 1:  # 아래(a-1)층에 1호부터 b 호까지 사람들의 수의 합, ex) 1층 (1-1=0)층 1호 = 1명, 2층 (2-1=1)층 1호 = 1명...
        return 1

    if apart[k][n - 1] == 0:
        apart[k][n - 1] = find_people(k - 1, n) + find_people(k, n - 1)

    return apart[k][n - 1]


if __name__ == "__main__":

    for i in range(14):
        apart[0][i] = i + 1

    T = int(input().strip())  # Test Case

    for i in range(T):
        k = int(input().strip())  # 1<= k <= 14
        n = int(input().strip())  # 1 <= n <= 14

        print(find_people(k, n))  # a층 b 호, b-1 번째 배열
