
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# File: eval2.py
# [H1-3] (eval2.py) Same as the previous, but for the expression: 1.0 + 2.0 * 5 ** 6 ** 2 % 3 - 4 // 47.
# Note the two new operators ** (exponentiation) and // (integer division).
# Precedence Order - Parenthesis > Exponential > Multiplication/Division/Integer Division/Modulus > Addition/Subtraction
# ----------------------------------------------------------------------------------------------------------------------

e1 = 1.0
e2 = 2.0
e3 = 5
e4 = 6
e5 = 2
e6 = 3
e7 = 4
e8 = 47

# Exponential **
ex1 = e4 ** e5  # Associativity - Start from right exponential

ex2 = e3 ** ex1

# Modulus
mo1 = ex2 % e6

# Multiplication
m1 = e2 * mo1

# Integer Division
d1 = e7 // e8

# Addition
a1 = e1 + m1

# Subtraction
s1 = a1 - d1

print(s1)

print(1.0 + 2.0 * 5 ** 6 ** 2 % 3 - 4 // 47)

