package main

import (
    "testing"
    "github.com/stretchr/testify/assert"
)

var primeFixtures = []struct {
    max uint32
    expected []uint32
}{
    {0, []uint32{}},
    {1, []uint32{}},
    {2, []uint32{2}},
    {3, []uint32{2,3}},
    {10, []uint32{2,3,5,7}},
    {20, []uint32{2,3,5,7, 11, 13, 17, 19}},
    {100, []uint32{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}},
}

func TestPrimes(t *testing.T) {
    for _, tt := range primeFixtures {
        assert.Equal(t, tt.expected, FindPrimes(tt.max))
    }
}
