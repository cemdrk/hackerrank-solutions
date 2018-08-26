
def geo_dist(p, n):
    q = 1-p
    return (q ** (n-1)) * p

if __name__ == '__main__':
    num, denom = list(map(int, input().rstrip().split()))
    n = int(input())

    p = num / denom

    print('%.3f' % geo_dist(p, n))
