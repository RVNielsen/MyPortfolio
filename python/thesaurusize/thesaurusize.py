import webbrowser
import urllib.request  
import random 
from random import seed
from random import randint
import time

# ---------- word mode ----------

def fix_spaces(synonym):
      # temporary synonym and counter for fixing spaces
      temp_syn = ""
      t = 0
      while(t < len(synonym)):
            if(synonym[t] == '%' and synonym[t + 1] == '2' and synonym[t + 2] == '0'):
                  temp_syn += ' '
                  t += 2
            else:
                  temp_syn = temp_syn + synonym[t]
            t += 1
      # change synonym to the version with correct spaces and return
      synonym = temp_syn
      return synonym

def get_syn(linestring, y, synonym):
      # create the synonym string and stop when quotes are reached
      i = 0
      while True:
            # stop at the end of the word
            if(linestring[y + i] == "\""):
                  return fix_spaces(synonym) # ----- to fix_spaces
            synonym = synonym + linestring[y + i]
            i += 1

def find_browse(linestring, syn_num):
      rand_num = randint(2, 5)
      for y in range(len(linestring)):
            synonym = ""
            # search for the end of the word "browse" and when found, check if this is the right synonym to use
            if(linestring[y] == 'w' and linestring[y + 1] == 's' and linestring[y + 2] == 'e'):
                  if(syn_num == rand_num):
                        y += 4
                        return get_syn(linestring, y, synonym) # ----- to get_syn
                  syn_num += 1

def thesaurusize(word):
      # open the website with the word as the address and write to file "test.txt"
      address = "https://www.thesaurus.com/browse/" + word + "?s=t"
      urllib.request.urlretrieve(address, "thesaurus_page.txt")

      # find the line in the website html with the synonyms in it
      syn_line = 0
      # which synonym on the page is being used
      syn_num = 0

      # seed a random number using system time in milliseconds 
      seed(round(time.time() * 1000))

      # open the file with the thesaurus page and go through each line
      with open('thesaurus_page.txt') as f:
            for line in f:
                  # when the line with the synonyms is reached, index through the line as a string
                  if(syn_line == 136):
                        return find_browse(str(line), syn_num) # ----- to find_browse
                  syn_line += 1
      # if for some reason, the function hasn't already returned, display error
      return "---ERROR: can't find synonym---"

def find_indiv_syn(indiv_word):
      while True:
            try:
                  syn = str(thesaurusize(indiv_word)) # ----- to thesaurusize
                  if(syn == "None"):
                        return("No synonyms found")
                  else:
                        return("\"Synonym\": " + syn)
                  break
            except urllib.error.HTTPError: 
                  if(indiv_word != 'q'):
                        return("No synonyms found")
                  break

def space_replace(indiv_word):
      # replace any spaces with %20 for the website address
      no_space_word = ""
      for h in range(len(indiv_word)):
            if(indiv_word[h] == ' '):
                  no_space_word += "%20"
            else:
                  no_space_word += indiv_word[h]
      return no_space_word

def word_mode():
      # get user inputted words and find synonyms until they quit
      indiv_word = 'a'
      while(indiv_word != 'q'):
            indiv_word = input("Enter a word. (write 'q' to quit): ")
            print("Your word: " + indiv_word)
            indiv_word = space_replace(indiv_word) # ----- to space_replace
            print(find_indiv_syn(indiv_word)) # ----- to find_indiv_syn

# ^---------- word mode ----------^

# ---------- file mode ----------

def fix_caps(found_capital, the_word):
      case_word = ""
      for h in range(len(the_word)):
            case_word += chr(ord(the_word[h]) - 32 * found_capital)
            found_capital = 0
      return case_word

