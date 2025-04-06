package myinput

import (
	"bufio"
	"fmt"
	"os"
)

func CustomInput() {
	fmt.Println("Enter your name: ")
	// name := ""
	// fmt.Scan(&name)
	// fmt.Println("You name : ", name)

	reader := bufio.NewReader(os.Stdin)
	name, _ := reader.ReadString('\n')
	fmt.Println("You name : ", name)
}
