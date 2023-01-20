package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scan(&s)
	index := strings.Index(s, "a")
	fmt.Println(s[index:])
}
