[![Build Status](https://travis-ci.org/Dinoshauer/name-me.svg?branch=master)](https://travis-ci.org/Dinoshauer/name-me)
[![Coverage Status](https://coveralls.io/repos/Dinoshauer/name-me/badge.png)](https://coveralls.io/r/Dinoshauer/name-me)


NameMe
======

# Usage

	from nameme import NameMe
	from nameme.adjectives import adjective_words
	from nameme.nouns import noun_words

	name = NameMe(adjective_words, noun_words, seperator='-')

	name.regenerate_noun()
	name.regenerate_adjective()
