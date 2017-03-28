import collections
from functools import reduce
import string
import sys

files = collections.OrderedDict() # (K, V) = (filename, list of words in file)
strip = (string.whitespace + string.punctuation + string.digits + "\"'") # Strip parameters

# Reads in words from files specified in command-line arguments
for filename in sys.argv[1:]: 						# Iterate over filenames
	with open(filename) as file:					# Open current file
		files[filename] = []						# Each filename corresponds to a list
		for line in file:							# Iterate over lines of file
			for word in line.lower().split():		# Split each line (lowercase) into words
				word = word.strip(strip)			# Strip each word using 'strip' parameters
				files[filename].append(word)		# Add it to the current file's list

# Performs a set intersection reduction on the set of words for each file
common_words = reduce(set.intersection, [set(words) for words in files.values()])

# Outputs the words common to all files
if not common_words:
	print("\nNO COMMON WORDS", end="")
else:
	print("\nCOMMON WORDS")
	for word in common_words:
		print(word, end=" ")

# Reconstructs each file's list from only words found in common_words
for filename in files:
	files[filename] = [word for word in files[filename] if word in common_words]

print() # Formatting

# Finds files whose order of the common words are the same
for current_file in list(files.keys()):								# Iterate over all files
	if current_file in files:										# If current file is in the file dictionary
		print('\n"{0}":'.format(current_file), end="")				# Print the current filename
		for other_file in list(files.keys()):						# Iterate over all files, again
			if current_file is other_file or not files[other_file]:	# If we're looking at the same file or other file's list is empty
				continue											# Continue on to next file
			elif files[current_file] == files[other_file]:			# If the lists are the same (order-sensitive)
				print(' "{0}"'.format(other_file), end=" ")			# Print the filename of the other file
				del files[other_file]								# And delete it so it doesn't come up again												# Once a file has been processed, remove it

print() # Formatting
