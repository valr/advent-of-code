package main

// go run 2024/day2/puzzle_2.go

import (
	_ "embed"
	"fmt"
	"slices"
	"strings"

	"github.com/valr/go-std/mathx"
	"github.com/valr/go-std/strconvx"
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
		for f := range strings.FieldsSeq(line) {
			l = append(l, strconvx.StrToInt(f))
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
		for f := range strings.FieldsSeq(line) {
			l = append(l, strconvx.StrToInt(f))
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
		abs := mathx.Abs(l[i] - l[i+1])
		if incr && l[i] > l[i+1] ||
			!incr && l[i] < l[i+1] ||
			abs < 1 || abs > 3 {
			return false
		}
	}
	return true
}
