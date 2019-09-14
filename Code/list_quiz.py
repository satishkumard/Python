
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: list_quiz.py
# [H7-5] (list_quiz.py) Write a program that administers a short one-question quiz on lists to the user, then grades it
# and presents the results.  Your question should test on these topics discussed in HTT10 ("Lists").
# Your quiz should be interactive; it should print a question, read the user's answer and print if it's correct or not.
# If it's not correct, give the correct answer.  In both cases, print out a brief description of why the correct answer
# is correct.
# You might present multiple-choice questions, or else a question that asks the user to enter the output printed by some
# given Python code. In either case, your program should be able to read the user's response and determine if it's
# correct or not.
# An example of the latter is:
# Enter the output of the following code:
# 		s = 'moxie, sasha, sandy'
# 		slist = s.split()
# 		result = [elt[:-1] for elt in slist]
# 		print (result)
# If the user enters: ['moxie','sasha','sand'] then output might be: Correct!
# If the user enters: ['moxie','sasha','sandy'] then output might be: Sorry, that is incorrect.
# In both cases, the explanation of the correct answer should be printed, like this:
# s.split() returns a list of strings delimited by whitespace in the original - not by commas.
# Thus, slist = ['moxie,','sasha,','sandy']. Then the list comprehension builds a new list result that trims the last
# character from each of slist's elements.  So the final value of result is:
# ['moxie','sasha','sand']
# ----------------------------------------------------------------------------------------------------------------------

# Give short one-question quiz on HTT10 (Lists) to user


def main():
    """Function asking a question to the user and evaluate the user answer."""
    print("What does the below code print for result for a given mylist ")
    print("result = []")
    print("for i in myList:")
    print("    if i not in result:")
    print("        result.append(i)")
    print("print(result)")
    answer = [1, 2, [1, 2], [3, 4]]
    userInput = eval(input("The value entered for myList is [1,2,[1,2],[3,4],1,[1,2],2]. "
                           "Enter your answer: "))
    if len(userInput) == len(answer) and all(input in answer for input in userInput):
        print("Congrats! you entered the right answer.")
        print("The for loop check each item in myList and copies into an new result list.")
        print("Any duplicates in myList will be ignored while copying into new result list.")
    else:
        print("Sorry, you entered the wrong answer.")
        print("The answer is [1, 2, [1, 2], [3, 4]]")
        print("The for loop check each item in myList and copies into an new result list."
              "Any duplicates in myList will be ignored while copying into result list.")


if __name__ == "__main__":
    main()

