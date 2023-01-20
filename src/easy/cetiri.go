package main

import (
	"fmt"
	"sort"
)

func main() {
	var a, b, c int
	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Scan(&c)
	s := []int{a, b, c}
	sort.Ints(s)
	a, b, c = s[0], s[1], s[2]
	if c-b == b-a {
		fmt.Println(c + c - b)
	} else if c-b > b-a {
		fmt.Println(c - b + a)
	} else {
		fmt.Println(a + c - b)
	}
}
