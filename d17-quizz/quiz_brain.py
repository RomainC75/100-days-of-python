class Quiz_Brain:
    def __init__(self, questions) -> None:
        self.questions_list=questions
        self.question_number=0
        self.points=0

    def next_question(self):    
        ans = input(f'Q. {self.question_number} {self.questions_list[self.question_number].text}. (True/False) ? ')
        
        if(ans==self.questions_list[self.question_number].answer):
            self.points+=1
            print("right answer")
        else:
            print("wrong answer")
        self.print_score()
        self.question_number+=1

    def is_finished(self):
        if self.question_number>=len(self.questions_list):
            return True
        return False

    def print_score(self):
        print(f'Current score = > {self.points}/{self.question_number+1}')