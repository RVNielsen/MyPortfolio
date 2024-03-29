import webbrowser
import urllib.request  
import random 
from random import seed
from random import randint
import time

# ---------- word mode ----------

# replace any "%20" with " "
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
      return temp_syn

# get the number of synonyms available for the word
def syn_num_max(linestring):
      max_num = 0
      for y in range(len(linestring)):
            # "opposites of" always precedes the antonyms section, so stop once that phrase is found
            if(linestring[y] == 'e' and linestring[y + 1] == 's' and linestring[y + 2] == ' ' and linestring[y + 3] == 'o' and linestring[y + 4] == 'f'):
                  break
            # if not at the anyonyms section, keep looking
            if(linestring[y] == 'w' and linestring[y + 1] == 's' and linestring[y + 2] == 'e'):
                  y += 4
                  max_num += 1
      return max_num

# create the synonym string
def get_syn(linestring, y, synonym):
      i = 0
      while True:
            # stop at the end of the word when quotes start
            if(linestring[y + i] == "\""):
                  return fix_spaces(synonym) # ----- to fix_spaces
            synonym = synonym + linestring[y + i]
            i += 1

# find the synonyms on the page
def find_browse(linestring, syn_num, which_syn):
      # did the user want the 1 synonym on the page or a random one
      if(str(which_syn) == '1'):
            # the word itself is the first "synonym" on the page, so start at 2
            rand_num = 2
      elif(str(which_syn) == 'r'):
            max_num = syn_num_max(linestring) # ----- to syn_num_max
            rand_num = randint(2, max_num)
      for y in range(len(linestring)):
            synonym = ""
            # "browse" always precedes the synonyms
            if(linestring[y] == 'w' and linestring[y + 1] == 's' and linestring[y + 2] == 'e'):
                  if(syn_num == rand_num):
                        y += 4
                        return get_syn(linestring, y, synonym) # ----- to get_syn
                  syn_num += 1

# transfer the page's code to a file and find the line with the synonyms
def thesaurusize(word, which_syn):
      # open the website with the word in the address and write to the file "thesaurus_page.txt"
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
                  # line 136 always includes the synonyms, so only search that one
                  if(syn_line == 136):
                        return find_browse(str(line), syn_num, which_syn) # ----- to find_browse
                  syn_line += 1
      # if for some reason, the function hasn't already returned, display error
      return "---ERROR: can't find synonym---"

# find the synonym of a word in "word mode"
def find_indiv_syn(indiv_word, which_syn):
      while True:
            try:
                  syn = str(thesaurusize(indiv_word, which_syn)) # ----- to thesaurusize
                  if(syn == "None"):
                        return("No synonyms found")
                  else:
                        return("\"Synonym\": " + syn)
                  break
            except urllib.error.HTTPError: 
                  if(indiv_word != 'q'):
                        return("No synonyms found")
                  break

# opposite of fix_spaces(), takes " " and turns into "%20" before turning into web address
def space_replace(indiv_word):
      # replace any spaces with %20 for the website address
      no_space_word = ""
      for h in range(len(indiv_word)):
            if(indiv_word[h] == ' '):
                  no_space_word += "%20"
            else:
                  no_space_word += indiv_word[h]
      return no_space_word

# prompt user for a word and send word to get thesaurusized
def word_mode(which_syn):
      # get user inputted words and find synonyms until they quit
      indiv_word = 'a'
      while(indiv_word != 'q'):
            indiv_word = input("Enter a word. (write 'q' to quit): ")
            print("Your word: " + indiv_word)
            indiv_word = space_replace(indiv_word) # ----- to space_replace
            print(find_indiv_syn(indiv_word, which_syn)) # ----- to find_indiv_syn

# ^---------- word mode ----------^

# ---------- file mode ----------

# if the word originally started with a capital, capitalize the new word
def fix_caps(found_capital, the_word):
      case_word = ""
      for h in range(len(the_word)):
            case_word += chr(ord(the_word[h]) - 32 * found_capital)
            found_capital = 0
      return case_word

