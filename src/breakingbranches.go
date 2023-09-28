package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n%2 == 0 {
		fmt.Println("Alice")
		fmt.Println(1)
	} else {
		fmt.Println("Bob")
	}
}
