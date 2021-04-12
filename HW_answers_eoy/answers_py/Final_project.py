#Final_project

"""
Knowledge competition:
    - Write a knowledge competition program.
    - It should consist of 10 questions in total.
    - Each question will have only one answer.
    - Adjust the answers of the questions according to case sensitivity.
    - Each question should be worth 10 points.
    - If User answers 5 or fewer questions, it will be considered unsuccessful.
    - If the user answers more than 5 questions correctly, it will be considered successful.
"""


# Questions for the fundamental of economics (econ291 or econ294):

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "1 - Which of the following is the basic characteristic of Oligopoly? \n(a) 'a few sellers, one buyer '\n(b)'a few sellers, many buyers'",'\n'
    "2 - Which of the following is used to denote broad money??\n(a) 'M1'\n(b)'M3'",'\n'
    "3 - The best indicator of economic development of any country is ?\n (a) 'Its gross production'\n (b) 'Its per capita income'", '\n'
    "4 - The increase in oil seeds production was due to ?\n (a) 'Yellow revolution'\n (b) 'Green revolution'", '\n'
    "5 - With which aspect of commerce are ‘Bulls and Bears’ associated?\n (a) 'Stock Exchange market'\n (b) 'Foreign Trade'", '\n'
    "6 - National income is the\n (a) 'Net National Product at Market price'\n (b) 'Net domestic product at market price'", '\n'
    "7 - When was the International Monetary Fund (IMF) established?\n (a) '1944'\n (b) '1950'", '\n'
    "8 - Decision taken at Bretton Woods Conference led to the formation of\n (a) 'IMF'\n (b) 'ADB'", '\n'
    "9 - Which of the following best defines a floating-rate bond?\n (a) 'A bond with a fixed interest rate and has lower yield than varying interest rate bond'\n (b) 'A bond with a varying interest rate and has lower yield than fixed interest rate bond'", '\n'
    "10 - Inflation Indexed of Consumers is pegged to ___?\n (a) 'WPI'\n (b) 'CPI'", '\n'
                  ]
name = input("Please enter your name: ").title()
questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b")
              ]
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == "a" or "b":
            if answer == question.answer:
                score += 10
                print("\n{}, Your scored {} in total {} questions.".format(name, score, len(questions)))
                print("Great job!" if score > 50  else "You failed :( ")
        else:
            print("Please select (a) or (b).")
            
run_quiz(questions)
