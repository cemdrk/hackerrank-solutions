class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        import math
        divisors = []
        for i in range(1, int(math.sqrt(n) + 1)):
            if n % i == 0:
                divisors.append(i)
                if i*i != n:
                    divisors.append(n // i)

        return sum(divisors)

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
