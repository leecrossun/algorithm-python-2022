# a^b
import decimal
from decimal import Decimal
decimal.getcontext().prec=10000
a, b = map(Decimal, input().split())
answer = ("{:f}".format(pow(a, b)))
print(answer)