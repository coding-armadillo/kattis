package main

import "fmt"

func main() {
	var m, d string
	fmt.Scan(&m)
	fmt.Scan(&d)
	if (m == "OCT" && d == "31") || (m == "DEC" && d == "25") {
		fmt.Println("yup")
	} else {
		fmt.Println("nope")
	}
}
