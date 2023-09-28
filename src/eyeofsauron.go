package main

import (
	"fmt"
	"strings"
)

func main() {
	var drawing string
	fmt.Scan(&drawing)
	parts := strings.Split(drawing, "()")
	left, right := parts[0], parts[1]
	if left == right {
		fmt.Println("correct")
	} else {
		fmt.Println("fix")
	}
}
