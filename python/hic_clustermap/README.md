# Hi-C Matrix Clustering
This program was my summer internship project for WashU in the bioinformatics department. It takes Hi-C data for specific chromosomes from a mouse genome as input. It then takes turns this data into a matrix and plots it as a clustermap. The program also clusters the matrix and presents these clusters as bedgraphs. It also produces output files for the cluster data. 

## Options
The program allows the user to pick:

-which chromosomes

-how many clusters

-clustering method

-clustering metric

And outputs:

-clustermap with bedgraphs

-output files with columns for chromosome, start position on the chromosome, end position on the chromosome, and cluster number


## Table of Contents
clustermap.py - uses thesaurus.com to replace words

sources.pdf - all sources I gathered throughout the 8-week internship. Some were for understanding genomics in general or my final presentation, but most were related to the program itself

## Acknowledgements
Haley Abel was my mentor for this summer. She provided the idea for the project as well as part of the code in the clustermap.py file to start with that plotted matrices as a clustermap.

Chris Miller organized the internship program this summer.

Tim Ley led the lab I was a part of for the summer.
