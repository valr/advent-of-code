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
	for endBlock := len(block) - 1; endBlock >= 0; {
		// endBlock will contain the end position of the slice of number inside block
		for endBlock >= 0 && block[endBlock] == -1 {
			endBlock--
		}
		// startBlock will contain the start position of the slice of number inside block
		var startBlock int
		for startBlock = endBlock - 1; startBlock >= 0 && block[startBlock] == block[endBlock]; startBlock-- {
		}
		startBlock++
		if startBlock >= 0 && endBlock >= 0 {
			sz := endBlock - startBlock + 1
			// startBlock2 will contain the start position of the slice of -1 inside block2
			startBlock2 := util.SlicesIndex(block2, util.SlicesCreate(sz, -1))
			if startBlock2 >= 0 && startBlock2 < startBlock {
				for i, j := startBlock2, startBlock; i < startBlock2+sz; i, j = i+1, j+1 {
					block2[i], block2[j] = block[j], block[i]
				}
			}
		}
		endBlock = startBlock - 1
	}
	lo.ForEach(block2, func(x int, i int) {
		if x > 0 {
			res += i * x
		}
	})
	return res
}
