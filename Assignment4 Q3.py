import random

#function to generate a random multiplication question
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2
    return (num1, num2, answer)

# main game loop
num_correct = 0
for i in range(10):
    # generate a new question
    num1, num2, answer = generate_question()
    
    # prompt the user for an answer
    user_answer = int(input("Question {}: What is {} x {}? ".format(i+1, num1, num2)))
    
    # check if the answer is correct
    if user_answer == answer:
        print("Right!")
        num_correct += 1
    else:
        print("Wrong. The answer is", answer)
    
# display the final score
print("You got", num_correct, "out of 10 questions correct.")