import requests
import re
from random import seed
from random import randint
import time

VOWELS = ['a', 'e', 'i', 'o', 'u']
TOLERANCE = 10

# ---return a random synonym from thesaurus.com for word--- 
def thes(word: str) -> str:
    url = 'https://www.thesaurus.com/browse/' + word # webaddress for thesuarus.com page for word
    req = requests.get(url, 'html.parser') # code from the thesaurus.com page for word
    seed(round(time.time() * 1000))
    allSyns = req.text.split('href="/browse/')
    randSynNum = randint(1, min(len(allSyns) - 1, TOLERANCE))
    wordSyn = allSyns[randSynNum].split('"')[0] # synonym for word
    for a in wordSyn.split('%')[1:]: 
        hexCode = a[0:2] # hex value of a non-alphanumreric is two characters following '%'
        wordSyn = wordSyn.replace(str('%' + hexCode), bytes.fromhex(hexCode).decode('utf-8'))
    return(wordSyn)

# ---return the discord message with synonyms in place of uncommon words---
def thesMain(message: str) -> str:
    thesMessage = '' # Thesaurusized message to be returned 
    aFlag = False # was previous character 'a'
    anFlag = False # was previous character 'an'
    dqEven = 1 # is there an even number of double quotes
    message = re.sub(' +', ' ', message[3:])
    comFile = open('commonWords.txt', 'r')
    comWords = str(comFile.read())
    for word in re.split(' |-|\n', message):
        if bool(word):
            chars = '`' # non-alphanumeric characters attached to word ('`' means none)
            wordLets = '' # letters in the word
            wordSyn = str(word) # synonymn of the word
            if re.match(r'[^0-9]', word):
                wordLets = re.sub(r'[^a-zA-Z\'\.]', '', word)
                if wordLets.lower() in comWords:
                    chars = re.sub(r'[a-zA-Z\'\.]', '`', word)
                    wordSyn = wordLets
                else:
                    wordLets = re.sub(r'[\'\.]', '', wordLets)
                    chars = re.sub(r'[a-zA-Z]', '`', word)
                    wordSyn = thes(wordLets)
                    if wordLets.isupper():
                        wordSyn = wordSyn.upper()
                    elif wordLets[0].isupper():
                        wordSyn = wordSyn.capitalize()
                if aFlag == True and wordSyn[0] in VOWELS:
                    thesMessage += 'n'
                elif anFlag == True and wordSyn[0] not in VOWELS:
                    thesMessage = thesMessage[:-1]
                aFlag = True if wordLets.lower() == 'a' else False
                anFlag = True if wordLets.lower() == 'an' else False
            firstChar = True
            addedToTM = False
            for c in chars:
                if firstChar == True:
                    thesMessage += ' ' 
                if c == '`':
                    if addedToTM == False:
                        addedToTM = True
                        thesMessage += wordSyn
                elif c == '"':
                    dqEven = (dqEven + 1) % 2
                else:
                    thesMessage += c
                if firstChar == True:
                    firstChar = False 
    return(thesMessage)
