package main

// go run 2024/day5/puzzle_5.go

import (
	_ "embed"
	"fmt"
	"slices"
	"strings"

	"advent-of-code/2024/util"

	"github.com/samber/lo"
)

//go:embed input1.txt
var input1 string

//go:embed input2.txt
var input2 string

func main() {
	l1, l2 := strings.Split(input1, "\n"), strings.Split(input2, "\n")
	fmt.Println("solution 1:", solution1(l1, l2))
	fmt.Println("solution 2:", solution2(l1, l2))
}

func solution1(s1, s2 []string) (result int) {
	rule := make(map[int][]int)
	for _, s := range s1 {
		order := lo.Map(strings.Split(s, "|"), func(x string, i int) int {
			return util.StrToInt(x)
		})
		rule[order[0]] = append(rule[order[0]], order[1])
	}
next:
	for _, s := range s2 {
		page := lo.Map(strings.Split(s, ","), func(x string, i int) int {
			return util.StrToInt(x)
		})
		for i, x := range page {
			if len(lo.Intersect(page[:i], rule[x])) > 0 {
				continue next
			}
		}
		result += page[len(page)/2]
	}
	return result
}

func solution2(s1, s2 []string) (result int) {
	rule := make(map[int][]int)
	for _, s := range s1 {
		order := lo.Map(strings.Split(s, "|"), func(x string, i int) int {
			return util.StrToInt(x)
		})
		rule[order[0]] = append(rule[order[0]], order[1])
	}
	for _, s := range s2 {
		page := lo.Map(strings.Split(s, ","), func(x string, i int) int {
			return util.StrToInt(x)
		})
		ordered := false
		for i := 0; i < len(page); i++ {
			intersect := lo.Intersect(page[:i], rule[page[i]])
			if len(intersect) > 0 {
				ordered = true
				x1, x2 := slices.Index(page, page[i]), slices.Index(page, intersect[0])
				page[x1], page[x2] = page[x2], page[x1]
				i = -1 // restart loop at 0
			}
		}
		if ordered {
			result += page[len(page)/2]
		}
	}
	return result
}
