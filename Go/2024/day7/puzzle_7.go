package main

// go run 2024/day7/puzzle_7.go

import (
	_ "embed"
	"fmt"
	"strings"

	"github.com/valr/go-std/slicesx"
	"github.com/valr/go-std/strconvx"
	"github.com/valr/go-std/util"
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
		val := strconvx.StrToInt(s1)
		num := slicesx.Map(strings.Fields(s2), func(x string) int {
			return strconvx.StrToInt(x)
		})
		if slicesx.Count(getResults(num, nil, false), val) > 0 {
			res1 += val
		}
		if slicesx.Count(getResults(num, nil, true), val) > 0 {
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
			nres = append(nres, n+num[0], n*num[0])
			if withConcat {
				nres = append(nres, strconvx.StrToInt(strconvx.IntToStr(n)+strconvx.IntToStr(num[0])))
			}
		}
	}
	return getResults(num[1:], nres, withConcat)
}
