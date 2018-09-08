class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        arr_len = len(a)

        for i in range(arr_len-1):
            for j in range(i+1, arr_len):
                dif = abs(a[i] - a[j])
                if dif > self.maximumDifference:
                    self.maximumDifference = dif

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
