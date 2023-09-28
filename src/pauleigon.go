package main

import "fmt"

func main() {
	var n, p, q int
	fmt.Scan(&n)
	fmt.Scan(&p)
	fmt.Scan(&q)
	if ((p+q)/n)%2 == 0 {
		fmt.Println("paul")
	} else {
		fmt.Println("opponent")
	}
}
