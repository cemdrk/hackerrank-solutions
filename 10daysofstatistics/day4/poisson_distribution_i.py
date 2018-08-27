import math

def poisson_dist(mean, x):
    return ((mean ** x) * math.exp(-mean)) / math.factorial(x)


if __name__ == '__main__':
    mean = float(input())
    x = int(input())

    print('%.3f' % poisson_dist(mean, x))
