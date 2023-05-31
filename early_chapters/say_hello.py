# say_hello.py

print("Hi! I'm going to ask some questions")

name = input("What is your name? ")
print(f"It's nice to meet you {name}")
print(name + ", right?")

print(f"There are {len(name)} letters in your name!")

age = input("What is your age? ")

if int(age) >= 21:
	print("You're old enough to buy beer!")

print("You will be " + str(int(age) +1) + " within the next year!")

print(f"You'll be {int(age) + 1} in a year!")