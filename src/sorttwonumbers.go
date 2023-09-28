package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a)
	fmt.Scan(&b)
	if a < b {
		fmt.Printf("%d %d\n", a, b)
	} else {
		fmt.Printf("%d %d\n", b, a)
	}
}
