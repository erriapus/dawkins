import pytest
from pytest import raises
from rotatedsorted import rotate

class TestA(object):
    def test1(self, inputs):
        assert 2 == rotate()
        assert 5 == len(inputs)
