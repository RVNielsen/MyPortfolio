from tokenize import Triple
from numpy import character, void
import requests
import re
from random import seed
from random import randint
import time

FILENAME = 'illegallearning.txt'
VOWELS = ['a', 'e', 'i', 'o', 'u']

def thes(oWord: str) -> str:
    url = 'https://www.thesaurus.com/browse/' + oWord
    req = requests.get(url, 'html.parser')
    seed(round(time.time() * 1000))
    randNum = randint(1, 5)
    return(req.text.split('href="/browse/')[randNum].split('"')[0].replace('%20', ' '))


def getNonLetters(str1: str, str1Reg: str) -> str:
    diffStr1 = ''
    for let in str1:
        if let not in str1Reg:
            diffStr1 += let
        else:
            diffStr1 += '`'
    return(diffStr1)


def checkLC(LC: character, n: character, DQE: int) -> bool:
    if LC == '(':
        return(False)
    if LC.isnumeric() and n == '.':
        return(False)
    elif LC == '"' and DQE == 0:
        return(False)
    else:
        return(True)


def main(oLines: str) -> str:
    outputStr = ''
    fCommon = open('commonWords.txt', 'r')
    commonWords = str(fCommon.read()).strip('\n')
    aFlag = False
    anFlag = False
    dQuotesEven = 1
    for a in re.split(' |-', oLines):
        if re.match('[0-9]', a):
            regA = ''
            aNonLet = '`'
            tWord = str(a)
        else:
            regA = re.sub(r'[^a-zA-Z]', '', a)
            aNonLet = getNonLetters(a, regA)
            if regA.lower() not in commonWords:
                tWord = thes(regA)
                if regA.isupper():
                    tWord = tWord.upper()
                elif regA[0].isupper():
                    tWord = tWord.capitalize()
            else:
                if '\'' in a:
                    tWord = a
                    aNonLet = '`'
                else:
                    tWord = regA
        if aFlag == True and tWord[0] in VOWELS:
            outputStr += 'n'
        if anFlag == True and tWord[0] not in VOWELS:
            outputStr = outputStr[:-1]
        if regA.lower() == 'a':
            aFlag = True
        else:
            aFlag = False
        if regA.lower() == 'an':
            anFlag = True
        else:
            anFlag = False
        wordFlag = False
        lastChar = ''
        if bool(aNonLet):
            for n in aNonLet:
                if n == '`':
                    if wordFlag == False:
                        if tWord[-1].isalnum() and checkLC(lastChar, n, dQuotesEven):
                            outputStr += ' '
                        wordFlag = True
                        outputStr += tWord
                else:
                    if n == '"':
                        if dQuotesEven == 1:
                            outputStr += ' '
                        dQuotesEven = (dQuotesEven + 1) % 2
                    if n == '(':
                        outputStr += ' '
                    if n != '\'':
                        outputStr += n
                        lastChar = n
    return(outputStr[3:])


if __name__ == "__main__":
    main()
