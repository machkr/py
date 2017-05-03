#!/usr/bin/python

import os
import math
import threading

# Global count variable
count = 0

def getpositions(fnom, chunksize):

	# List to store positions
	positions = [0]

	# Open file
	with open(fnom, 'rb') as file:

		# Loop until EOF
		while True:

			# Read chunk from file
			if not file.read(chunksize):

				# Break loop
				break

			# Get cursor position
			position = file.tell()

			# Append position to list of positions
			positions.append(position)

	print(positions)

	# Print list of positions
	return positions

def chunk_counter(f, pos, csize, b):

	# Allow function to modify global variable
	global count

	# Move cursor position
	f.seek(pos)

	# Read data from file
	data = f.read(csize)

	# For each byte in data read
	for byte in data:

		# If byte matches the one being searched for
		if byte == b:

			# Increment count
			count += 1

	# Return count
	return count

def total_counter(fnom, b):

	# Get size of file
	fsize = os.path.getsize(fnom)
	print('File Size:', fsize)

	# Chunk size
	csize = math.ceil(fsize / 100)
	print('Bytes Per Thread:', csize)

	# Get thread starting indices
	idxs = getpositions(fnom, csize)

	# List containing running threads
	threads = []

	# Open file
	with open(fnom, 'rb') as file:

		# For each thread
		for x in range(100):

			# Create new thread
			thread = threading.Thread(target=chunk_counter, 
				args=(file, idxs[x], csize, b))

			# Append to list of threads
			threads.append(thread)

		# For each thread
		for x in range(100):

			# Start each thread
			threads[x].start()

		# For each thread
		for x in range(100):

			# Wait for each thread
			threads[x].join()

	# Print count
	print('Count:', count)

def main():
	# Request filename input
	# filename = input('Filename: ')
	filename = 'text.txt'
	file = open(filename, 'rb')

	# Call function
	# getpositions(filename, 2048)
	# chunk_counter(file, 0, 34657, 99)
	total_counter(filename, 99)

if __name__ == '__main__':
	main()
