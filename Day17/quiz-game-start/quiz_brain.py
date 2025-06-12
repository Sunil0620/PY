class QuizBrain:
    
    def __init__(self, q_list):
        """Initializes the QuizBrain with a list of questions."""
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_questions(self):
        """Checks if there are more questions left in the quiz."""
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        """Returns the next question in the quiz."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        
    
    def check_answer(self, user_answer):
        """Checks the user's answer against the correct answer."""
        current_question = self.question_list[self.question_number - 1]
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print("You got it right!")
            return True
        else:
            print("That's wrong. ")
             
        print(f"The correct answer was: {current_question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
