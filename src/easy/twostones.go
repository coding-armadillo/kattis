package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n%2 == 1 {
		fmt.Println("Alice")
	} else {
		fmt.Println("Bob")
	}
}
