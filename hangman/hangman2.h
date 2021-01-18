#include <iostream>
using namespace std;

class Player2
{
      private:
      // keep track of incorrect strikes
      int strikes = 0;
      int maxStrikes = 5;

      // keep track of correct and incorrect letters guessed 
      string corLetters = "";
      string incorLetters = "";

      // player 2's guess
      string letterStr;
      char letter;
      int asciiLetter;

      public:
      // did the player win or lose yet
      bool keepPlaying(string);

      // get a valid letter from the user and set to letter
      void setLetter();

      // set letter to the space character
      void setSpace();

      char getLetter() { return letter; }

      int getCorLettersLen() { return corLetters.length(); } 

      // add a correct letter to the corLetters
      void setCorLetters();

      string getCorLetters() { return corLetters; }

      int getIncorLettersLen() { return incorLetters.length(); } 

      // add an incorrect letter to incorLetters
      void setIncorLetters();

      string getIncorLetters() { return incorLetters; }

      void incStrikes() { strikes++; }

      int getRemainingStrikes() { return maxStrikes - strikes; }

      // check if letter is a lower case letter
      bool lowercase();

      // check if letter has been guessed already
      bool haveGuessed();      

      // make hangman figure based off strikes
      void man();
};
