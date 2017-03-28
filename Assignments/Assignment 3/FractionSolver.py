import fractions
import operator
import re
import sys

# Regular expression pattern
pattern = re.compile('([-]?[\d]+)\/([-]?[\d]+)\s?([+\-/*])\s?([-]?[\d]+)\/([-]?[\d]+)')

# Arithmetic operator lookup table
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

# Main program loop
while True:
	# Collect input, store in string
	string = input()

	# Break if string is empty
	if not string:
		break

	# General error catching
	try:
		# Find regular expression
		parts = re.findall(pattern, string)

		# Define operands
		x = fractions.Fraction(int(parts[0][0]), int(parts[0][1]))
		y = fractions.Fraction(int(parts[0][3]), int(parts[0][4]))

		# Calculate result
		r = fractions.Fraction(ops[parts[0][2]](x, y))

		# Print output
		print(string, "=", r)
	# Catch any exception
	except Exception as exception:
		# Print exception
		print(exception)

		# Continue loop
		continue
