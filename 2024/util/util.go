package util

import (
	"log"
	"maps"
	"slices"
	"strconv"
	"strings"
)

type Number interface {
	uint8 | uint16 | uint32 | uint64 |
		int8 | int16 | int32 | int64 |
		int | float32 | float64
}

// Compute the absolute value of a number
func MathAbs[V Number](v V) V {
	if v < 0 {
		return -v
	}
	return v
}

// Count the occurences of an element in a slice
func SlicesCount[S ~[]E, E comparable](s S, e E) (count int) {
	for _, ss := range s {
		if e == ss {
			count++
		}
	}
	return count
}

// Return the reversed string
func StrReverse(s string) string {
	ss := []rune(s)
	for i, j := 0, len(ss)-1; i < j; i, j = i+1, j-1 {
		ss[i], ss[j] = ss[j], ss[i]
	}
	return string(ss)
}

// Return the rotated string matrix
func StrRotateMatrix(s []string) []string {
	var m []string
	for i := range len(s[0]) {
		var r []rune
		for j := range len(s) {
			r = append(r, []rune(s[j])[i])
		}
		m = append(m, string(r))
	}
	return m
}

// Return the string matrix read diagonally
func StrDiagonalMatrix(s []string) []string {
	var m []string
	i, j := len(s), len(s[0])
	for k := range i + j - 1 {
		var r []rune
		for l := max(0, k-j+1); l < min(i, k+1); l++ {
			r = append([]rune{[]rune(s[l])[k-l]}, r...)
		}
		m = append(m, string(r))
	}
	return m
}

// Return the string matrix read counter diagonally
func StrCounterDiagonalMatrix(s []string) []string {
	var m []string
	for i := range s {
		m = append(m, StrReverse(s[i]))
	}
	return StrDiagonalMatrix(m)
}

// Split the string into substrings separated by seps and return the slice of substrings
func StrSplitAny(s string, seps string) []string {
	return strings.FieldsFunc(s, func(r rune) bool {
		return strings.ContainsRune(seps, r)
	})
}

// Trim all strings in the slice in-place and return the slice of strings
func StrTrimSpaceAll(s []string) []string {
	for i := range s {
		s[i] = strings.TrimSpace(s[i])
	}
	return s
}

// Convert the string to int and return the value
func StrToInt(s string) int {
	num, err := strconv.Atoi(s)
	if err != nil {
		log.Panicf("error when converting %v in StrToInt: %v", s, err)
	}
	return num
}

// Compute the sum of all values in the map and return the sum
func MapSum[K comparable, V Number](m map[K]V) (sum V) {
	for _, value := range m {
		sum += value
	}
	return sum
}

// Compute the product of all values in the map and return the product
func MapProduct[K comparable, V Number](m map[K]V) (product V) {
	v := slices.Collect(maps.Values(m))
	if len(v) > 0 {
		product = v[0]
		for _, value := range v[1:] {
			product *= value
		}
	}
	return product
}
