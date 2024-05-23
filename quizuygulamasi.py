class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkanswer(self,answer):
        return self.answer == answer

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[quiz.questionIndex]

    def display(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1} : {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("Cevap : ")
        print(question.checkanswer(answer))
        self.guess(answer)
        self.load()
    
    def guess(self,answer):
        question = self.getQuestion()

        if(question.checkanswer(answer)):
            self.score += 1
        self.questionIndex += 1

    def load(self):
        if(len(self.questions)) == self.questionIndex:
            self.showScore()
        else:
            self.displaypro()
            self.display()

    def showScore(self):
        print("Score : ",self.score)

    def displaypro(self):
        totalquestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if (questionNumber > totalquestion):
            print("Quiz bitti")
        else:
            print(f"Question {questionNumber} of {totalquestion}".center(100,'*'))

q1 = Question("En iyi programlama dili hangisidir ?",["C#","Python","C","JavaScript"],"Python")
q2 = Question("En çok kazandiran programlama dili hangisidir ?",["C#","JavaScript","C","Python"],"Python")
q3 = Question("En kolay programlama dili hangisidir ?",["Python","C#","C","JavaScript"],"Python")
questions = [q1,q2,q3]

quiz = Quiz(questions)
question = quiz.getQuestion()

quiz.load()