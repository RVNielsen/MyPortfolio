# Assignment Grader

This program grades students' programming assignments. For each assignment, the script runs each student's submission with the sample input and compares it to the expected output. After each file has been tested, a text file called "grades.txt" is created and lists each student's percentage of correct submissions out of the total assignments checked. A star is put next to any students who may have hard-coded the expected output into their program. (submissions files were not written by me)

## Installation
```
bash assignment_grader.sh

Archive:  sampleInput.zip
extracting: ./sampleInput/input1.txt
extracting: ./sampleInput/input2.txt
extracting: ./sampleInput/input3.txt
Archive:  expectedOutput.zip
extracting: ./expectedOutput/input1.txt.out
extracting: ./expectedOutput/input2.txt.out
extracting: ./expectedOutput/input3.txt.out
Archive:  submissions.zip
inflating: ./submissions/duckd.pl
inflating: ./submissions/leopoldj.pl
inflating: ./submissions/simpsonh.pl
inflating: ./submissions/studentn.pl
```

## Table of Contents
counters - this folder includes a file for each student which contains information about how many correct programs they have submitted

expectedOutput - this unzipped folder includes a file for each assignment being graded with the exact output the students' programs should result in after running the sample input

myOutput - this folder contains the output of each student's program after running them with the sample input

sampleInput - this unzipped folder contains files to be fed to the students' programs

submissions - this unzipped folder contians the students' programs

assignment_grader.sh - the main file containing the bash script

expectedOutput.zip - the original expected output folder

grades.txt - this file contains the information gathered by the bash script about the students' grades

nameFile.txt - this file contains the last name and first initial of one student at a time and is used by the bash script

sampleInput.zip - the original sample input folder

submissions.zip - the original submissions folder

## Usage
The grades.txt file will look like this after running the bash script:
```
duckd, 0
leopoldj, 100
simpsonh, 33*
studentn, 33*
```
-duckd got 0% correct (0 / 3)

-leopoldj got 100% correct (3 / 3)

-simpsonh got 33% correct (1 / 3) and the expected output was found hard-coded into their code

-studentn got 33% correct (1 / 3) and the expected output was found hard-coded into their code
