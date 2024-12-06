package main

// go run 2024/day6/puzzle_6.go

import (
	_ "embed"
	"fmt"
	"strings"

	"github.com/samber/lo"
)

const (
	clear = iota
	obstacle
	walked
)

//go:embed input.txt
var input string

func main() {
	lines := strings.Split(input, "\n")
	fmt.Println("solution 1:", solution1(lines))
	fmt.Println("solution 2:", solution2(lines))
}

func solution1(lines []string) int {
	return walkMatrix(buildMatrix(lines))
}

func solution2(lines []string) (count int) {
	m, y, x := buildMatrix(lines)
	for i := range m {
		for j := range m[i] {
			mm := copyMatrix(m)
			if mm[i][j] == clear {
				mm[i][j] = obstacle
				if walkMatrix(mm, y, x) == 0 {
					count++
				}
			}
		}
	}
	return count
}

func buildMatrix(lines []string) (arr [][]int, y int, x int) {
	arr = make([][]int, len(lines))
	for i := range lines {
		arr[i] = make([]int, len(lines[i]))
		for j, r := range lines[i] {
			switch r {
			case rune('#'):
				arr[i][j] = obstacle
			case rune('^'):
				arr[i][j] = walked
				y, x = i, j
			}
		}
	}
	return arr, y, x
}

func copyMatrix(arr [][]int) [][]int {
	dup := make([][]int, len(arr))
	for i := range arr {
		dup[i] = make([]int, len(arr[i]))
		copy(dup[i], arr[i])
	}
	return dup
}

func walkMatrix(arr [][]int, y int, x int) int {
	loop := 0
	dy, dx := -1, 0
	for {
		yy, xx := y+dy, x+dx
		if yy < 0 || xx < 0 || yy >= len(arr) || xx >= len(arr[yy]) {
			break
		}
		if arr[yy][xx] == obstacle {
			switch {
			case dy == -1 && dx == 0:
				dy, dx = 0, 1
			case dy == 0 && dx == 1:
				dy, dx = 1, 0
			case dy == 1 && dx == 0:
				dy, dx = 0, -1
			case dy == 0 && dx == -1:
				dy, dx = -1, 0
			}
		} else {
			y, x = yy, xx
			arr[y][x] = walked
		}
		loop++
		if loop > 10000 { // very complex loop detection algorithm
			return 0
		}
	}
	return len(lo.Filter(lo.Flatten(arr), func(x int, i int) bool {
		return x == walked
	}))
}
