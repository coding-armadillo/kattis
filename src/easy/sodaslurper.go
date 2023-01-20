package main

import "fmt"

func main() {
	var e, f, c int
	fmt.Scan(&e)
	fmt.Scan(&f)
	fmt.Scan(&c)
	total := 0
	s := e + f
	for s >= c {
		total += s / c
		s = s%c + s/c
	}
	fmt.Println(total)
}
