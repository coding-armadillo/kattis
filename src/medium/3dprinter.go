package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	fmt.Scan(&n)
	d := 1.0
	for math.Pow(2, d-1) < float64(n) {
		d += 1
	}
	fmt.Println(d)
}
