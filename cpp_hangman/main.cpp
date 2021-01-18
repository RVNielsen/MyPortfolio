#include <iostream>
#include "main.h"
using namespace std;

bool checkAnswer(string ansStr, string letStr, int ansLen, int letLen)
{
      bool digitFound;
      int ansIndex;
      for(ansIndex = 0; ansIndex < ansLen; ansIndex++)
      {
            digitFound = false;
            for(int t = 0; t < letLen; t = t + 3)
            {
                  if(ansStr[ansIndex] == letStr[t])
                  {
                        digitFound = true;
                  }
            }
            if(digitFound == false)
            {
                  break;
            }
      }

      // if after going through the loop, index = length, then each letter was correct
      if(ansIndex == ansLen)
      {
            return 1;
      }
      return 0;
}

int main()
{      
      // player 1 picks the word
      Player1 p1;
      string answer;
      p1.setWord();
      answer = string(p1.getWord());

      // player 2 guesses letters
      Player2 p2;

      // set letter to the space character
      p2.setSpace();

      // determines number of spaces between incorrect and correct letter display
      int spaceNum;

      int found = 0;
      bool foundBool;
      do
      {
            foundBool = false; 
            for(int g = 0; g < p1.getLen(); g++)
            {
                  if(p2.getLetter() == p1.getWord()[g])
                  {
                        p1.updateWord(p1.getWord(), p1.getLen(), g);
                        found++;
                        foundBool = true;
                  }
            }      
      }while(foundBool == true);

      if(found != 0)
      {
            // add letter to correct letter list
            p2.setCorLetters();
      }
      else
      {
            // add letter to incorrect letter list and add a strike
            p2.setIncorLetters();
            p2.incStrikes();
      }

      while(1)
      {
            // if too many incorrect strikes have been made, reveal the answer and end
            if(!p2.keepPlaying(answer))
            {
                  break;
            }

            cout << endl << endl;

            // output the word with blanks and correctly guessed letters
            bool needSpace = true;
            for(int u = 0; u < p1.getLen(); u++)
            {
                  for(int i = 0; i < p2.getCorLettersLen(); i = i + 3)
                  {
                        if(answer[u] == p2.getCorLetters()[i])
                        {
                              cout << p2.getCorLetters()[i] << " ";
                              needSpace = false;
                              break;
                        }
                  }
                  if(needSpace == true)
                  {
                        cout << "_ "; 
                  }
                  needSpace = true;
            }

            cout << endl << endl;

            // get letter from player 2
            p2.setLetter();

            // search the word for the letter and update the word if found so that that letter is not searched for later
            found = 0;
            // bool foundBool;
            do
            {
                  foundBool = false; 
                  for(int g = 0; g < p1.getLen(); g++)
                  {
                        if(p2.getLetter() == p1.getWord()[g])
                        {
                              p1.updateWord(p1.getWord(), p1.getLen(), g);
                              found++;
                              foundBool = true;
                        }
                  }      
            }while(foundBool == true);

            if(found != 0)
            {
                  // add letter to correct letter list
                  p2.setCorLetters();
            }
            else
            {
                  // add letter to incorrect letter list and add a strike
                  p2.setIncorLetters();
                  p2.incStrikes();
            }

            // output the guessed letters
            cout << "\n\n\n\n---Incorrect Letters---     ---Correct Letters---\n";

            spaceNum = 0;

            for(int g = 0; g < p2.getIncorLettersLen(); g++)
            {
                  if(int(p2.getIncorLetters()[g]) == 32 && int(p2.getIncorLetters()[g + 1]) == 44)
                  {
                        g++;
                  }
                  else
                  {
                        cout << p2.getIncorLetters()[g];
                        spaceNum++;
                  }
            }

            for(int i = 0; i < 27 - spaceNum; i++)
            {
                  cout << " ";
            }

            for(int g = 0; g < p2.getCorLettersLen(); g++)
            {
                  if(int(p2.getCorLetters()[g]) == 32 && int(p2.getCorLetters()[g + 1]) == 44)
                  {
                        g++;
                  }
                  else
                  {
                        cout << p2.getCorLetters()[g];
                  }                 
            }
            cout << "\n\nYou have " << p2.getRemainingStrikes() << " strikes left!\n";
      }

      return 0;
}
