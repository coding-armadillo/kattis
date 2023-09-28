package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	a := n / 2
	b := n - a
	fmt.Println((a + 1) * (b + 1))
}
