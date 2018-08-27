

if __name__ == '__main__':
    mean_a, mean_b = list(map(float, input().rstrip().split()))


    cost_a = 160 + 40 * (mean_a + mean_a ** 2)
    cost_b = 128 + 40 * (mean_b + mean_b ** 2)

    print('%.3f' % cost_a)
    print('%.3f' % cost_b)
