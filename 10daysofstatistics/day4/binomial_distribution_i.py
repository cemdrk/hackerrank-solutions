
def nCr(n,r):
    import math
    f = math.factorial
    return f(n) // f(r) // f(n-r)


def binom_dist(n, x, p):
    return nCr(n, x) * (p ** x) * (1-p)**(n-x)


if __name__ == '__main__':
    ratio, child = input().rstrip().split()
    ratio = float(ratio)

    n = 6
    x = 3
    p = ratio/(1+ratio)

    result = binom_dist(n, x, p) + binom_dist(n, x+1, p) + binom_dist(n, x+2, p) + binom_dist(n, x+3, p)
    
    print('%.3f' % result)
