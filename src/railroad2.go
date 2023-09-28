package main

import "fmt"

func main() {
	var x, y int
	fmt.Scan(&x)
	fmt.Scan(&y)
	if y%2 == 1 {
		fmt.Println("impossible")
	} else {
		fmt.Println("possible")
	}
}
