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
