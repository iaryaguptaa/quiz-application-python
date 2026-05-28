def run_quiz():
    questions =[
        {
            "question" : "What is the capital of France?",
        "options" : ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer" : "A) Paris"
        },
        {
            "question" : "What is 2 + 2?",
            "options" : ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer" : "B) 4"
        },
        {
            "question" : "What is the largest planet in our solar system?",
            "options" : ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer" : "C) Jupiter"
        },
        {
            "question" : "Who wrote Hamlet?",
            "options" : ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
            "answer" : "B) William Shakespeare"
        }
    ]
    
    score = 0
    '''
    enumerate function ids used to get both the index and the value of the list item. Example:
    for index, value in enumerate(['a', 'b', 'c']):
        print(index, value)
    The output will be:
    0 a
    '''

    for index,q in enumerate(questions):
        # print(index, q)
        print(f"Question {index + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("Your answer(A/B/C/D): ")
        # print(user_answer.strip().upper(),q['answer'][0])
        if user_answer.strip().upper() == q['answer'][0]: 
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong!\n")

    print(f"Your final score is: {score}/{len(questions)}")
                

run_quiz()