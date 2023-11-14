package main

import "fmt"

func f(n int) int {
	if n == 0 {
		return 1
	} else if n == 1 {
		return 1
	} else if n == 2 {
		return 2
	} else {
		return f(n-1) + f(n-2) + f(n-3)
	}

}

func main() {
	var n int
	fmt.Scan(&n)
	fmt.Println(f(n))
}
