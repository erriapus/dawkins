package main

import (
    "fmt"
    "math"
    "github.com/javouhey/iter"
)

// Given an upper limit N (i.e. `max` argument), 
// return all primes less than or equal to N.
func FindPrimes(max uint32) []uint32 {
    x := make([]uint32, max + 1)
    for i, _ := range x {
        if i >= 2 {
            x[i] = uint32(i)
        }
    }

    for i, _ := range x {
        // the first prime begin at 2
        if i < 2 {
            continue
        }
        index := i
        for j := range iter.M(len(x) - index) {
            // look for a non-zero prime candidate
            if x[index + j] == 0 {
                continue
            }

            // zero out all multiples
            thisPrime := index + j
            k := 2
            for {
                c := thisPrime * k
                if c >= len(x) {
                    break
                }
                x[c] = 0
                k = k + 1
            }

            if thisPrime >= int(math.Sqrt(float64(max))) + 1 {
                break
            }
        }
    }
    return filterNonZero(x)
}

func filterNonZero(s []uint32) []uint32 {
    x := make([]uint32, 0)
    for _, item := range s {
        if item != 0 {
            x = append(x, item)
        }
    }
    return x
}

func main() {
    do(1)
    do(2)
    do(4)
    do(10)
    do(100)
}

func do(n uint32) {
    primes := FindPrimes(n)
    for _, val := range primes {
        fmt.Printf("%d ", val)
    }
    fmt.Println()
}
