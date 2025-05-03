package main

// go run 2024/day1/puzzle_1.go

import (
	_ "embed"
	"fmt"
	"slices"
	"strings"

	"advent-of-code/2024/util"
)

//go:embed input.txt
var input string

func main() {
	lines := strings.Split(input, "\n")
	solution1and2(lines)
}

func solution1and2(lines []string) {
	var distance, similarity int
	var l1, l2 []int

	for _, line := range lines {
		v := strings.Fields(line)
		l1 = append(l1, util.StrToInt(v[0]))
		l2 = append(l2, util.StrToInt(v[1]))
	}

	slices.Sort(l1)
	slices.Sort(l2)

	for i, v := range l1 {
		distance += util.MathAbs(v - l2[i])
		similarity += v * util.SlicesCount(l2, v)
	}

	fmt.Println("solution 1:", distance)
	fmt.Println("solution 2:", similarity)
}
