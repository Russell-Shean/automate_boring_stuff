#zigzag.py

import time
import sys

increasing = True
pattern = "********"
indent = 0

try:
	while True:
		time.sleep(0.1)
		# print(" " * indent, end = "")


		if increasing:
			indent += 1

			if indent > 19:
				increasing = False


		else:
			indent -= 1

			if indent < 1:
				increasing = True

		print(" " * indent + pattern)

except KeyboardInterrupt:
	print("\n\tGoodbye!")
	sys.exit()

# Documents/python_projects/automate_boring_stuff/early_chapters