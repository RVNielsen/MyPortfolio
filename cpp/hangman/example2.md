# Example 2: Both players try and break the game
## How the program handles special cases
```txt
Player 1, write a word with at least 3 letters:
345
The word needs to be at least one letter long and can only consist of lower case letters, try again.
```
the word consisted of no letters
```txt
Player 1, write a word with at least 3 letters:
hi
The word needs to be at least one letter long and can only consist of lower case letters, try again.
```
the word is only two letters
```txt
Player 1, write a word with at least 3 letters:
hi345
The word needs to be at least one letter long and can only consist of lower case letters, try again.
```
numbers were removed only leaving two letters
```txt
Player 1, write a word with at least 3 letters:
chiCken89 (and) waf_flEs
```
numbers and special characters were removed (besides spaces) leaving a valid word - "chicken and waffles"

uppercase letters were also changed to lowercase 

(there are normally about 50 blank lines here when running in the command line so that player 2 does not see the word, but they were removed for readability)
```txt
_ _ _ _ _ _ _   _ _ _   _ _ _ _ _ _ _
```
the number of letters is represented by underscores and spaces are automatically filled in
```txt
Player 2, guess a letter:
2
Sorry, only lowercase letters please.
```
the guess was not a letter
```txt
Player 2, guess a letter:
G




---Incorrect Letters---     ---Correct Letters---
g

You have 4 strikes left.
-----
|   |
|
|
|
|


_ _ _ _ _ _ _   _ _ _   _ _ _ _ _ _ _
```
the uppercase letter was turned into a lowercase one when searching through the word
```txt
Player 2, guess a letter:
jk




---Incorrect Letters---     ---Correct Letters---
g, j

You have 3 strikes left.
-----
|   |
|   o
|
|
|


_ _ _ _ _ _ _   _ _ _   _ _ _ _ _ _ _
```
only the first letter inputted is considered
```txt
Player 2, guess a letter:
i w




---Incorrect Letters---     ---Correct Letters---
g, j                        i

You have 3 strikes left.
-----
|   |
|   o
|
|
|


_ _ i _ _ _ _   _ _ _   _ _ _ _ _ _ _

Player 2, guess a letter:
c




---Incorrect Letters---     ---Correct Letters---
g, j                        i, c

You have 3 strikes left.

-----
|   |
|   o
|
|
|


c _ i c _ _ _   _ _ _   _ _ _ _ _ _ _

Player 2, guess a letter:
h




---Incorrect Letters---     ---Correct Letters---
g, j                        i, c, h

You have 3 strikes left.
-----
|   |
|   o
|
|
|


c h i c _ _ _   _ _ _   _ _ _ _ _ _ _

Player 2, guess a letter:
a




---Incorrect Letters---     ---Correct Letters---
g, j                        i, c, h, a

You have 3 strikes left.
-----
|   |
|   o
|
|
|


c h i c _ _ _   a _ _   _ a _ _ _ _ _
```
even when spaces are added
```txt
Player 2, guess a letter:
i
That letter has already been guessed, try again.
Player 2, guess a letter:
()
Sorry, only lowercase letters please.
Player 2, guess a letter:
l




---Incorrect Letters---     ---Correct Letters---
g, j                        i, c, h, a, l

You have 3 strikes left.
-----
|   |
|   o
|
|
|


c h i c _ _ _   a _ _   _ a _ _ l _ _

Player 2, guess a letter:
h
That letter has already been guessed, try again.
Player 2, guess a letter:
b




---Incorrect Letters---     ---Correct Letters---
g, j, b                     i, c, h, a, l

You have 2 strikes left.
-----
|   |
|   o
|   |
|
|


c h i c _ _ _   a _ _   _ a _ _ l _ _

Player 2, guess a letter:
y




---Incorrect Letters---     ---Correct Letters---
g, j, b, y                  i, c, h, a, l

You have 1 strike left!
-----
|   |
|   o
|  /|\
|
|


c h i c _ _ _   a _ _   _ a _ _ l _ _

Player 2, guess a letter:
qwerty




---Incorrect Letters---     ---Correct Letters---
g, j, b, y, q               i, c, h, a, l

You have 0 strikes left.
-----
|   |
|   o
|  /|\
|  / \
|

You lose, the word was chicken and waffles.
```
the player is asked for a letter until they pick one that has not already been guessed
