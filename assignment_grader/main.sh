# set -x

# remove the folders if present
rm -r ./sampleInput/*
rm -r ./expectedOutput/*
rm -r ./submissions/*
rm -r ./counters/*

# make new versions of the folders
mkdir -p sampleInput
mkdir -p expectedOutput
mkdir -p submissions
mkdir -p counters
mkdir -p myOutput

# unzip the data
unzip *[Ii]nput.zip -d ./sampleInput
unzip *[Oo]utput.zip -d ./expectedOutput
unzip *submissions.zip -d ./submissions

# create terms 
submission_files=`ls ./submissions`
sample_files=`ls ./sampleInput`
expected_output=`ls ./expectedOutput`

# create counter files for tracking correct and incorrect submissions
for subFile in $submission_files;
do
      > ./counters/count_$subFile.out
done


# variable to hold total number of files to be tested
filenum=0

# for each sample file
for sampleFile in $sample_files; 
do
      # increment the filenum
      filenum=$((filenum+1))

      # open the file and read the input
      cat sampleInput/$sampleFile | while read line
      do
            # for each submission file
            for subFile in $submission_files; 
            do
                  # if the submission file needs input, don't accept
                  if [[ "$subFile" = "read"* ]]; 
                  then
                        echo "$subFile requires user input -- subFile not tested!"
                        continue
                  fi

                  # run the submission program and send output to myOutput
                  swipl submissions/$subFile $line > myOutput/output_$subFile.out

                  # check for differences between myOutput and expectedOutput
                  diff_lines=`diff ./myOutput/output_$subFile.out \
                                    ./expectedOutput/$sampleFile.out \
                                    --ignore-space-change --ignore-case --ignore-blank-lines | egrep -c "^<|^>"`
                  
                  # if there was a difference
                  if [ $diff_lines != 0 ]
                  then
                        # add a 1 to the counter file
                        echo "1" >> ./counters/count_$subFile.out
                  else
                        # otherwise, add a 0 for no erros
                        echo "0" >> ./counters/count_$subFile.out
                  fi
            done
      done
done

# create a term for counter files
counter_files=`ls ./counters`

# clear the grades file
> grades.txt

# remove brackets from the test files
for outputFile in $expected_output;
do
      toCheck=`cut -b 2- expectedOutput/$outputFile`
      echo $toCheck | rev > expectedOutput/$outputFile
      toCheck=`cat expectedOutput/$outputFile`
      toCheck=`cut -b 2- expectedOutput/$outputFile`
      echo $toCheck | rev > expectedOutput/$outputFile
      toCheck=`cat expectedOutput/$outputFile`
done

# for each counter file
for countFile in $counter_files;
do
      # create variables for score and incrementing
      score=0
      inc=0
      
      # open the counters file
      cat counters/$countFile | (while read line
      do
            # if the line is a 0, add 1 correct file to the score
            if [ $line == 0 ]
            then
                  score=$((score+1))
            fi
            # increment variable
            inc=$((inc+1))
      done
      # send the countFile name to the nameFile for editing
      echo "$countFile" > nameFile.txt
      # remove "count_" from it
      newName=`cut -b 7- nameFile.txt`
      # send new name to nameFile in reverse
      echo $newName | rev > nameFile.txt
      # remove "tuo.lp." (reversed ".pl.out")
      newName=`cut -b 8- nameFile.txt`
      # set newName to whats in the nameFile
      set newName=<nameFile.txt
      # reverse
      echo $newName |rev > nameFile.txt
      # get the final results of just the student's name and store in newName
      newName=$(< nameFile.txt)

      # calculate the percent
      percent=`echo "scale=2 ; $score / $filenum * 100" | bc`
      percent=`echo ${percent%.*}`

      # check if student hard-coded in answer
      for outputFile in $expected_output; 
      do
            toCheck=`cat expectedOutput/$outputFile`
            didGrep=`grep -i "$toCheck" submissions/$newName.pl`
            if [ ! -z "$didGrep" ]
            then
                  # add a star to percent if hard-coded
                  percent="${percent}*"
                  break
            fi
      done
      # output the info 
      echo "$newName, $percent" >> grades.txt)
done
