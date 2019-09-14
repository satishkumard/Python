
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# File: eval1.py
# [H1-2] (eval1.py) In HTT2 Exercise 2, the parenthesized expression 2 + (3 - 1) * 10 / 5 * (2 + 3) is given.
# This chapter describes the order in which Python evaluates the different sub-expressions within it,
# leading to a single value for evaluating the entire expression.
# Precedence Order - Parenthesis > Exponential > Multiplication/Division/Integer Division/Modulus > Addition/Subtraction
# ----------------------------------------------------------------------------------------------------------------------

e1 = 2
e2 = 3
e3 = 1
e4 = 10
e5 = 5
e6 = 2
e7 = 3

# Parenthesis ()
p2 = e2 - e3

p1 = e6 + e7

# Division /
d1 = e4 / e5

# Multiplication *
m1 = p2 * d1
m2 = m1 * p1

# Addition +
a1 = e1 + m2

print(a1)

print(2 + (3 - 1) * 10 / 5 * (2 + 3))



