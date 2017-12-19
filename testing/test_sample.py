# content of test_sample.py
def func(x: int) -> str:
    return x + 1

def test_answer():
    assert func(3) == 5

class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')