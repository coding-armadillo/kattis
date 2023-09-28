package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scan(&s)
	if strings.HasPrefix(s, "555") {
		fmt.Println(1)
	} else {
		fmt.Println(0)
	}
}
