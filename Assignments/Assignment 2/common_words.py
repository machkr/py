import collections
from functools import reduce
import string
import sys

files = collections.OrderedDict() # (K, V) = (filename, ordered dictionary of words in file)
strip = (string.whitespace + string.punctuation + string.digits + "\"'") # Strip parameters

# Reads in words from files specified in command-line arguments
for filename in sys.argv[1:]: 						# Iterate over filenames
	with open(filename) as file:					# Open current file
		files[filename] = collections.OrderedDict() # (K, V) = (Word, Count)
		for line in file:							# Iterate over lines of file
			for word in line.lower().split():		# Split each line (lowercase) into words
				word = word.strip(strip)			# Strip each word using 'strip' parameters
				if word not in files[filename]:		# If the current word is not in the file's dictionary
					files[filename][word] = 0		# Set it's count to 0
				files[filename][word] += 1			# Increment count by one

# Performs a set intersection reduction on the set of words in each file
common_words = reduce(set.intersection, [set(words.keys()) for words in files.values()])

# Outputs the words common to all files
print("\nCOMMON WORDS")
for word in common_words:
	print(word, end=" ")

# Deletes all unique words from each file's dictionary
for filename, words in files.items():	# Iterate over all files
	for word in words.keys():			# For each word in this file
		if word not in common_words:	# If the word is not a common word
			del words[word]				# Remove it from the file's dictionary

print() # Formatting

# Finds files whose order of the common words are the same
for current_file, current_dict in files.items():						# Iterate over all files
	print('\n"{0}":'.format(current_file), end="")						# Print the current filename
	if current_dict:													# If current file's dictionary is not empty
		for other_file, other_dict in files.items():					# Iterate over all files, again
			if current_file is other_file:								# If we're looking at the same file
				continue												# Continue on to next file
			elif not other_dict:										# If other file's dictionary is empty
				del files[other_file]									# Remove it from the main file dictionary
			elif list(current_dict.keys()) == list(other_dict.keys()):	# If the dictionary keys are the same (order-sensitive)
				print(' "{0}"'.format(other_file), end=" ")				# Print the filename of the other file
				del files[other_file]									# And delete it so it doesn't come up again
	del files[current_file]												# Once a file has been processed, remove it

print() # Formatting
