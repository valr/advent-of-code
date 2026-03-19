package main

// go run 2025/day1/puzzle_1.go

import (
	_ "embed"
	"fmt"
	"slices"
	"strings"

	"github.com/valr/go-std/mathx"
	"github.com/valr/go-std/slicesx"
	"github.com/valr/go-std/strconvx"
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
		l1 = append(l1, strconvx.StrToInt(v[0]))
		l2 = append(l2, strconvx.StrToInt(v[1]))
	}

	slices.Sort(l1)
	slices.Sort(l2)

	for i, v := range l1 {
		distance += mathx.Abs(v - l2[i])
		similarity += v * slicesx.Count(l2, v)
	}

	fmt.Println("solution 1:", distance)
	fmt.Println("solution 2:", similarity)
}
