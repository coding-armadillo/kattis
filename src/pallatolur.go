package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a)
	fmt.Scan(&b)

	if (a <= 2) && (2 <= b) {
		fmt.Println("1")
		fmt.Println("2")
	} else {
		fmt.Println(":(")
	}
}
