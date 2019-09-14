
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: inventory.py
# [H8-5] (inventory.py) Using a dictionary with string keys and integer values, implement a simple database for tracking
# the inventory of items. That is, for a dictionary dict, dict['apples'] == 47 represents 47 apples in the inventory.
# ----------------------------------------------------------------------------------------------------------------------


def getCommand():
    print("\nAdd:- A")
    print("View:- V")
    print("Quit:- Q")
    command = input("Enter command: ")
    return command


def addToInventory(dict):
    keyValueList = []
    key = input("\nEnter item name: ")
    value = int(input("Enter no. of items: "))
    keyValueList = [key, value]
    dict[keyValueList[0]] = dict.get(keyValueList[0], 0) + keyValueList[1]
    return dict


def viewInventory(dict):
    print("\nHere are the items in the inventory: ")
    for k, v in dict.items():
        print("%s -- %s" % (k, str(v)))


def main():
    print("Welcome to StuffMaster, v.0.47")

    inventory = {'Item': 'Qty'}  # empty dictionary

    while True:  # get command, process command; quit when selected below
        # Get the command,
        userInput = getCommand()
        # Call the appropriate function based on command
        if userInput.upper() == 'A':
            inventory = addToInventory(inventory)
        elif userInput.upper() == 'V':
            viewInventory(inventory)
        elif userInput.upper() == 'Q':  # If unknown command, complain and prompt for reentry
            print("\nQuitting. Final version of inventory is:")
            viewInventory(inventory)
            break
        else:
            print("\nNot a valid command, Retry")  # here, we're quitting


if __name__ == "__main__":
    main()



