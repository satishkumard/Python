
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: trace_me.py
# H3-5: run the following in the PyCharm debugger and print
#       the following requested info...
# ----------------------------------------------------------------------------------------------------------------------
num = int(input("enter number of floats: "))

a = 0.0
b = 0.0
c = 0.0

for d in range(num):
    e = float(input("enter next float: "))
    a = max(a, e)
    b = min(b, e)
    c = c + e
    print("set breakpoint here...")
    # LOCATION 1:
    # list values of a, b, c, d, e at this point, each time through loop

print(a)
print(b)
print(c / num)

print("set another breakpoint here...")
# list final values of a, b, c, d, e

# Answers:
# Iteration 1: a = 1.0, b = 0.0, c = 1.0, d = 0, e = 1.0
# Iteration 2: a = 1.0, b = -2.0, c = -1.0, d = 1, e = -2.0
# Iteration 3: a = 3.0, b = -2.0, c = 2.0, d = 2, e = 3.0
# Iteration 4: a = 3.0, b = -4.0, c = -2.0, d = 3, e = -4.0
# Iteration 5: a = 5.0, b = -4.0, c = 3.0, d = 4, e = 5.0
# Final Values: a = 5.0, b = -4.0, c = 3.0, d = 4, e = 5.0

