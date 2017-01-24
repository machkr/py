import random
import sys

articles = ["the", "a", "another", "their", "my", "his", "her"]
subjects = ["sausage", "wizard", "toy", "robe", "taco", "muffin", "globe", "belly button"]
verbs = ["squealed", "dribbled", "exalted", "creaked", "snorted", "swung", "squirted"]
adverbs = ["mysteriously", "shamelessly", "finely", "severely", "suddenly", "dryly", "ferociously"]

num = 5

if len(sys.argv) > 1:
	tmp = int(sys.argv[1])
	if 1 <= tmp <= 10:
		num = tmp

while num > 0:
	article = random.choice(articles)
	subject = random.choice(subjects)
	verb = random.choice(verbs)
	adverb = random.choice(adverbs)

	if(random.randint(0, 1) == 0):
		print(article, subject, verb, adverb)
	else:
		print(article, subject, verb)

	num = num - 1
