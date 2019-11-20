class Calculator:
    @staticmethod
    def power(_n, _p):
        if _n < 0 or _p < 0:
            raise ValueError("n and p should be non-negative")
        else:
            return _n ** _p


if __name__ == '__main__':
    myCalculator = Calculator()
    T = int(input())
    for i in range(T):
        n, p = map(int, input().split())
        try:
            ans = myCalculator.power(n, p)
            print(ans)
        except Exception as e:
            print(e)
