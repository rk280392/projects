package main

//Generate funny names by randomly combining names from 2 separate lists.

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
)

func input(prompt string) string {
	// input function to take input

	fmt.Println(prompt)
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	return strings.TrimSpace(text)
}

func main() {
	//Choose names at random from 2 tuples of names and print to screen.

	fmt.Println("Welcome to Silly name generator program")
	firstNameList := []string{"Baby Oil", "Bad News", "Big Burps", "Bill 'Beenie-Weenie", "Bob 'Stinkbug", "Bowel Noises", "Boxelder", "Bud Lite", "Butterbean", "Buttermilk", "Buttocks", "Chad", "Chesterfield", "Chewy", "Chigger", "Cinnabuns", "Cleet", "Cornbread", "Crab Meat", "Crapps", "Dark Skies", "Dennis Clawhammer", "Dicman", "Elphonso"}
	lastNameList := []string{"Appleyard", "Bigmeat", "Bloominshine", "Boogerbottom", "Breedslovetrout", "Butterbaugh", "Clovenhoof", "Clutterbuck", "Cocktoasten"}

	for {
		firstName := firstNameList[rand.Intn(len(firstNameList))]
		lastName := lastNameList[rand.Intn(len(lastNameList))]
		fmt.Printf("%s %s \n\n", firstName, lastName)

		tryAgain := input("Didn't like the name? Try again (Press 'Enter' else 'n' to quit): ")
		tryAgain = strings.ToLower(tryAgain)
		if tryAgain == "n" {
			break
		}

	}
}
