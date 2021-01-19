# Example 1: Both players play the game well
```
Player 1, write a word with at least 3 letters:
strawberry
```
When run in the command line, many blank lines are added here so that player 2 cannot see the word. The lines were cut in this example for readability
```
-----
|   |
|
|
|
|


_ _ _ _ _ _ _ _ _ _

Player 2, guess a letter:
r




---Incorrect Letters---     ---Correct Letters---
                           r

You have 4 strikes left.
-----
|   |
|
|
|
|


_ _ r _ _ _ _ r r _

Player 2, guess a letter:
e




---Incorrect Letters---     ---Correct Letters---
                           r, e

You have 4 strikes left.
-----
|   |
|
|
|
|


_ _ r _ _ _ e r r _

Player 2, guess a letter:
i




---Incorrect Letters---     ---Correct Letters---
 i                         r, e

You have 3 strikes left.
-----
|   |
|   o
|
|
|


_ _ r _ _ _ e r r _

Player 2, guess a letter:
w




---Incorrect Letters---     ---Correct Letters---
 i                         r, e, w

You have 3 strikes left.
-----
|   |
|   o
|
|
|


_ _ r _ w _ e r r _

Player 2, guess a letter:
n




---Incorrect Letters---     ---Correct Letters---
 i, n                      r, e, w

You have 2 strikes left.
-----
|   |
|   o
|   |
|
|


_ _ r _ w _ e r r _

Player 2, guess a letter:
l




---Incorrect Letters---     ---Correct Letters---
 i, n, l                   r, e, w

You have 1 strike left!
-----
|   |
|   o
|  /|\
|
|


_ _ r _ w _ e r r _

Player 2, guess a letter:
s




---Incorrect Letters---     ---Correct Letters---
 i, n, l                   r, e, w, s

You have 1 strike left!
-----
|   |
|   o
|  /|\
|
|


s _ r _ w _ e r r _

Player 2, guess a letter:
a




---Incorrect Letters---     ---Correct Letters---
 i, n, l                   r, e, w, s, a

You have 1 strike left!
-----
|   |
|   o
|  /|\
|
|


s _ r a w _ e r r _

Player 2, guess a letter:
t




---Incorrect Letters---     ---Correct Letters---
 i, n, l                   r, e, w, s, a, t

You have 1 strike left!
-----
|   |
|   o
|  /|\
|
|


s t r a w _ e r r _

Player 2, guess a letter:
b




---Incorrect Letters---     ---Correct Letters---
 i, n, l                   r, e, w, s, a, t, b

You have 1 strike left!
-----
|   |
|   o
|  /|\
|
|


s t r a w b e r r _

Player 2, guess a letter:
y




---Incorrect Letters---     ---Correct Letters---
 i, n, l                   r, e, w, s, a, t, b, y

You have 1 strike left!
-----
|   |
|   o
|  /|\
|
|
Congrats, you found the word!
The word was strawberry!
```
