import webbrowser
import urllib.request  
import random 
from random import seed
from random import randint
import time

def thesarusize(word):
      # open the website with the word as the address and write to file "test.txt"
      address = "https://www.thesaurus.com/browse/" + word + "?s=t"
      urllib.request.urlretrieve(address, "thesarus_page.txt")

      # find the line in the website html with the synonyms in it
      syn_line = 0
      # which synonym on the page is being used
      syn_num = 0

      # seed a random number using system time in milliseconds 
      seed(round(time.time() * 1000))

      # open the file with the thesaurus page and go through each line
      with open('thesarus_page.txt') as f:
            for line in f:
                  # which synonym on the page is being used 
                  rand_num = randint(2, 5)
                  # when the line with the synonyms is reached, index through the line as a string
                  if(syn_line == 136):
                        linestring = str(line)
                        for y in range(len(linestring)):
                              synonym = ""
                              # search for the end of the word "browse" and when found, check if this is the right synonym to use
                              if(linestring[y] == 'w' and linestring[y + 1] == 's' and linestring[y + 2] == 'e'):
                                    if(syn_num == rand_num):
                                          y = y + 4
                                          # create the synonym string and stop when anything other than a letter is reached
                                          for i in range(15):
                                                # stop at the end of the word
                                                if(linestring[y + i] == "\""):
                                                      # temporary synonym and counter for fixing spaces
                                                      temp_syn = ""
                                                      t = 0
                                                      while(t < len(synonym)):
                                                            if(synonym[t] == '%' and synonym[t + 1] == '2' and synonym[t + 2] == '0'):
                                                                  temp_syn = temp_syn + ' '
                                                                  t = t + 2
                                                            else:
                                                                  temp_syn = temp_syn + synonym[t]
                                                            t = t + 1
                                                      # change synonym to the version with correct spaces and return
                                                      synonym = temp_syn
                                                      return synonym
                                                synonym = synonym + linestring[y + i]
                                          break
                                    syn_num = syn_num + 1
                  syn_line = syn_line + 1
      # if for some reason, the function hasn't already returned, display error
      return "ERROR: can't find synonym"

def find_replacements(paragraph):
      # open the file to be editing and turn into a string
      my_file = open(paragraph, "r")
      paragraph_str = my_file.read()
      # string to store the paragraph with replaced words
      new_paragraph = ""
      # is there a capital letter in the word
      found_capital = 0
      # current word
      c_word = ""
      # for the entire paragraph
      for u in range(len(paragraph_str)):
            # if there's a capital letter in a word, flag it
            if((ord(paragraph_str[u]) >= 65 and ord(paragraph_str[u]) <= 90)):
                  found_capital = 1
            # if the current character is not a letter, assume end of the word
            if((ord(paragraph_str[u]) < 97 or ord(paragraph_str[u]) > 122) and 
                  (ord(paragraph_str[u]) < 65 or ord(paragraph_str[u]) > 90) and (ord(paragraph_str[u]) < 48 or ord(paragraph_str[u]) > 57)):
                  # if the word is at least 4 letters long, start replacement process
                  if(len(c_word) > 3):
                        # try to search the thesarus for the word
                        while True:
                              # if it works, check if the case of the first letter needs to be raised
                              try:
                                    the_word = thesarusize(c_word)
                                    case_word = ""
                                    if(found_capital == 1):
                                          for h in range(len(the_word)):
                                                case_word = case_word + chr(ord(the_word[h]) - 32 * found_capital)
                                                found_capital = 0
                                          the_word = case_word
                                    # add the new word to the new paragraph
                                    new_paragraph = new_paragraph + the_word + " "
                                    break
                              # if the thesarus couldn't find the word, leave it as is
                              except urllib.error.HTTPError:
                                    # add the original word to the new paragraph
                                    new_paragraph = new_paragraph + c_word + " "
                                    break
                  else:
                        # reset the capital flag and add the current word since it is not
                              # long enough to be replaced
                        found_capital = 0
                        new_paragraph = new_paragraph + c_word + " "
                  # reset current word
                  c_word = ""
            else:
                  # add the current letter to the current word
                  c_word = c_word + paragraph_str[u]
            # if the current character is punctuation, remove space after the previous 
                  # word and add the punctuation to the new paragraph
            if(ord(paragraph_str[u]) >= 33 and ord(paragraph_str[u]) <= 47):
                  new_paragraph = new_paragraph[:-1] + paragraph_str[u]
      # completed going through original paragraph, so new paragraph is complete
      my_file.close()
      return new_paragraph

def main():
      # try to open user inputted file and ask for another name if not available
      mode = 'a'
      while(mode != 'f' and mode != 'w'):
            mode = input("Would you like to enter an entire file or just individual words? f / w: ")
      # file mode
      if(mode == 'f'):
            while True:
                  try:
                        # pass the file name to the find_replacements file and get the result in new paragraph
                        file_name = input("Enter the name of a file: ")
                        new_paragraph = find_replacements(file_name)
                        break
                  except FileNotFoundError:
                        print("Try again, file not found")
            num_loops = 'a'
            while(ord(num_loops) > 57 or ord(num_loops) < 49):
                  num_loops = input("How many times would you like to translate? ")
                  num_loops = num_loops[0]
            print("Looping " + num_loops + " times")
            # open the new file and write the result to it the first time
            file_name = "2" + file_name
            new_file = open(file_name, "w")
            new_file.write(new_paragraph)
            new_file.close()
            # if the user asked for more than 1 loop, keep going
            if(int(num_loops) > 1):
                  for n in range(int(num_loops) - 1):
                        new_paragraph = find_replacements(file_name)
                        new_file = open(file_name, "w")
                        new_file.write(new_paragraph)
                        new_file.close()
      # individual word mode
      elif(mode == 'w'):
            indiv_word = 'a'
            # get user inputted words and find synonyms until they quit
            while(indiv_word != 'q'):
                  indiv_word = input("Enter a word. (wite 'q' to quit): ")
                  # replace any spaces with %20 for the website address
                  no_space_word = ""
                  for h in range(len(indiv_word)):
                        if(indiv_word[h] == ' '):
                              no_space_word = no_space_word + "%20"
                        else:
                              no_space_word = no_space_word + indiv_word[h]
                  print("Your word: " + indiv_word)
                  indiv_word = no_space_word
                  while True:
                        try:
                              print("\"Synonym\": " + thesarusize(indiv_word))
                              break
                        except urllib.error.HTTPError: 
                              print("No synonyms found")
                              break

main()
