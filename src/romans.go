package main

import "fmt"

func main() {
	var x float64
	fmt.Scan(&x)
	fmt.Println(int(x*1000*5280/4854 + 0.5))
}