# send words off to be thesaurusized 
def try_thes(new_paragraph, c_word, found_capital, which_syn):
      while True:
            try:
                  # get a new word and fix capitalization if necessary
                  the_word = thesaurusize(c_word, which_syn)
                  if(found_capital == 1):
                        the_word = fix_caps(found_capital, the_word) # ----- to fix_caps
                        found_capital = 0
                  new_paragraph += the_word + " "
                  break
            # if the thesarus couldn't find the word, leave it as is
            except urllib.error.HTTPError:
                  # add the original word to the new paragraph
                  new_paragraph += c_word + " " 
                  break
      return new_paragraph

# decide whether the word will be thesaurusized or not
def end_of_word(c_word, found_capital, new_paragraph, which_syn):
      # if the word is at least the minimum number of letters long, start replacement process
      min_word_len = 4
      if(len(c_word) >= min_word_len):
            # try to search the thesarus for the word
            new_paragraph = try_thes(new_paragraph, c_word, found_capital, which_syn) # ----- to try_thes
      else:
            # reset the capital flag and add the current word since it is not
            #     long enough to be replaced
            new_paragraph += c_word + " "
      return new_paragraph

# pick words out of the original file and send them off to "end_of_word"
def find_replacements(paragraph, which_syn):
      # open the file to be editing and turn into a string
      my_file = open(paragraph, "r")
      paragraph_str = my_file.read()

      # string to store the paragraph with replaced words
      new_paragraph = ""
      # current word
      c_word = ""
      # should the current word be capitalized
      found_capital = 0

      for u in range(len(paragraph_str)):
            # if there's a capital letter in a word, flag it
            if((ord(paragraph_str[u]) >= 65 and ord(paragraph_str[u]) <= 90)):
                  found_capital = 1
            # if the current character is not a letter, assume end of the word
            if((ord(paragraph_str[u]) < 97 or ord(paragraph_str[u]) > 122) and 
                  (ord(paragraph_str[u]) < 65 or ord(paragraph_str[u]) > 90) and 
                        (ord(paragraph_str[u]) < 48 or ord(paragraph_str[u]) > 57)):
                  # if the word is at least 4 letters long, start replacement process
                  new_paragraph = end_of_word(c_word, found_capital, new_paragraph, which_syn) # ----- to end_of_word
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

# write the thesaurusized text to the new file
def write_to_file(file_name, range_val, which_syn):
      # progress status for user as the file is thesaurusized
      for n in range(range_val):
            if(n == 0):
                  print("...Running 1st thesaurusize...")
            elif(n == 1):
                  print("...Running 2nd thesaurusize...")
            elif(n == 2):
                  print("...Running 3rd thesaurusize...")
            else:
                  print("...Running " + str(n + 1) + "th thesaurusize...")
            new_paragraph = find_replacements(file_name, which_syn) # ----- to find_replacements
            if(n == 0):
                  file_name = "new_" + file_name
            new_file = open(file_name, "w")
            new_file.write(new_paragraph)
            new_file.close()

# prompt user for a file and number of times to run that file through the thesaurusizer
def file_mode(which_syn):
      while True:
            try:
                  # get valid file name and send file off to write_to_file with num_loops
                  file_name = input("Enter the name of a file: ")
                  num_loops = 0
                  while(int(num_loops) < 1 or int(num_loops) > 9):
                        num_loops = input("How many times would you like to thesaurusize the file? (1 - 9): ")
                        num_loops = num_loops[0]
                  
                  write_to_file(file_name, int(num_loops), which_syn) # ----- to write_to_file
                  break
            except FileNotFoundError:
                  print("Try again, file not found")
      # tell user what the new file is called 
      print("Check " + file_name + " for thesaurisized result")

# ^---------- file mode ----------^

# prompt user for mode 
def main():
      # get mode from user
      mode = 'a'
      while(mode != 'f' and mode != 'w'):
            mode = input("Would you like to enter an entire file or just individual words?\n(\"f\" for file / \"w\" for word): ")
            mode = mode[0]
      # get synonym preference from user and pass all the way to find_browse
      which_syn = ""
      while(str(which_syn) != '1' and str(which_syn) != 'r'):
            which_syn = input("Would you like to get the most relevant synonym (first one) or a random one?\n(\"1\" for first / \"r\" for random) ")
            which_syn = which_syn[0]
      if(mode == 'f'):
            file_mode(which_syn) # ----- to file_mode
      elif(mode == 'w'):
            word_mode(which_syn) # ----- to word_mode

main()
