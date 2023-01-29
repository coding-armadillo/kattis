package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	mapping := map[string]string{
		"a": "@",
		"b": "8",
		"c": "(",
		"d": "|)",
		"e": "3",
		"f": "#",
		"g": "6",
		"h": "[-]",
		"i": "|",
		"j": "_|",
		"k": "|<",
		"l": "1",
		"m": "[]\\/[]",
		"n": "[]\\[]",
		"o": "0",
		"p": "|D",
		"q": "(,)",
		"r": "|Z",
		"s": "$",
		"t": "']['",
		"u": "|_|",
		"v": "\\/",
		"w": "\\/\\/",
		"x": "}{",
		"y": "`/",
		"z": "2",
	}
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	line := scanner.Text()
	runes := []rune(strings.ToLower(line))
	for i := 0; i < len(runes); i++ {
		v, ok := mapping[string(runes[i])]
		if ok {
			fmt.Printf(v)
		} else {
			fmt.Printf(string(runes[i]))
		}
	}
}
