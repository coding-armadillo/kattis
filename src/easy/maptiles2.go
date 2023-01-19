package main

import (
	"fmt"
	"math"
)

func main() {
	var s string
	fmt.Scanln(&s)
	zoom := len(s)
	var x, y float64
	for i := 0; i < zoom; i++ {
		d := math.Pow(2, float64(zoom)-float64(i)-1)
		if s[i] == '1' {
			x += d
		} else if s[i] == '2' {
			y += d
		} else if s[i] == '3' {
			x += d
			y += d
		}
	}
	fmt.Printf("%d %d %d", zoom, int64(x), int64(y))
}
