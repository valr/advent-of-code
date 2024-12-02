package main

// go run 2024/day2/puzzle_2.go

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
	fmt.Println("solution 1:", solution1(lines))
	fmt.Println("solution 2:", solution2(lines))
}

func solution1(lines []string) int {
	var safe int
	for _, line := range lines {
		var l []int
		for _, f := range strings.Fields(line) {
			l = append(l, util.StrToInt(f))
		}
		if is_safe(l) {
			safe++
		}
	}
	return safe
}

func solution2(lines []string) int {
	var safe int
next:
	for _, line := range lines {
		var l []int
		for _, f := range strings.Fields(line) {
			l = append(l, util.StrToInt(f))
		}
		if is_safe(l) {
			safe++
			continue next
		}
		for i := range len(l) {
			ll := slices.Concat(l[:i], l[i+1:])
			if is_safe(ll) {
				safe++
				continue next
			}
		}
	}
	return safe
}

func is_safe(l []int) bool {
	var incr bool
	for i := range len(l) - 1 {
		if i == 0 {
			if l[i] < l[i+1] {
				incr = true
			} else if l[i] > l[i+1] {
				incr = false
			} else {
				return false
			}
		}
		abs := util.MathAbs(l[i] - l[i+1])
		if incr && l[i] > l[i+1] ||
			!incr && l[i] < l[i+1] ||
			abs < 1 || abs > 3 {
			return false
		}
	}
	return true
}
