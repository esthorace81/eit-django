a = 0.1
b = 0.2

c = a + b
print(c)

from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
c = a + b
print(c)

from fractions import Fraction

a = Fraction(1, 10)  # 1/10 represents 0.1
b = Fraction(1, 5)  # 1/5 represents 0.2
c = a + b
print(c, float(c))
