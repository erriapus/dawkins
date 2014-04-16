import pytest
from pytest import raises
from rotatedsorted import rotate_search

SKIP = False

class TestA(object):
    def test1(self, inputs):
        assert 26 == len(inputs)

    @pytest.mark.skipif(SKIP, reason="none")
    def test_sorted(self, inputs):
        fixture = inputs[0]
        print fixture
        assert fixture[2] == rotate_search(fixture[1], fixture[0])

    @pytest.mark.skipif(SKIP, reason="none")
    def test_singles(self, inputs):
        fixtures = inputs[1:3]
        for f in fixtures:
            assert f[2] == rotate_search(f[1], f[0])

    @pytest.mark.skipif(SKIP, reason="none")
    def test_odd(self, inputs):
        fixtures = inputs[7:18]
        for f in fixtures:
            assert f[2] == rotate_search(f[1], f[0])

    def test_odd2(self, inputs):
        fixtures = inputs[18:23]
        for f in fixtures:
            assert f[2] == rotate_search(f[1], f[0])

    def test_odd2(self, inputs):
        fixtures = inputs[23:27]
        for f in fixtures:
            assert f[2] == rotate_search(f[1], f[0])

    def test_both_halves_sorted(self, inputs):
        #([3, 4, 1, 2], 4, 1),
        fixture = inputs[4]
        print fixture
        assert fixture[2] == rotate_search(fixture[1], fixture[0])

    @pytest.mark.skipif(SKIP, reason="none")
    def test_weird(self, inputs):
        fixtures = [ inputs[3], inputs[5] ]
        for f in fixtures:
            assert f[2] == rotate_search(f[1], f[0])

    @pytest.mark.skipif(SKIP, reason="none")
    def test_missing(self, inputs):
        fixture = inputs[6]
        print fixture
        assert fixture[2] == rotate_search(fixture[1], fixture[0])
