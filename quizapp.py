

questions = (
    "Which planet is known as the Red Planet?",
    "Who wrote Romeo and Juliet?",
    "What is the largest ocean on Earth?",
    "What is the chemical symbol for Gold?",
    "In which year did World War II end?",
)

options = (("A. Venus","B. Mars","C. Jupiter","D. Saturn"),
           ("A. Charles Dickens","B. William Wordsworth","C. William Shakespeare","D. Jane Austen"),
           ("A. Atlantic Ocean","B. Indian Ocean","C. Arctic Ocean","D. Pacific Ocean"),
           ("A. Go","B. Gd","C. Au","D. Ag"),
           ("A. 1942","B. 1945","C. 1948","D. 1950")
           )

answer = ("B","C","D","C","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    question_num += 1
    input("Choose option(A,B,C,D):")
