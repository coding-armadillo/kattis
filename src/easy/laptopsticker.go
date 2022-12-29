package main

import "fmt"

func main() {
	var wc, hc, ws, hs int
	fmt.Scan(&wc)
	fmt.Scan(&hc)
	fmt.Scan(&ws)
	fmt.Scan(&hs)
	if wc-2 >= ws && hc-2 >= hs {

		fmt.Println(1)

	} else {

		fmt.Println(0)

	}
}
