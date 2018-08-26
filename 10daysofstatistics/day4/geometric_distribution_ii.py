
def geo_dist(p, n):
    q = 1-p
    return (q ** (n-1)) * p

if __name__ == '__main__':
    num, denom = list(map(int, input().rstrip().split()))
    n = int(input())

    p = num / denom
    result = 0

    for i in range(1, n + 1):
        result += geo_dist(p, i)

    print('%.3f' % result)
