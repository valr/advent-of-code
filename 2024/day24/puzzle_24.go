package main

// go run 2024/day24/puzzle_24.go

import (
	_ "embed"
	"fmt"
	"slices"
	"strconv"
	"strings"

	"advent-of-code/2024/util"
)

//go:embed input1.txt
var input1 string

//go:embed input2.txt
var input2 string

func main() {
	l1, l2 := strings.Split(input1, "\n"), strings.Split(input2, "\n")
	m1 := make(map[string]int)
	for _, l := range l1 {
		f := util.StrTrimSpaceAll(strings.Split(l, ":"))
		m1[f[0]] = util.StrToInt(f[1])
	}
	m2, w2 := make(map[string][]string), make([]string, 0)
	for _, l := range l2 {
		f := strings.Fields(l)
		m2[f[4]] = []string{f[0], f[1], f[2]}
		if f[4][0] == 'z' {
			w2 = append(w2, f[4])
		}
	}
	fmt.Println("solution 1:", solution1(m1, m2, w2))
}

func solution1(m1 map[string]int, m2 map[string][]string, w2 []string) (result int64) {
	slices.Sort(w2)
	slices.Reverse(w2)
	var s string
	for _, w := range w2 {
		s += util.IntToStr(computeWire(m1, m2, w))
	}
	result, _ = strconv.ParseInt(s, 2, 64)
	return result
}

func computeWire(m1 map[string]int, m2 map[string][]string, w string) int {
	v, ok := m1[w]
	if ok {
		return v
	}
	o1, op, o2 := computeWire(m1, m2, m2[w][0]), m2[w][1], computeWire(m1, m2, m2[w][2])
	switch op {
	case "AND":
		if o1+o2 > 1 {
			return 1
		}
	case "OR":
		if o1+o2 >= 1 {
			return 1
		}
	case "XOR":
		if o1+o2 == 1 {
			return 1
		}
	}
	return 0
}
