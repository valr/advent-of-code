package main

// go run 2024/day3/puzzle_3.go

import (
	_ "embed"
	"fmt"
	"regexp"
	"strings"

	"advent-of-code/2024/util"
)

//go:embed input.txt
var input string

func main() {
	fmt.Println("solution 1:", solution1(input))
	fmt.Println("solution 2:", solution2(input))
}

func solution1(s string) (result int) {
	re := regexp.MustCompile(`mul\((?<num>\d+,\d+)\)`)
	matches := re.FindAllStringSubmatch(s, -1)
	for _, m := range matches {
		s1, s2, _ := strings.Cut(m[1], ",")
		result += util.StrToInt(s1) * util.StrToInt(s2)
	}
	return result
}

func solution2(s string) (result int) {
	re := regexp.MustCompile(`mul\((?<num>\d+,\d+)\)|do\(\)|don't\(\)`)
	matches := re.FindAllStringSubmatch(s, -1)
	mul := true
	for _, m := range matches {
		switch m[0] {
		case "do()":
			mul = true
		case "don't()":
			mul = false
		default:
			if mul {
				s1, s2, _ := strings.Cut(m[1], ",")
				result += util.StrToInt(s1) * util.StrToInt(s2)
			}
		}
	}
	return result
}
