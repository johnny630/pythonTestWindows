from nose.tools import eq_

def just_do_it(text):
	return text.title()

def test_one_word():
	text = "duck"
	result = just_do_it(text)
	eq_(result , "Duck")

def test_multiple_words():
	text = "a veritable flock of ducks"
	result = just_do_it(text)
	eq_(result , "a Veritable Flock Of Ducks")