from decimal import Decimal


class Calculator:
    # 相加
    def add(self, a, b):
        return a + b

    # 相减
    def sub(self, a, b):
        return a - b

    # 相乘
    def multi(self, a, b):
        return a * b

    # 相除
    def divi(self, a, b):
        if type(a) == float or type(b) == float:
            a = Decimal(str(a))
            b = Decimal(str(b))
            result = a / b
            return result
        else:
            return a / b
