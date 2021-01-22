# Thesaurusize
I created this program to learn how to gather information from websites and to have a funny grammar changer for text files. The program has two modes. It can find synonyms for individual words or parse through a text file and replace as many words as it can with a random synonym from "thesaurus.com". In word mode, the program takes the word and searches for a thesaurus.com page for that word. It then simply displays that word to the user and asks for another word. In file mode, the program asks for a file name and the number of times to "thesaurusize". It will go through each word in the file greater than 3 letters and try and replace it with a word from the thesaurus. After going through the whole file, it will write the results to a new text file. If the user asked to loop multiple times, it will use this new file and do the same thing however many times getting further off in meaning from the original file each time.

## Installation
```
python3 thesaurusize.py
```
## Table of Contents
thesaurusize.py - uses thesaurus.com to replace words

paragraph.txt - example of original text file

new_paragraph.txt - example of thesaurisized text file
