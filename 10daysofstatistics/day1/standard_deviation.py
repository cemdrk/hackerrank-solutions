
def standard_dev(n, arr):
    from math import sqrt

    mean = sum(arr) / n
    distance = 0

    for num in arr:
        distance += (num - mean) ** 2

    st_dev = sqrt(distance / n)

    return st_dev

if __name__ == '__main__':
    n = int(input())

    X = list(map(int, input().rstrip().split()))

    print('%.1f' % standard_dev(n, X))
