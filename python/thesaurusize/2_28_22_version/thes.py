from numpy import character
import requests
import re
from random import seed
from random import randint
import time

VOWELS = ['a', 'e', 'i', 'o', 'u']

# ---return a random synonym from thesaurus.com for word--- 
def thes(word: str) -> str:
    url = 'https://www.thesaurus.com/browse/' + word # webaddress for thesuarus.com page for word
    req = requests.get(url, 'html.parser') # code from the thesaurus.com page for word
    seed(round(time.time() * 1000))
    randSynNum = randint(1, 5)
    return(req.text.split('href="/browse/')[randSynNum].split('"')[0].replace('%20', ' '))

# ---return the characters attached to word (quotes, parentheses, etc.)---
def getNonLetters(word: str, wordLets: str) -> str:
    chars = '' # characters attached to word
    for let in word:
        if let not in wordLets:
            chars += let
        else:
            chars += '`'
    return(chars)

# ---return True or False if a space should be added before the current word---
def shouldAddSpace(prevChar: character, c: character, dqEven: int) -> bool:
    if prevChar == '(':
        return(False)
    elif prevChar.isnumeric() and c == '.':
        return(False)
    elif prevChar == '"' and dqEven == 0:
        return(False)
    else:
        return(True)

# ---take discord message as input and return the message with synonyms in place of uncommon words---
def thesMain(message: str) -> str:
    print('in other', flush=True)
    thesMessage = '' # Thesaurusized message to be returned 
    aFlag = False # was previous character 'a'
    anFlag = False # was previous character 'an'
    dqEven = 1 # is there an even number of double quotes
    message = message.replace('\n', ' ')
    comFile = open('commonWords.txt', 'r')
    comWords = str(comFile.read())
    for word in re.split(' |-', message):
        chars = '`' # characters attached to word ('`' means none)
        addedToTM = False # has word been added to thesMessage
        prevChar = '' # previous character
        wordLets = '' # letters in the word
        wordSyn = str(word) # synonymn of the word
        if re.match(r'[^0-9]', word):
            wordLets = re.sub(r'[^a-zA-Z\']', '', word)
            chars = getNonLetters(word, wordLets)
            if wordLets.lower() in comWords:
                wordSyn = wordLets
            else:
                wordSyn = thes(wordLets)
                if wordLets.isupper():
                    wordSyn = wordSyn.upper()
                elif wordLets[0].isupper():
                    wordSyn = wordSyn.capitalize()
            if aFlag == True and wordSyn[0] in VOWELS:
                thesMessage += 'n'
            elif anFlag == True and wordSyn[0] not in VOWELS:
                thesMessage = thesMessage[:-1]
            if wordLets.lower() == 'a':
                aFlag = True
            else:
                aFlag = False
            if wordLets.lower() == 'an':
                anFlag = True
            else:
                anFlag = False
        for c in chars:
            if c == '`':
                if addedToTM == False:
                    if wordSyn[-1].isalnum() and shouldAddSpace(prevChar, c, dqEven):
                        thesMessage += ' '
                    addedToTM = True
                    thesMessage += wordSyn
            else:
                if c == '"':
                    if dqEven == 1:
                        thesMessage += ' '
                    dqEven = (dqEven + 1) % 2
                elif c == '(':
                    thesMessage += ' ('
                elif c != '\'':
                    thesMessage += c
                    prevChar = c
    return(thesMessage[3:])