def try_thes(new_paragraph, c_word, found_capital):
      # try to search the thesarus for the word
      while True:
            # if it works, check if the case of the first letter needs to be raised
            try:
                  the_word = thesaurusize(c_word)
                  if(found_capital == 1):
                        the_word = fix_caps(found_capital, the_word) # ----- to fix_caps
                        found_capital = 0
                  # add the new word to the new paragraph
                  new_paragraph += the_word + " "
                  break
            # if the thesarus couldn't find the word, leave it as is
            except urllib.error.HTTPError:
                  # add the original word to the new paragraph
                  new_paragraph += c_word + " " # todo
                  break
      return new_paragraph

def end_of_word(c_word, found_capital, new_paragraph):
      # if the word is at least the minimum number of letters long, start replacement process
      min_word_len = 4
      if(len(c_word) >= min_word_len):
            # try to search the thesarus for the word
            new_paragraph = try_thes(new_paragraph, c_word, found_capital) # ----- to try_thes
      else:
            # reset the capital flag and add the current word since it is not
            #     long enough to be replaced
            new_paragraph += c_word + " " # todo
      return new_paragraph

def find_replacements(paragraph):
      # open the file to be editing and turn into a string
      my_file = open(paragraph, "r")
      paragraph_str = my_file.read()

      # string to store the paragraph with replaced words
      new_paragraph = ""
      # current word
      c_word = ""
      # should the current word be capitalized
      found_capital = 0

      # for the entire paragraph
      for u in range(len(paragraph_str)):
            # if there's a capital letter in a word, flag it
            if((ord(paragraph_str[u]) >= 65 and ord(paragraph_str[u]) <= 90)):
                  found_capital = 1
            # if the current character is not a letter, assume end of the word
            if((ord(paragraph_str[u]) < 97 or ord(paragraph_str[u]) > 122) and 
                  (ord(paragraph_str[u]) < 65 or ord(paragraph_str[u]) > 90) and 
                        (ord(paragraph_str[u]) < 48 or ord(paragraph_str[u]) > 57)):
                  # if the word is at least 4 letters long, start replacement process
                  new_paragraph = end_of_word(c_word, found_capital, new_paragraph) # ----- to end_of_word
                  # reset current word and capital counter
                  c_word = ""
                  found_capital = 0
            else:
                  # add the current letter to the current word
                  c_word += paragraph_str[u]
            # if the current character is punctuation, remove space after the previous 
            #     word and add the punctuation to the new paragraph
            if(ord(paragraph_str[u]) >= 33 and ord(paragraph_str[u]) <= 47):
                  new_paragraph = new_paragraph[:-1] + paragraph_str[u]
      # completed going through original paragraph, so new paragraph is complete
      my_file.close()
      return new_paragraph

def write_to_file(file_name, range_val):
      for n in range(range_val):
            new_paragraph = find_replacements(file_name) # ----- to find_replacements
            new_file = open(file_name, "w")
            new_file.write(new_paragraph)
            new_file.close()

def file_mode():
      while True:
            try:
                  # pass the file name to the find replacements file and get the result in new paragraph
                  file_name = input("Enter the name of a file: ")
                  break
            except FileNotFoundError:
                  print("Try again, file not found")
      num_loops = 0
      while(int(num_loops) < 1 or int(num_loops) > 9):
            num_loops = input("How many times would you like to thesaurusize the file? (1 - 9): ")
            num_loops = num_loops[0]
      if(int(num_loops) == 1):
            print("Running " + num_loops + " time")
      else:
            print("Running " + num_loops + " times")
      # open the new file and write the result to it the first time
      file_name = "new_" + file_name
      write_to_file(file_name, int(num_loops)) # ----- to write_to_file
      print("Check " + file_name + " for thesaurisized result")

# ^---------- file mode ----------^

def main():
      # try to open user inputted file and ask for another name if not available
      mode = 'a'
      while(mode != 'f' and mode != 'w'):
            mode = input("Would you like to enter an entire file or just individual words? f / w: ")
      # file mode
      if(mode == 'f'):
            file_mode() # ----- to file_mode
      elif(mode == 'w'):
            word_mode() # ----- to word_mode

main()
