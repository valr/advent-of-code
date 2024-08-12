package util

import (
	"log"
	"strconv"
	"strings"
)

type Number interface {
	uint8 | uint16 | uint32 | uint64 |
		int8 | int16 | int32 | int64 |
		int | float32 | float64
}

// Split the string into substrings separated by seps and return the slice of trimmed substrings
func StringsSplitAny(s string, seps string) []string {
	return TrimSpaceAll(strings.FieldsFunc(s, func(r rune) bool {
		return strings.ContainsRune(seps, r)
	}))
}

// Trim all strings in the slice of strings and return the slice
func TrimSpaceAll(s []string) []string {
	for i := range s {
		s[i] = strings.TrimSpace(s[i])
	}
	return s
}

// Convert the string to int and return the value
func ToInt(s string) int {
	num, err := strconv.Atoi(s)
	if err != nil {
		log.Panicf("error when converting %v in ToInt: %v", s, err)
	}
	return num
}

// Compute the sum of all values in the map and return the sum
func Sum[K comparable, V Number](m map[K]V) V {
	var sum V
	for _, value := range m {
		sum += value
	}
	return sum
}

// Compute the product of all values in the map and return the product
func Product[K comparable, V Number](m map[K]V) V {
	var product V
	var idx int
	for _, value := range m {
		if idx == 0 {
			product = value
		} else {
			product *= value
		}
		idx++
	}
	return product
}