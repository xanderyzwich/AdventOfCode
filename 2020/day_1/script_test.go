package day1

import (
	"testing"
)

var example = []int{1721, 979, 366, 299, 675, 1456}

func Test_Part1_Example(t *testing.T)  {
	expense := expenseReport(example, 2020)
	//fmt.Println("Part 1 - Example")
	if 514579 != expense {
		t.Errorf("Expense for example expected %d and got %d", 514579, expense)
	}
}

func Test_Part1_Data(t *testing.T) {
	data := convert("day1.part1.txt")
	expense := expenseReport(data, 2020)
	//fmt.Println("Part 1 - Data")
	if 913824 != expense {
		t.Errorf("Expense for data expected %d and got %d", 913824, expense)
	}
}

func Test_Part2_Example(t *testing.T) {
	data := threeFerReport(example)
	if 241861950 != data {
		t.Errorf("Expected %d and got %d", 241861950, data)
	}
}

func Test_Part2_Data(t *testing.T) {
	data := convert("day1.part1.txt")
	expense := threeFerReport(data)
	if 240889536 != expense {
		t.Errorf("Expense for data expected %d and got %d", 240889536, expense)
	}
}