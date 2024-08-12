package main

// go run 2023/day2/puzzle_2.go -file 2023/day2/input.txt

import (
	"flag"
	"fmt"
	"log/slog"
	"os"
	"strings"

	"advent-of-code/2023/util"
)

type Game struct {
	id  int
	set []map[string]int
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
	solution1and2(lines)
}

func solution1and2(lines []string) {
	var sum1, sum2 int

	for _, line := range lines {
		game := parseLine(line)
		gameOk, setOk := true, make(map[string]int, 3)

		for _, set := range game.set {
			if set["red"] > 12 || set["green"] > 13 || set["blue"] > 14 {
				gameOk = false
			}
			for _, color := range []string{"red", "green", "blue"} {
				setOk[color] = max(setOk[color], set[color])
			}
		}

		if gameOk {
			sum1 += game.id
		}
		sum2 += util.Product(setOk)
	}

	fmt.Println("solution 1:", sum1)
	fmt.Println("solution 2:", sum2)
}

func parseLine(s string) Game {
	gameStr := util.StringsSplitAny(strings.TrimPrefix(s, "Game "), ":;")
	game := Game{util.ToInt(gameStr[0]), make([]map[string]int, 0)}

	for _, setStr := range gameStr[1:] {
		set := make(map[string]int, 3)
		for _, cubeStr := range util.StringsSplitAny(setStr, ",") {
			cubeFld := strings.Fields(cubeStr)
			set[cubeFld[1]] = util.ToInt(cubeFld[0])
		}
		game.set = append(game.set, set)
	}

	return game
}
