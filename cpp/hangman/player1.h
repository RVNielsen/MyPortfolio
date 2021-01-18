#include <iostream>
#include <string>
using namespace std;

class Player1
{
      private:
      // the word in the form of a character array
      char * arrayWord;
      string answer;

      // length of the word
      int wordLen;

      // ascii value of a letter in the word
      int asciiLetter;

      public:
      // get a valid word from the user and set it to arrayWord
      void setWord();

      char * getWord() { return arrayWord; }

      void setAnswer();

      string getAnswer() { return answer; }

      // set wordLen to an integer
      void setLen(int);

      int getLen() { return wordLen; }

      // remove a guessed letter from the word for later checks
      char * updateWord(char[], int, int);

      // ensure word is only lowercase letters
      void lowercaseWord();
};
