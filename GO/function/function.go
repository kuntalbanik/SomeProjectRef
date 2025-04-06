package function

import "fmt"

func SimpleFunction() {
	fmt.Println("Simple function")
}
func Add(a, b int) int { // same as func Add(a int, b int) int
	// func Add(a, b int) (result int) {
	return a + b
}

func Multiply(a, b int) int {
	return a * b
}
