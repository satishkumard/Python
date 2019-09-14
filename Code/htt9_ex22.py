
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: htt9_ex22.py
# [H6-1] (htt9_ex22.py) Do Exercise 22 at the end of HTT9. The code can be seen via the Show Code button.
# Modify this code so it prints each subtotal, the total cost, and average price to exactly two decimal places.
# ----------------------------------------------------------------------------------------------------------------------


def checkout():
    """Function to keep track of number of items, total and average cost per item"""
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: ${:.2f}'.format(total))
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total ${:.2f}'.format(total))
    print('Average price per item: ${:.2f}'.format(average))


checkout()

