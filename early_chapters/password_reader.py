#password_reader.py

password_file = open('SecretPasswordFile.txt')
password = password_file.read()

print("Enter your password ")

password_attempt = input()

if password_attempt == password:
	print("Access Granted!")
	if password_attempt == "12345":
		print("That's a terrible password!")

else:
	print("Access Denied!")