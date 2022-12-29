package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	line := scanner.Text()
	if strings.HasSuffix(line, "eh?") {
		fmt.Println("Canadian!")
	} else {
		fmt.Println("Imposter!")
	}
}
