package main

import (
	"fmt"
	"strings"
)

func main() {
	var a, b string
	fmt.Scan(&a)
	fmt.Scan(&b)
	if strings.Count(a, "a") >= strings.Count(b, "a") {
		fmt.Println("go")
	} else {
		fmt.Println("no")
	}
}
