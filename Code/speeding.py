
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: speeding.py
# [H5-2] (speeding.py) The speeding ticket fine policy in Beldenville is $50 plus $5 for each mph over the limit, plus a
#  penalty of $200 for any speed over 90 mph. Write a program that reads a float speed limit and another float as the
# measured speed, then either prints a message indicating the speed was legal or prints the amount of the fine if the
# speed was illegal.
# ----------------------------------------------------------------------------------------------------------------------


def is_speeding(speedLimit, measuredSpeed):
    """Calculating the fine if the speed is over the limit"""
    if measuredSpeed < speedLimit:
        message = "The measured speed is within the legal speed limit."
    elif measuredSpeed > speedLimit:
        totalFine = 50 + ((measuredSpeed - speedLimit) * 5)
        if measuredSpeed > 90:
            totalFine = totalFine + 200
        message = "The measured speed is illegal and fine is $" + str(totalFine)
    return message


def main():
    speedLimit = float(input("Enter the legal speed limit: "))
    measuredSpeed = float(input("Enter the measured speed: "))
    print(is_speeding(speedLimit, measuredSpeed))


if __name__ == "__main__":
    main()
