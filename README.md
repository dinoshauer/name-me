NameMe
======

# Usage

	from name.adjectives import adjective_words
	from name.nouns import noun_words

	name = NameMe(adjective_words, noun_words, seperator='-')

	name.regenerate_noun()
	name.regenerate_adjective()
