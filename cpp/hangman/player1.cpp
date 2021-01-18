#include <iostream>
#include <string>
#include "main.h"
using namespace std;

void Player1::setWord()
{
      // a vector is used to get the word from the user in order to remove 
            // spaces if necessary 
      char c;
      string line;
      do
      {
            // clear the word in case mutliple attempts are needed and get a word from user
            cout << "Player 1, write a word with at least 3 letters: \n";   
            getline(cin, line);

            setLen(line.length());
            for(int b = 0; b < line.length(); b++)
            {
                  arrayWord[b] = line[b];
            }
            lowercaseWord();  
      // try again if word is too short
      } while (wordLen < 3);

      setAnswer();

      cout << string(50, '\n');
}


void Player1::setLen(int newLen)
{
      wordLen = newLen;
}

void Player1::setAnswer()
{
      for(int n = 0; n < wordLen; n++)
      {
            answer[n] = arrayWord[n];
      }
      cout << "answer is: " << answer << endl;
}

char * Player1::updateWord(char currentWord[], int currentLen, int index)
{
      for(int i = index; i < currentLen; i++)
      {
            currentWord[i] = currentWord[i + 1];
      }
      currentWord[currentLen - 1] = 0;
      setLen(currentLen);

      for(int y = 0; y < getLen(); y++)
      {
            arrayWord[y] = currentWord[y];
      }
      return getWord();
}

void Player1::lowercaseWord()
{
      // check each letter in the word
      for(int u = 0; u < wordLen; u++)
      {
            asciiLetter = int(arrayWord[u]);
            if(asciiLetter < 97 || asciiLetter > 122)
            {
                  // if it's capital, change to lowercase
                  if(asciiLetter > 64 && asciiLetter < 91)
                  {
                        asciiLetter += 32;
                        arrayWord[u] = asciiLetter;
                  }
                  else if(asciiLetter != 32)
                  {
                        // if it's not a letter or space, remove it
                        for(int q = u; q < wordLen; q++)
                        {
                              arrayWord[q] = arrayWord[q + 1];
                        }
                        arrayWord[wordLen - 1] = 0;
                        setLen(wordLen - 1);
                        u--;
                  }
            }
      }
      if(wordLen < 3)
      {
            cout << "The word needs to be at least one letter long and can"
                  << " only consist of lower case letters, try again.\n";
      }
}
