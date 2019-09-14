#
#  dec_2_bin.py, part of Lab 4
#
num = int(input("Enter a decimal integer to convert to binary: "))

while num > 0:
    bit = num % 2
    print (bit,end='')
    num = num // 2

#print ()

def reverse(s): # mystery3.py in Lab 3
    result = ''

    for ch in s:
        result = ch + result

    return result

print (reverse("moxie"))
