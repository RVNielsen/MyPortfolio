#!/bin/bash

clear
javac source/*.java
mv source/*.class code
jar -cvfm Project1.jar source/Project1.txt *
java -jar Project1.jar