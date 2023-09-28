package main

import "fmt"

func main() {
	var a float32
	fmt.Scan(&a)
	fmt.Printf("%.10f", 100/a)
	fmt.Println()
	fmt.Printf("%.10f", 100/(100-a))
}
