import unittest

from nameme.adjectives import adjective_words
from nameme.nouns import noun_words
from nameme import NameMe


class TestCase(unittest.TestCase):
	def setUp(self):
		self.name = NameMe(adjective_words, noun_words)

class DefaultSeperatorIsSpace(TestCase):
	def test(self):
		assert self.name.seperator == ' '

class NameIsGeneratedCorrectly(TestCase):
	def test(self):
		manual_name = self.name.first_part + self.name.seperator + self.name.last_part
		assert self.name.name == manual_name

class IsString(TestCase):
    def test(self):
		assert isinstance(self.name.name, str)

class RegeneratedWordISNotTheSame(TestCase):
	def test_first_part(self):
		original_word = self.name.first_part
		original_index = self.name.adjective_index
		self.name.regenerate_adjective()
		assert original_word != self.name.first_part
		assert original_index != self.name.adjective_index

	def test_last_part(self):
		original_word = self.name.last_part
		original_index = self.name.noun_index
		self.name.regenerate_noun()
		assert original_word != self.name.last_part
		assert original_index != self.name.noun_index

if __name__ == '__main__':
    unittest.main()
