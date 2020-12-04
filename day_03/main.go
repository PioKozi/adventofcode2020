package main

import (
	"bufio"
	"fmt"
	"os"
)

func traverse(y, x int) int {
	file, _ := os.Open("./input")
	defer file.Close()
	source := bufio.NewScanner(file)
	count := 0
	pos := 0
	for source.Scan() {
		line := source.Text()
		if len(line) == 0 { // passed the end of the file (possible reason: skipping lines)
			return count
		}
		// fmt.Printf("%s, %c\n", line, line[pos])
		if line[pos] == '#' {
			count += 1
		}
		for i := 1; i < y; i++ { // if we need to skip lines (eg, down 2)
			source.Scan()
		}
		pos = (pos + x) % len(line)
	}
	return count
}

func main() {
	fmt.Printf("y=1, x=1, count=%d\n", traverse(1, 1))
	fmt.Printf("y=1, x=3, count=%d\n", traverse(1, 3))
	fmt.Printf("y=1, x=5, count=%d\n", traverse(1, 5))
	fmt.Printf("y=1, x=7, count=%d\n", traverse(1, 7))
	fmt.Printf("y=2, x=1, count=%d\n", traverse(2, 1))
}
