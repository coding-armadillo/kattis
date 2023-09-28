package main

import "fmt"

func main() {
	var x, y int
	for true {
		fmt.Scan(&x)
		fmt.Scan(&y)
		if x == 0 && y == 0 {
			break
		}
		if x+y == 13 {
			fmt.Println("Never speak again.")
		} else if x > y {
			fmt.Println("To the convention.")
		} else if x == y {
			fmt.Println("Undecided.")
		} else {
			fmt.Println("Left beehind.")
		}
	}
}
