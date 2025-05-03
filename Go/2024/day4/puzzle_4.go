package main

// go run 2024/day4/puzzle_4.go

import (
	_ "embed"
	"fmt"
	"strings"

	"advent-of-code/2024/util"
)

//go:embed input.txt
var input string

func main() {
	lines := strings.Split(input, "\n")
	fmt.Println("solution 1:", solution1(lines))
	fmt.Println("solution 2:", solution2(lines))
}

func solution1(lines []string) int {
	var count int

	// This is definitely not the most efficient solution, but the idea here is
	// to improve the util package by adding extra functions that may be reused
	// in future Advent of Code exercices.

	s := strings.Join(lines, " ")
	count += strings.Count(s, "XMAS")
	s = util.StrReverse(s)
	count += strings.Count(s, "XMAS")

	s = strings.Join(util.StrRotateMatrix(lines), " ")
	count += strings.Count(s, "XMAS")
	s = util.StrReverse(s)
	count += strings.Count(s, "XMAS")

	s = strings.Join(util.StrDiagonalMatrix(lines), " ")
	count += strings.Count(s, "XMAS")
	s = util.StrReverse(s)
	count += strings.Count(s, "XMAS")

	s = strings.Join(util.StrCounterDiagonalMatrix(lines), " ")
	count += strings.Count(s, "XMAS")
	s = util.StrReverse(s)
	count += strings.Count(s, "XMAS")

	return count
}

func solution2(lines []string) int {
	var count int
	for i := range len(lines) - 2 {
		for j := range len(lines[i]) - 2 {
			s1 := lines[i][j:j+1] + lines[i+1][j+1:j+2] + lines[i+2][j+2:j+3]
			s2 := lines[i][j+2:j+3] + lines[i+1][j+1:j+2] + lines[i+2][j:j+1]
			if checkXmas(s1, s2) {
				count++
			}
		}
	}
	return count
}

func checkXmas(s1, s2 string) bool {
	return s1 == "MAS" && s2 == "MAS" ||
		s1 == "MAS" && s2 == "SAM" ||
		s1 == "SAM" && s2 == "MAS" ||
		s1 == "SAM" && s2 == "SAM"
}
