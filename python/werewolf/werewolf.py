# list of roles in the game
roles = []

# get a valid number of wolves from the user and add to roles list
while True:
      try:
            wolvesNum = int(input("How many wolves (1 - 3)? One wolf for every 4 players is a good rule-of-thumb: "))
            if(wolvesNum > 0 and wolvesNum <= 3):
                 break
            else:
                  print("Out of range, try again.")
      except:
            print("Invalid, try again.")

for a in range(wolvesNum):
      roles.append("wolf")

# add two more neccessary roles
roles.append("detective")
roles.append("bodyguard")

# display the current roles
print("Current roles: ")
for z in roles:
      print(z)

# get a valid number of villagers from the user and add to roles list
while True:
      try:
            villagerNum = int(input("How many villagers? (random roles will be added for the rest after this): "))
            if(villagerNum > 0 and villagerNum <= 10):
                 break
            else:
                  print("Out of range, try again.")
      except:
            print("Invalid, try again.")

for a in range(villagerNum):
      roles.append("villager")

print("Current roles: ")
for z in roles:
      print(z)

# add the rest of the options for roles
otherRoles = ["match-maker", "hunter", "tough guy", "chief of police", "prince", "witness", "grandma with a gun"]
roles = roles + otherRoles

# create list for players and get user imput for player names
names = []
print("Enter the name of a player. Write \"done\" when all players have been added. For list of players already added, write \"list\":\n")
playerNum = 0
playerNumStr = "Player " + str(playerNum) + ": "
newName = input(playerNumStr)

# while the user wants to keep adding names
while newName != "done" and newName != "Done":
      # print the list of players
      if newName == "list" or newName == "List":
            print("Current players: ")
            for x in names:
                  print(x)
      else:
            print(newName + " added to players")
            # format the name to have 10 total characters for readability later if the name is less than 10 characters long
            y = 10 - len(newName)
            if y > 0:
                  for z in range(y):
                        newName = newName + " "
            names.append(newName)
            playerNum = playerNum + 1
            playerNumStr = "Player " + str(playerNum) + ": "
      newName = input(playerNumStr)

# import ability to randomize seed using internal clock
import random
from datetime import datetime
random.seed(datetime.now())

# check if players and roles are equal in number
def check():
    if(len(names) > len(roles)):
            print("Error, more names than roles.")
            return 0
    if(len(names) == 0):
            print("Error, empty lists.")
            return 0
    return 1

# generate random names and roles recursively
def divvy(nList, rList):
    # halt recursion if the base case is reached: name list consists of 1 final element
    # (roles picked by the user at the beginning may not be able to all be used if there are not enough players)
    if(len(names) == 1):
            rChoice = random.randint(0, len(rList) - 1)
            return [nList[0]] + [rList[rChoice]]
    else:
            nChoice = random.randint(0, len(nList) - 1)
            # ensure that there are 2 wolves, 1 detective, and at least 4 villagers
            if(rList[0] == "wolf" or rList[0] == "detective" or rList[0] == "bodyguard" or rList[0] == "villager"):
                  rChoice = 0
            else:
                  rChoice = random.randint(0, len(rList) - 1)
            # pop the chosen name and role and recursively call the updated lists
            return [nList.pop(nChoice)] + [rList.pop(rChoice)] + divvy(nList, rList)

def main():
      if(check() == 0):
            return      
      output = divvy(names, roles)
      a = 0
      # print table with results
      print("\n\nName       |  Role\n----------------------")
      while a < len(output):
            print(output[a], ": ", output[a + 1], "\n")
            a = a + 2    
main()
