

def weighted_mean(n, x, w):
    product = 0
    for i in range(n):
        product += x[i] * w[i]
    
    return product / sum(w)

if __name__ == '__main__':
    N = int(input())
    X = list(map(int, input().rstrip().split()))
    W = list(map(int, input().rstrip().split()))

    print('%.1f' % weighted_mean(N, X, W))
