package arraydata

import "fmt"

func Array() {
	var Name [2]string
	Name[0] = "John"
	Name[1] = "Jane"
	fmt.Println(Name)

	var numbers = [5]int{1, 2, 3, 4}
	fmt.Println(numbers)
}
