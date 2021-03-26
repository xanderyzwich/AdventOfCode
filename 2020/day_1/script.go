package day1

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func expenseReport (input [] int, addTo int) int {
	if addTo == 0 {
		addTo = 2020
	}

	var i, j = 0, len(input) - 1
	//fmt.Println(addTo, input)
	for i <= j {
		var left, right = input[i], input[j]
		var total = left + right

		if total < addTo {
			i++
		} else if total > addTo {
			j--
		} else {
			//fmt.Println("exiting expense report from:", left, right, left * right)
			return left * right
		}

	}
	return 0
}

func convert(fileName string) [] int {
	var output []int
	f, _ := os.Open(fileName)
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		s, _ := strconv.Atoi(scanner.Text())
		output = append(output, s)
	}
	sort.Ints(output)
	return output
}

func threeFerReport(input []int) int {
	for i := 0; i < len(input); i++ {
		temp_result := expenseReport(input[i+1:], 2020-input[i])
		if temp_result != 0 {
			return temp_result * input[i]
		}
	}
	return 0
}

func main() {
	example := []int{1721, 979, 366, 299, 675, 1456}
	fmt.Println("Pt1 w/example data", expenseReport(example, 2020))
	fmt.Println()
}