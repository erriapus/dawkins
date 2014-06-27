package main

import (
    "fmt"
)

// Given an upper limit `max`, it will return a slice of all
// primes less than or equal to N
func findPrimes(max uint32) []uint32 {
    //Create a list of integers from 0 to the MAX
    x := make([]uint32, max)
    for i, _ := range x {
        if i >= 2 {
            x[i] = uint32(i)
        }
        fmt.Printf("%d - %d\n", i, x[i])
    }


//-Start with 2, set all list indices which are multiples of 2 to 0
//--Find the next non-zero integer in the list, this is the next prime
//--Zero out the list indices which are multiples of the new prime
//-Repeat until you have reached the sqrt(MAX) + 1
//-Now your list is all primes and 0s, remember to also zero out number 1


    return x
}

func main() {
    fmt.Printf("%#v\n", findPrimes(10))
    fmt.Printf("%#v\n", findPrimes(4))
}
