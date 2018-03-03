[![Build Status](https://travis-ci.org/Dinoshauer/name-me.svg?branch=master)](https://travis-ci.org/Dinoshauer/name-me)
[![Coverage Status](https://img.shields.io/coveralls/Dinoshauer/name-me.svg)](https://coveralls.io/r/Dinoshauer/name-me?branch=master)
[![Latest Version](https://img.shields.io/pypi/v/name-me.svg
[![License](https://img.shields.io/pypi/l/name-me.svg


NameMe
======

Generate random strings that you can actually remember.

## Installation

	pip install name-me

## Usage

	from nameme import NameMe
	from nameme.adjectives import adjective_words
	from nameme.nouns import noun_words

	name = NameMe(adjective_words, noun_words, seperator='-')

	name.regenerate_noun()
	name.regenerate_adjective()
