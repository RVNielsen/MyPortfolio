# (Fictional) Murder Mystery at S&T
This is a school project and probably does not make much sense without context, but I still wanted to include it since it's a good example of my experience with prolog. In this project I was given information in the form of multiple paragraphs and was tasked with creating a program to determine which professor murdered my professor (fictional). For someone to be a suspect, they had to have had access to one of the two possible murder weapons, a key to the computer science building, access to the crime scene, and a motive. Using the information given, I was able to transfer that into prolog facts and when run, the program finds a single suspect.

## Installation
```pl
prolog murder_mystery.pl
```

## Usage
```pl
?- murderer(X, Y, Z).
X = price,
Y = patties,
Z = poor ;
X = price,
Y = patties,
Z = poor ;
false.
```
