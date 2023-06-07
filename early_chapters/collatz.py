#collatz.py

def collatz(numbah = ""):
	'''A function that runs the collatz function to completion'''


	iterations = 0


	while True:

		if numbah == "":
			numbah = input("Enter a number: ")


		try:
			numbah = int(numbah)

			if numbah <= 0:
				numbah = input("Please try again with an integer larger than zero ")

			else:
				break

		except ValueError:
			print("Please try again with an integer!")
			numbah = input("Enter a number: ")


	while numbah != 1:

		iterations += 1

		if numbah % 2 == 0:
			numbah = numbah // 2

		elif numbah % 2 == 1:
			numbah = 3 * numbah + 1


		print(f"{iterations}: {numbah}")



	print(f"You reached 1 in {iterations} iterations! Yay!")


try:
	collatz(hjkhj)

except NameError:
	collatz()


