package main

import (
	"fmt"
)

func reverse(str string) (ans string) {
	for _, v := range str {
		ans = string(v) + ans
	}
	return
}
func main() {
	var str string
	fmt.Scan(&str)
	fmt.Println(reverse(str))
}
