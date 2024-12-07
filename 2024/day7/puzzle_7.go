package main

// go run 2024/day7/puzzle_7.go

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

func solution1and2(lines []string) (res1, res2 int) {
	for _, l := range lines {
		s1, s2, _ := strings.Cut(l, ":")
		val := util.StrToInt(s1)
		num := lo.Map(strings.Fields(s2), func(x string, i int) int {
			return util.StrToInt(x)
		})
		if util.SlicesCount(getResults(num, []int{}, false), val) > 0 {
			res1 += val
		}
		if util.SlicesCount(getResults(num, []int{}, true), val) > 0 {
			res2 += val
		}
	}
	return res1, res2
}

func getResults(num []int, res []int, withConcat bool) []int {
	var nres []int
	if len(num) == 0 {
		return res
	}
	if len(res) == 0 {
		nres = append(nres, num[0])
	} else {
		for _, n := range res {
			nres = append(nres, n+num[0])
			nres = append(nres, n*num[0])
			if withConcat {
				nres = append(nres, util.StrToInt(util.IntToStr(n)+util.IntToStr(num[0])))
			}
		}
	}
	return getResults(num[1:], nres, withConcat)
}
