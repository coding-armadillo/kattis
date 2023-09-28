package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	a := 1
	b := 0
	for i := 0; i < n; i++ {
		a, b = b, b+a
	}
	fmt.Println(a, b)
}
