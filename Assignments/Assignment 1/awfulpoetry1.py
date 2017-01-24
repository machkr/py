import random

articles = ["the", "a", "another", "their", "my", "his", "her"]
subjects = ["sausage", "wizard", "toy", "robe", "taco", "muffin", "globe", "belly button"]
verbs = ["squealed", "dribbled", "exalted", "creaked", "snorted", "swung", "squirted"]
adverbs = ["mysteriously", "shamelessly", "finely", "severely", "suddenly", "dryly", "ferociously"]

for _ in [1, 2, 3, 4, 5]:
	article = random.choice(articles)
	subject = random.choice(subjects)
	verb = random.choice(verbs)
	adverb = random.choice(adverbs)

	if(random.randint(0, 1) == 0):
		print(article, subject, verb, adverb)
	else:
		print(article, subject, verb)
