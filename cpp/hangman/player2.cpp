#include <iostream>
#include <string>
#include "main.h"
using namespace std;

bool Player2::keepPlaying(string p1Answer)
{
      man();
      if(strikes == maxStrikes)
      {
            cout << "You lose, the word was " << p1Answer << endl;
            return false;
      }
      else if(checkAnswer(p1Answer, corLetters, p1Answer.length(), corLetters.length()))
      {
            cout << "Congrats, you found the word!\nThe word was " << p1Answer << "!" << endl;
            return false;
      }
      return true;
}

void Player2::setLetter()
{
      // used to getline from user and account for spaces
      string line;
      do
      {
            // clear the word in case mutliple attempts are needed and get a word from user
            cout << "Player 2, guess a letter: \n";
            getline(cin, line);
            letter = line[0];
      // try again if word is too short
      }while(!lowercase() || haveGuessed());
}

void Player2::setSpace()
{
      letter = ' ';
}

void Player2::setCorLetters()
{
      if(getCorLettersLen() == 0)
      {
            corLetters = letter;
      }
      else
      {
            corLetters = corLetters + ", " + letter;
      }
}

void Player2::setIncorLetters()
{
      if(getIncorLettersLen() == 0)
      {
            incorLetters = letter;
      }
      else
      {
            incorLetters = incorLetters + ", " + letter;
      }
}

bool Player2::lowercase()
{
      asciiLetter = int(letter);
      if(asciiLetter > 96 && asciiLetter < 123)
      {
            return true;
      }
      else if(asciiLetter > 64 && asciiLetter < 91)
      {
            asciiLetter += 32;
            letter = asciiLetter;
            return true;
      }
      cout << "Sorry, only lowercase letters please.\n";
      return false;
}

bool Player2::haveGuessed()
{
      for(int i = 0; i < getIncorLettersLen(); i++)
      {
            if(letter == getIncorLetters()[i])
            {
                  cout << "That letter has already been guessed, try again.\n";
                  return true;
            }
      }
      for(int c = 0; c < getCorLettersLen(); c++)
      {
            if(letter == getCorLetters()[c])
            {
                  cout << "That letter has already been guessed, try again.\n";
                  return true;
            }
      }
      return false;
}

void Player2::man()
{
      switch(strikes) 
      {
            case 0:
            break;
            case 1:
                  cout << "-----\n";
                  cout << "|   |\n";
                  cout << "|    \n";
                  cout << "|    \n";
                  cout << "|    \n";
                  cout << "|    \n";
            break;
            case 2:
                  cout << "-----\n";
                  cout << "|   |\n";
                  cout << "|   o\n";
                  cout << "|    \n";
                  cout << "|    \n";
                  cout << "|    \n";
            break;
            case 3: 
                  cout << "-----\n";
                  cout << "|   |\n";
                  cout << "|   o\n";
                  cout << "|   |\n";
                  cout << "|    \n";
                  cout << "|    \n";
            break;
            case 4:
                  cout << "-----\n";
                  cout << "|   |\n";
                  cout << "|   o\n";
                  cout << "|  /|\\\n";
                  cout << "|    \n";
                  cout << "|    \n";
            break;
            case 5:
                  cout << "-----\n";
                  cout << "|   |\n";
                  cout << "|   o\n";
                  cout << "|  /|\\\n";
                  cout << "|  / \\\n";
                  cout << "|    \n";
            break;
            default:
            cout << "Error displaying man\n";
      }
}
