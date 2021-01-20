# Hangman
I wrote this program to get more comfortable with classes and using multiple files. This program simulates the word-guessing game hangman and is played by two players. The program gets a word from player 1 and letter guesses from player 2. There are checks in place throughout the program to prevent as many issues as possible such as not allowing special characters from either player, setting a minimum number of letters for the word, and dealing with spaces in the word as multiple words are allowed to be inputted by player 1 for more variety in gameplay.

## Installation
```bash
bash hangman.sh
```

## Table of Contents
example1.md - Both players play the game well

example2.md - Both players try to break the game

hangman.sh - bash script for running all the cpp files together

main.cpp - main and checkAnswer functions

main.h - function prototype for checkAnswer

player1.cpp - Player1 class function declarations

player1.h - Player1 class, variables, and public function prototypes

player2.cpp - Player2 class function declarations

player2.h - Player2 class, variables, and public function prototypes

## Usage
Both example files show how the game is played in the command line. After running the bash script, players can just follow the instuctions that are given in order to play the game.
