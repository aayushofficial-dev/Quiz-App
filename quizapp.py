print("Welcome to Kaun Banega Crorepati!")
questions = [
    ["What is the capital city of Nepal?", "Kathmandu", "Pokhara", "Biratnagar", "Itahari", 1],
    ["What is the capital city of India?", "UP", "Mumbai", "Delhi", "Chennai", 3],
    ["What is the capital city of China?", "Shanghai", "Beijing", "Hong Kong", "Guangzhou", 2],
    ["What is the capital city of USA?", "Chicago", "New York", "Los Angeles", "Washington DC", 4],
    ["Which planet is known as the “Red Planet”?", "Venus", "Mars", "Jupiter", "Saturn", 2],
    ["Which is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Great White Shark", 2],
    ["Who wrote the play 'Romeo and Juliet'?", "Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen", 3],
    ["What is the chemical symbol for gold?", "Au", "Ag", "Fe", "Pb", 1],
    ["Which country is known as the Land of the Rising Sun?", "China", "South Korea", "Japan", "Thailand", 3],
    ["Which is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4]
]
print("You will be asked a series of questions. Answer them correctly to win money!")
levels = [1000, 2000, 3000, 40000, 50000, 100000, 200000, 500000, 1000000, 2000000]

for i in range (0, len(questions)):
    print(f"Question {i+1}: {questions[i][0]}")
    print(f"1. {questions[i][1]}")
    print(f"2. {questions[i][2]}")
    print(f"3. {questions[i][3]}")
    print(f"4. {questions[i][4]}")
    
    answer = int(input("Please enter your answer (1/2/3/4) or press 0 to quit the game: "))
    
    if answer == 0:
        print("You have chosen to quit the game.")
        break
    if answer == questions[i][5]:
        print(f"Correct! You have won {levels[i]} rupees.")
    else:
        print(f"Wrong answer! The correct answer was {questions[i][questions[i][5]]}.")
        print("The total amount you have won is: ", levels[i-1] if i > 0 else 0)
        break
    if i == len(questions) - 1:
        print("Congratulations! You have answered all questions correctly and won the maximum prize of 2,000,000 rupees!")