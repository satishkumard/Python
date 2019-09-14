
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: student.py
# [H9-1] (student.py) Create a new class Student. Its instances should track the name and each quiz scores taken by the
# student, including the number of quiz scores that are dropped and the resulting average quiz score. Use a list _scores
# of float values as a Student attribute (field), with _scores[I-1] stored as the score of Quiz I.
#
# Here are the Student methods you should define:
#
# A constructor with a single argument, setting the name of a newly-initialized Student.
# Instance method addScore(self,score), which adds another quiz score to the collection within the Student
# Instance method getNumberQuizzes(self) which should return the total number of quiz scores
# Instance method calcQuizStats(self,dropNumber), which should calculate and set the Student attribute (field) _
# average, after calculating the float average (mean) score after dropping the lowest dropNumber quiz scores.
# If dropNumber is greater than or equal to the total number of quiz scores, then calculate the average as 0.0.
# This method should also set the field _dropNumber
# Instance method getAverage(self) which should return the value of _average
# Instance method __str__(self), which should create a string representation of the student, giving the name, quiz
# average _average, number of dropped quizzes _dropNumber, and the list of each quiz score, with dropped scores marked
# with a *. Example (your output should show the same information, though your formatting may differ):
#
# Name: Moxie Berner
#
# Quiz Average: 47.0
# Number of Quizzes: 4
# Dropped Quizzes: 2
#
# Quiz Scores (* => dropped):
# 1 - 64.0
# 2 - 30.0
# 3 - 10.5 *
# 4 - 20.0 *
#
# In the main() method of your class, create two Student instances, add some quiz scores to each, calculate the quiz
# stats, and print out the string equivalent of each resulting instance.  One of your students should have the same
# information as shown above, but you can choose your own information for the second.
# ----------------------------------------------------------------------------------------------------------------------


class Student():
    """Represents a single student, with attribes: name, list of quiz scores,
    # to drop,average score for all quizzes after dropping specified # of lowest cores"""

    def __init__(self, name):
        """Initialize new Student with given name and empty list _scores"""
        self._name = name
        self._scores = []

    def addScore(self, score):
        """Add score to internal attribute (field) _scores """
        self._scores.append(score)

    def getNumberQuizzes(self):
        return len(self._scores)

    def calcQuizStats(self, dropNumber):
        """Set _dropNumber, then set _average to mean (avg) calculated after dropping dropNumber lowest scores"""
        self._dropNumber = dropNumber
        sortedScore = sorted(self._scores)
        self._average = sum(sortedScore[dropNumber:]) / len(sortedScore[dropNumber:])

    def getAverage(self):
        """Return value of _average"""
        return self._average

    def __str__(self):
        """Return string, formatted as shown in handout"""
        name = "\nName: %s\n" % self._name
        average_score = "\nQuiz Average: %.1f\n" % self._average
        quizs_num = "Number of Quizzes: %d\n" % self.getNumberQuizzes()
        dropped_num = "Dropped Quizzes: %d\n" % self._dropNumber

        drops = self.getNumberQuizzes() * [0]
        for dropped in sorted(self._scores)[:self._dropNumber]:
            for index in range(len(self._scores)):
                if self._scores[index] == dropped and drops[index] != 1:
                    drops[index] = 1
                    break
        scores = ''

        for index in range(len(self._scores)):
            if drops[index] == 0:
                scores = scores + '%d - %.1f\n' % (index + 1, self._scores[index])
            else:
                scores = scores + '%d - %.1f *\n' % (index + 1, self._scores[index])

        quiz_scores = '\nQuiz Scores (* => dropped):\n' + scores
        result = name + average_score + quizs_num + dropped_num + quiz_scores

        return result


def main():
    """Create two Students, add quiz scores to each, then calculated quiz stats (choose # of lowest to drop)
    and print the stringified Student. One of your Students should have same output as in handout;
    you can choose your own data for the second"""

    student1 = Student('Eric Level')
    student1.addScore(75)
    student1.addScore(35)
    student1.addScore(80)
    student1.addScore(10)
    student1.calcQuizStats(2)

    student2 = Student('Satish')
    student2.addScore(91)
    student2.addScore(25)
    student2.addScore(45)
    student2.addScore(54)
    student2.calcQuizStats(2)

    print(student1)
    print(student2)


if __name__ == "__main__":
    main()




