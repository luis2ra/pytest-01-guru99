# content of test_sample1.py


def test_file1_method1():
	x=5
	y=6
	assert x+1 == y, "test passed - note"
	assert x == y, "test failed - note"
	assert "hello" == "Hai", 'an assertion failure'
	assert 4 == 4,  'is a successful assertion'
	assert True, 'is a successful assertion'
	assert False, 'is an assertion failure.'


def test_file1_method2():
	x=5
	y=6
	assert x+1 == y, "test passed"
