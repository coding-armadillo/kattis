package main

import (
    "fmt"
    "strings"
)

func main() {
    var s string
    fmt.Scan(&s)
    if strings.Contains(s, "COV") {
        fmt.Println("Veikur!")
    } else {
        fmt.Println("Ekki veikur!")
    }
}
