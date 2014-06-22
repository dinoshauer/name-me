NameMe
======

# Usage

	from nameme import NameMe
	from nameme.adjectives import adjective_words
	from nameme.nouns import noun_words

	name = NameMe(adjective_words, noun_words, seperator='-')

	name.regenerate_noun()
	name.regenerate_adjective()
