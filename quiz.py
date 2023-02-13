"""
we ask question and take input from the user and store it and compare it with our answer
we make a variable to keep score
"""

print("Welcome")
print("\n")
print("All answers in lowercase please ")
print("Answer yes or no in the questions")
print("\n" * 3)

playing = input("Do you wish to play? \n")
print("type yes to proceed")
score = 0
if playing.lower() != "yes":
    quit()


print('*' * 10)
print("Start")
print('*' * 10)

answer = input("Is the ALX Certificate accepted globlally?\n")
if answer.lower() == "yes":
    print("correct")
    score += 1
else:
    print("incorrect")
print("ALX and Holberton certificate is an internationally recognized coding school")

answer = input("what does ALX stand for?\n").lower()
if answer == "africa leadership academy":
    print("correct")
    score += 1
else:
    print("incorrect")
print("ALX Stand for africa leadership but the 'X' Is to be interpreted by you")

answer = input("who is the founder of ALX Group ?\n").lower()
if answer == "fred swaniker":
    print("correct")
    score += 1
else:
    print("incorrect")
print("fred swaniker established alx in 2018")

answer = input("Are ALX courses self paced?\n").lower()
if answer == "yes":
    print("correct")
    score += 1
else:
    print("incorrect")
print("alx courses are online and self paced")

answer = input("Who funds ALX?\n").lower()
if answer == "mastercard foundation":
    print("correct")
    score += 1
else:
    print("incorrect")
print("alx is funded master card foundation and patners")
print(f"your got {score} out of 5; {(score / 5) * 100}%")
