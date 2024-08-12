package main

// go run 2023/day1/puzzle_2.go -file ./2023/day1/input.txt

import (
	"flag"
	"fmt"
	"log/slog"
	"os"
	"strings"
)

const (
	digits        string = "0123456789"
	digitsNotZero string = "123456789"
)

var digitsString = []string{
	"0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
	"*", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
}

func main() {
	filename := flag.String("file", "input.txt", "input file to process")
	flag.Parse()

	data, err := os.ReadFile(*filename)
	if err != nil {
		slog.Error("os.ReadFile failed:", slog.Any("error", err))
		return
	}

	lines := strings.Split(string(data), "\n")
	solution1(lines)
	solution2(lines)
}

func solution1(lines []string) {
	var sum int

	for _, line := range lines {
		first, last := strings.IndexAny(line, digitsNotZero), strings.LastIndexAny(line, digits)
		if first >= 0 && last >= 0 {
			sum += int(([]rune(line)[first]-'0')*10 + ([]rune(line)[last] - '0'))
		}
	}

	fmt.Println("solution 1:", sum)
}

func solution2(lines []string) {
	var sum int

	for _, line := range lines {
		first, last := -1, -1
		firstIdx, lastIdx := len(line), -1

		for digitIdx, digit := range digitsString {
			idx := strings.Index(line, digit)
			if idx >= 0 && idx < firstIdx && digitIdx > 0 {
				firstIdx = idx
				first = digitIdx % 10
			}
			idx = strings.LastIndex(line, digit)
			if idx >= 0 && idx > lastIdx {
				lastIdx = idx
				last = digitIdx % 10
			}
		}

		if first >= 0 && last >= 0 {
			sum += first*10 + last
		}
	}

	fmt.Println("solution 2:", sum)
}
