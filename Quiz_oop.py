question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class Question:
  def __init__(self,text,answer):
    self.text=text
    self.answer=answer

class QuizBrain:
  def __init__(self,q_list):
    self.question_num=0
    self.question_list=q_list
    self.score=0

  def next_question(self):
    current_ques=self.question_list[self.question_num]
    self.question_num+=1
    choice=input(f"Q.{self.question_num}: {current_ques.text} (True/False): ")
    self.check_answer(choice,current_ques.answer)

  def still_has_ques(self):
    return self.question_num < len(self.question_list)

  def check_answer(self,choice,correct_answer):
    if choice.lower()==correct_answer.lower():
      self.score+=1
      print("You Got it right!!")
      
    else:
      print("You got it Wrong")
      print(f"Correct Answer is : {correct_answer}")
    print(f"Your Current score is: {self.score}/{self.question_num}")
    print("\n")
      
    
    

question_bank=[]

for question in question_data:
  new_q=question["text"]
  new_ans=question["answer"]
  new_question=Question(new_q,new_ans)
  question_bank.append(new_question)


quiz=QuizBrain(question_bank)


while quiz.still_has_ques():
  quiz.next_question()
  


print(f"Total Score: {quiz.score}/{quiz.question_num}")
  

  