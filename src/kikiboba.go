package main

import (
	"fmt"
	"strings"
)

func main() {
	var w string
	fmt.Scan(&w)
	b := strings.Count(w, "b")
	k := strings.Count(w, "k")
	if b > k {
		fmt.Println("boba")
	} else if b < k {
		fmt.Println("kiki")
	} else if b > 0 {
		fmt.Println("boki")
	} else {
		fmt.Println("none")
	}
}
