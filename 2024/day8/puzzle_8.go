package main

// go run 2024/day8/puzzle_8.go

import (
	_ "embed"
	"fmt"
	"strings"

	"advent-of-code/2024/util"

	"github.com/samber/lo"
)

//go:embed input.txt
var input string

func main() {
	lines := strings.Split(input, "\n")
	fmt.Printf("solution 1: %v\nsolution 2: %v\n", util.Wrap(solution1and2(lines))...)
}

func solution1and2(lines []string) (int, int) {
	m := buildMatrix(lines)
	return walkMatrix(m, setAntinodes1), walkMatrix(m, setAntinodes2)
}

func buildMatrix(lines []string) (arr [][]rune) {
	arr = make([][]rune, len(lines))
	for i := range lines {
		arr[i] = make([]rune, len(lines[i]))
		for j, r := range lines[i] {
			if r != '.' {
				arr[i][j] = r
			}
		}
	}
	return arr
}

func walkMatrix(arr [][]rune, setAntinodes func(i int, j int, arr [][]rune, res [][]int)) int {
	res := make([][]int, len(arr))
	for i := range res {
		res[i] = make([]int, len(arr[i]))
	}
	for i := range arr {
		for j := range arr[i] {
			if arr[i][j] != 0 {
				setAntinodes(i, j, arr, res)
			}
		}
	}
	return lo.Sum(lo.Flatten(res))
}

func setAntinodes1(i int, j int, arr [][]rune, res [][]int) {
	for y := range arr {
		for x := range arr[y] {
			if i != y && j != x && arr[i][j] == arr[y][x] {
				di, dj := util.MathAbs(i-y), util.MathAbs(j-x)
				ai, aj := i, j
				if i < y {
					ai -= di
				} else {
					ai += di
				}
				if j < x {
					aj -= dj
				} else {
					aj += dj
				}
				if ai >= 0 && ai < len(arr) && aj >= 0 && aj < len(arr[i]) {
					res[ai][aj] = 1
				}
			}
		}
	}
}

func setAntinodes2(i int, j int, arr [][]rune, res [][]int) {
	for y := range arr {
		for x := range arr[y] {
			if i != y && j != x && arr[i][j] == arr[y][x] {
				di, dj := util.MathAbs(i-y), util.MathAbs(j-x)
				ai, aj := i, j
				for {
					if ai < 0 || ai >= len(arr) || aj < 0 || aj >= len(arr[i]) {
						break
					}
					res[ai][aj] = 1
					if i < y {
						ai -= di
					} else {
						ai += di
					}
					if j < x {
						aj -= dj
					} else {
						aj += dj
					}
				}
			}
		}
	}
}
