class Mind:
    def __init__(self,listA, listQ):
        self.current = 0
        self.score = 0
        self.Answers = listA
        self.Questions = listQ
    
    def next(self):
        quest = self.Questions[self.current]
        a = self.Answers[self.current]
        self.current+=1
        answer = input(f"Q:{self.current} {quest} (True/False) ")
        self.correct(answer, a)

    def correct(self, answer, a):
        if answer.lower() == a.lower():
            self.score+=1
            print(f"You got it right {self.score}/{len(self.Answers)} ")
        else:
            print(f"You got it wrong {self.score}/{len(self.Answers)}")
        self.again()
    
    def again(self):
        if self.current < len(self.Answers):
            return True
        return False

            


