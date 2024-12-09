package main

// go run 2024/day9/puzzle_9.go

import (
	_ "embed"
	"fmt"
	"slices"

	"advent-of-code/2024/util"

	"github.com/samber/lo"
)

//go:embed input.txt
var input string

func main() {
	fmt.Println("solution 1:", solution1(input))
	fmt.Println("solution 2:", solution2(input))
}

func solution1(s string) (res int) {
	var block []int
	var num int
	for i, x := range s {
		if i%2 == 0 {
			for range util.StrToInt(string(x)) {
				block = append(block, num)
			}
			num++
		} else {
			for range util.StrToInt(string(x)) {
				block = append(block, -1)
			}
		}
	}
	for i, j := 0, len(block)-1; i < j; {
		for i < len(block) && block[i] != -1 {
			i++
		}
		for j >= 0 && block[j] == -1 {
			j--
		}
		if i < len(block) && j >= 0 && i < j {
			block[i], block[j] = block[j], block[i]
		}
	}
	lo.ForEach(block, func(x int, i int) {
		if x > 0 {
			res += i * x
		}
	})
	return res
}

func solution2(s string) (res int) {
	var block []int
	var num int
	for i, x := range s {
		if i%2 == 0 {
			for range util.StrToInt(string(x)) {
				block = append(block, num)
			}
			num++
		} else {
			for range util.StrToInt(string(x)) {
				block = append(block, -1)
			}
		}
	}
	block2 := slices.Clone(block)
	for i := len(block) - 1; i >= 0; {
		// i will contain the end position of the slice of number inside block
		for i >= 0 && block[i] == -1 {
			i--
		}
		// ii will contain the start position of the slice of number inside block
		var ii int
		for ii = i - 1; ii >= 0 && block[ii] == block[i]; ii-- {
		}
		ii++
		if i >= 0 && ii >= 0 {
			n := make([]int, i-ii+1)
			for nn := range n {
				n[nn] = -1
			}
			// j will contain the start position of the slice of -1 inside block2
			j := util.SlicesIndex(block2, n)
			if j >= 0 && j < ii {
				for k, l := j, ii; k < j+len(n); k, l = k+1, l+1 {
					block2[k], block2[l] = block[l], -1
				}
			}
		}
		i = ii - 1
	}
	lo.ForEach(block2, func(x int, i int) {
		if x > 0 {
			res += i * x
		}
	})
	return res
}
