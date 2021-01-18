# Ultimate Werewolf: Role Randomizer
I made this program to play the social deduction game "Ultimate Werewolf" online with friends over quarantine. The program asks the user for the number of wolves and villagers guaranteed to be in the game. It then asks for the names of all the players and recursively divvies out a role to each player and displays the outcome in the form of a table.

## Installation
```python
python3 werewolf.py
```

## Usage (example)
```
How many wolves (1 - 3)? One wolf for every 4 players is a good rule-of-thumb: a
Invalid, try again.
How many wolves (1 - 3)? One wolf for every 4 players is a good rule-of-thumb: 7
Out of range, try again.
How many wolves (1 - 3)? One wolf for every 4 players is a good rule-of-thumb: 2
Current roles:
wolf
wolf
detective
bodyguard
How many villagers? (random roles will be added for the rest after this): 100
Out of range, try again.
How many villagers? (random roles will be added for the rest after this): 3
Current roles:
wolf
wolf
detective
bodyguard
villager
villager
villager
Enter the name of a player. Write "done" when all players have been added. For list of players already added, write "list":

Player 0: Jenna
Jenna added to players
Player 1: Bob
Bob added to players
Player 2: Bill
Bill added to players
Player 3: Joe
Joe added to players
Player 4: John
John added to players
Player 5: Abby
Abby added to players
Player 6: Michael
Michael added to players
Player 7: George
George added to players
Player 8: Brenda
Brenda added to players
Player 9: Ellie
Ellie added to players
Player 10: Peter
Peter added to players
Player 11: list
Current players:
Jenna
Bob
Bill
Joe
John
Abby
Michael
George
Brenda
Ellie
Peter
Player 11: done


Name       |  Role
----------------------
Michael    :  wolf

Bill       :  wolf

Joe        :  detective

Jenna      :  bodyguard

Abby       :  villager

George     :  villager

Peter      :  villager

John       :  grandma with a gun

Ellie      :  hunter

Brenda     :  witness

Bob        :  chief of police
```
