
def nCr(n,r):
    import math
    f = math.factorial
    return f(n) // f(r) // f(n-r)


def binom_dist(n, x, p):
    return nCr(n, x) * (p ** x) * (1-p)**(n-x)


if __name__ == '__main__':
    p, n = input().rstrip().split()
    p = float(p)/100
    n = int(n)

    no_more_than = binom_dist(n, 0, p) + binom_dist(n, 1, p) + binom_dist(n, 2, p)

    print('%.3f' % no_more_than)
    print('%.3f' % ((1-no_more_than)+binom_dist(n, 2, p)))
