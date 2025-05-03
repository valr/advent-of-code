package main

// go run 2024/day24/puzzle_24.go

import (
	_ "embed"
	"fmt"
	"slices"
	"strings"

	"advent-of-code/2024/util"
)

//go:embed input1.txt
var input1 string

//go:embed input2.txt
var input2 string

var opcode = map[string][]int{"XOR": {1}, "OR": {1, 2}, "AND": {2}}

func main() {
	l1, l2 := strings.Split(input1, "\n"), strings.Split(input2, "\n")
	m1 := make(map[string]int)
	for _, l := range l1 {
		f := strings.Split(l, ": ")
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

func solution1(m1 map[string]int, m2 map[string][]string, w2 []string) (result int) {
	slices.Sort(w2)
	for i, v := range w2 {
		result += computeWire(m1, m2, v) << i
	}
	return result
}

func computeWire(m1 map[string]int, m2 map[string][]string, w string) int {
	if v, ok := m1[w]; ok {
		return v
	}
	o1, op, o2 := computeWire(m1, m2, m2[w][0]), m2[w][1], computeWire(m1, m2, m2[w][2])
	if slices.Contains(opcode[op], o1+o2) {
		return 1
	} else {
		return 0
	}
}
