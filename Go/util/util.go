package util

import (
	"log"
	"strconv"
	"strings"
)

type Number interface {
	~uint8 | ~uint16 | ~uint32 | ~uint64 |
		~int8 | ~int16 | ~int32 | ~int64 |
		~int | ~float32 | ~float64
}

// Convert the int to string and return the value
func IntToStr(n int) string {
	return strconv.Itoa(n)
}

// Compute the absolute value of a number
func MathAbs[T Number](x T) T {
	if x < 0 {
		return -x
	}
	return x
}

// Return the sum of all numbers
func MathSum[T Number](x ...T) T {
	var sum T
	for i := range x {
		sum += x[i]
	}
	return sum
}

// Return the product of all numbers
func MathProduct[T Number](x ...T) T {
	var product T
	if len(x) > 0 {
		product = x[0]
		for i := 1; i < len(x); i++ {
			product *= x[i]
		}
	}
	return product
}

// Count the occurrences of an element in a slice
func SlicesCount[S ~[]T, T comparable](s S, v T) int {
	count := 0
	for i := range s {
		if s[i] == v {
			count++
		}
	}
	return count
}

// Create a slice of size count with all elements initialized with value of given element v
func SlicesCreate[T any](count int, v T) []T {
	if count < 0 {
		log.Panicf("error when creating slice in SlicesCreate: %v", count)
	}
	slice := make([]T, count)
	if count > 0 {
		slice[0] = v
		for i := 1; i < count; i *= 2 {
			copy(slice[i:], slice[:i])
		}
	}
	return slice
}

// Return a slice of all elements in the slice s that satisfy the predicate function f
func SlicesFilter[S ~[]T, T any](s S, f func(v T) bool) S {
	filtered := make(S, len(s))
	count := 0
	for i := range s {
		if f(s[i]) {
			filtered[count] = s[i]
			count++
		}
	}
	return filtered[:count]
}

// Return a slice of all elements in the slice s that satisfy the predicate function f
func SlicesFilter2[S ~[]T, T any](s S, f func(v T, idx int) bool) S {
	filtered := make(S, len(s))
	count := 0
	for i := range s {
		if f(s[i], i) {
			filtered[count] = s[i]
			count++
		}
	}
	return filtered[:count]
}

// Flatten a nested slice into a single slice
func SlicesFlatten[T any](slices [][]T) []T {
	totalLen := 0
	for i := range slices {
		totalLen += len(slices[i])
	}
	flattened := make([]T, 0, totalLen)
	for i := range slices {
		flattened = append(flattened, slices[i]...)
	}
	return flattened
}

// Return the index of the first occurrence of sub in s, or -1 if not present
func SlicesIndex[S ~[]T, T comparable](s S, sub S) int {
next:
	for i := range len(s) - len(sub) + 1 {
		for j := range sub {
			if s[i+j] != sub[j] {
				continue next
			}
		}
		return i
	}
	return -1
}

// Return a slice of all elements that are present in all the given slices
func SlicesIntersect[T comparable](slices ...[]T) []T {
	result := make([]T, 0)
	if len(slices) == 0 {
		return result
	}
	freq := make(map[T]int)
	for i := range slices[0] {
		freq[slices[0][i]]++
	}
	for j := 1; j < len(slices); j++ {
		tempFreq := make(map[T]int)
		for i := range slices[j] {
			tempFreq[slices[j][i]]++
		}
		for elem, count1 := range freq {
			if count2, ok := tempFreq[elem]; ok {
				if count2 < count1 {
					freq[elem] = count2
				}
			} else {
				delete(freq, elem)
			}
		}
	}
	for elem, count := range freq {
		for range count {
			result = append(result, elem)
		}
	}
	return result
}

// Return a slice by applying function f to each element in the slice s
func SlicesMap[S1 ~[]T1, S2 []T2, T1, T2 any](s S1, f func(v T1) T2) S2 {
	mapped := make(S2, len(s))
	for i := range s {
		mapped[i] = f(s[i])
	}
	return mapped
}

// Return a slice by applying function f to each element in the slice s
func SlicesMap2[S1 ~[]T1, S2 []T2, T1, T2 any](s S1, f func(v T1, idx int) T2) S2 {
	mapped := make(S2, len(s))
	for i := range s {
		mapped[i] = f(s[i], i)
	}
	return mapped
}

// Return the result of applying a binary function f cumulatively to the elements of the slice s
func SlicesReduce[S ~[]T1, T1, T2 any](s S, init T2, f func(acc T2, v T1) T2) T2 {
	acc := init
	for i := range s {
		acc = f(acc, s[i])
	}
	return acc
}

// Return the result of applying a binary function f cumulatively to the elements of the slice s
func SlicesReduce2[S ~[]T1, T1, T2 any](s S, init T2, f func(acc T2, v T1, idx int) T2) T2 {
	acc := init
	for i := range s {
		acc = f(acc, s[i], i)
	}
	return acc
}

// Return the reversed string
func StrReverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// Return the rotated string matrix
func StrRotateMatrix(matrix []string) []string {
	var rotated []string
	for i := range len(matrix[0]) {
		var row []rune
		for j := range matrix {
			row = append(row, []rune(matrix[j])[i])
		}
		rotated = append(rotated, string(row))
	}
	return rotated
}

// Return the string matrix read diagonally
func StrDiagonalMatrix(matrix []string) []string {
	var diagonals []string
	rows, cols := len(matrix), len(matrix[0])
	for k := range rows + cols - 1 {
		var diag []rune
		for l := max(0, k-cols+1); l < min(rows, k+1); l++ {
			diag = append([]rune{[]rune(matrix[l])[k-l]}, diag...)
		}
		diagonals = append(diagonals, string(diag))
	}
	return diagonals
}

// Return the string matrix read counter diagonally
func StrCounterDiagonalMatrix(matrix []string) []string {
	var counterDiagonals []string
	for i := range matrix {
		counterDiagonals = append(counterDiagonals, StrReverse(matrix[i]))
	}
	return StrDiagonalMatrix(counterDiagonals)
}

// Split the string into substrings separated by separators and return the slice of substrings
func StrSplitAny(s string, separators string) []string {
	return strings.FieldsFunc(s, func(r rune) bool {
		return strings.ContainsRune(separators, r)
	})
}

// Convert the string to int and return the value
func StrToInt(s string) int {
	num, err := strconv.Atoi(s)
	if err != nil {
		log.Panicf("error when converting %v in StrToInt: %v", s, err)
	}
	return num
}

// Return a slice of the given values
func Wrap(x ...any) []any {
	return x
}
