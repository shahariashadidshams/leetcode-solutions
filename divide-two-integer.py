def divide(divided: int, divisor: int):
    if divided == -2**31 and divisor == -1:
      return 2**31 - 1 # Handle overflow

    signresult = -1 if (divided > 0) ^ (divisor > 0) else 1
    answer  = 0
    adivided  = abs(divided)
    adivisor  = abs(divisor)

    while adivided >= adivisor:
      a = 1
      while a * 2 * adivisor <= adivided:
        a <<= 1
      adivided -= a * adivisor
      answer += a

    return signresult * answer

print(divide(10, 3))
print(divide(7, -3))
print(divide(-8, 2))
print(divide(-8, -2))
print(divide(-2**31, -1))
print(divide(2**31 - 1, 1))


"""
Divide Two Integers:
Given two integers dividend and divisor, divide two integers without using multiplication, division, and modulo operator.
The integer division should truncate toward zero, meaning it loses its fractional part.
For example:

    8.345 would be truncated to 8

    -2.7335 would be truncated to -2

Return the quotient after dividing dividend by divisor.
"""