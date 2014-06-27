all: test

test: testpy testgo

testjs:
	node index.js

testgo:
	make -C primes all

testjava:
	make -C filesize all

testpy: collect1

collect1:
	python testify.py

collect2:
	python -m doctest powersof2/__init__.py
