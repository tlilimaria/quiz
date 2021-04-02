ass Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What does 'sein' mean?\n(a) 'to be'\n(b)'to have'", '\n'
                                                         "What does 'haben' mean?\n(a) 'to be'\n(b)'to have'", '\n'
                                                                                                               "What does 'werden' mean?\n (a) 'to become'\n (b) 'to come'",
    '\n'
    "What does 'sagen' mean?\n (a) 'to say'\n (b) 'to hear'", '\n'
                                                              "What does 'geben' mean?\n (a) 'to take'\n (b) 'to give'",
    '\n'
]
name = input("Please enter your name: ").title()
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b")
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("\n{0}, you scored {1} out of {2}.".format(name, score, len(questions)))


run_quiz(questions)