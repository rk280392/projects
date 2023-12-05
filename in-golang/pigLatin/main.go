package main

// Create pig latin equivalent from words.
import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// Take a word as input and create pig latin equivalent.

	vowels := "aeiou"

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Please enter the word: ")
	word, _ := reader.ReadString('\n')
	word = strings.TrimSpace(word)

	if strings.ContainsRune(vowels, rune(word[0])) {
		fmt.Println(word + "way")
	} else {
		fmt.Println(word[1:] + string(word[0]) + "ay")
	}
}
