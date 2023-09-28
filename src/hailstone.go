package main

import (
	"fmt"
)

func h(n int) int {
	if n == 1 {
		return 1
	} else if n%2 == 0 {
		return n + h(n/2)
	} else {
		return n + h(3*n+1)
	}
}

func main() {
	var n int
	fmt.Scan(&n)
	fmt.Println(h(n))
}
