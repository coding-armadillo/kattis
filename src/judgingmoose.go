package main

import "fmt"

func main() {
	var l, r int
	fmt.Scan(&l)
	fmt.Scan(&r)
	if l == 0 && r == 0 {
		fmt.Println("Not a moose")
	} else {
		p := 2 * l
		if r > l {
			p = 2 * r
		}
		t := "Odd"
		if l == r {
			t = "Even"
		}
		fmt.Println(t, p)
	}
}
