package main

import "fmt"

func main() {
	var a, b, c int
	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Scan(&c)
	x := b - a
	y := c - b
	ans := x
	if ans < y {
		ans = y
	}
	ans -= 1
	fmt.Println(ans)
}
