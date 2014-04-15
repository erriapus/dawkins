import sys

sys.path.append(".")

TESTS_DIRECTORY = 'pytests'
PYTEST_FLAGS = ['--doctest-modules']

def _test():
    import pytest
    return pytest.main(PYTEST_FLAGS + [TESTS_DIRECTORY])

if __name__ == "__main__":
    _test()
