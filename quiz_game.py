print("Welcome! Quiz Game Players!")

playing = input("Do you want to play? ")
print(playing)


if playing.lower() != "yes":
    quit()

print("Okay! Let's play : )")
score = 0

answer = input("Who is the creator of the Python programming language? ")
if answer.lower() == "guido van rossum":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Python code is significantly larger than its equivalent C++/Java code? ")
if answer.lower() == "smaller":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Python runs in the compiler, without any need to be compiled before running it? ")
if answer.lower() == "interpreter":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Python provides static data types and supports dynamic type checking? ")
if answer.lower() == "dynamic":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Used to display something in the console? ")
if answer.lower() == "print()":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Used to perform mathematical operations inside our programming language? ")
if answer.lower() == "arithmetic operators":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

    
answer = input("What is langauage that depends on the compiler? ")
if answer.lower() == "compiled languages":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What software that converts the source code to machine code at once? ")
if answer.lower() == "compiler":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is langauage that depends on the interpreter? ")
if answer.lower() == "interpreted languages":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What programming languages have a syntax similar to the English language? ")
if answer.lower() == "high-level languages":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")            

print("You got " + str(score) + " questions correct")
print("You got " + str((score / 10) * 100) + "%.")
