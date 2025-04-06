package errorhandling

import "fmt"

// write way handle error with error data type

func divide(a, b float64) (float64, error) { // return error type data
	if b == 0 {
		return 0, fmt.Errorf("denominator must not be zero")
	}
	return a / b, nil
}

// func divide(a, b float64) (float64, string) { // return string type data
// 	if b == 0 {
// 		return 0, "denominator must not be zero"
// 	}
// 	return a / b, "nil"
// }

func ErrorHandler() {

	// custom error handling
	// error returened from the divide function

	// ans, err := divide(10, 0)

	// if err != nil {
	// 	fmt.Println("> Error handling <")
	// }

	// Blank identifier that discard any value returend function and or
	// we don't want to use it anymore

	ans, _ := divide(10, 0)

	fmt.Println("Division answer is : ", ans)
}
