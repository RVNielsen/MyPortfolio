import argparse, sys
from os import link
from types import new_class
import numpy as np
from numpy.core.fromnumeric import argsort
from numpy.core.shape_base import vstack
from pandas.io.formats.format import return_docstring
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster, weighted
import scipy,sklearn,code
import pandas as pd
import csv
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme(color_codes=True)
import pdb
import os


# which chroms are going to be considered
# this option is placed here rather than the command line
#   so the user doesn't have to write it out each time  
ODDS = [3, 19]
EVENS = [16]
# wasn't able to get all chroms to run
#   smaller parts worked fine
# ODDS = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# EVENS = [2, 4, 6, 8, 10, 12, 14, 16, 18]
# dictionaries for methods and metrics
METHODS = {"a" : "average", "b" : "weighted", "c" : "ward", "d": "other (not listed)"}
METRICS = {"a" : "cityblock", "b" : "euclidean", "c" : "minkowski", "d": "other (not listed)"}


# "Getting lengths of chroms"
def getLens():
  # get approximate lengths of each chrom
  lens = np.loadtxt('../../../abelhj/amanda_projects/hic/data_for_rachel/straw.lengths.txt', dtype = 'int32')
  lens[:, 1] = lens[:, 1] / 1e5
  L_ODDS = [o - 1 for o in ODDS]
  L_EVENS = [e - 1 for e in EVENS]
  lens_odd = lens[L_ODDS, :]
  lens_even = lens[L_EVENS, :]

  # sum all the lengths and reformat
  cs = np.roll(np.cumsum(lens_odd[:, 1]), 1)
  cs[0] = 0
  lens_odd = np.hstack((lens_odd, np.reshape(cs, [cs.shape[0], 1])))
  lens_odd[:, 2] = lens_odd[:, 2] - lens_odd[0, 2]
  cs = np.roll(np.cumsum(lens_even[:, 1]), 1)
  cs[0] = 0
  lens_even = np.hstack((lens_even, np.reshape(cs, [cs.shape[0], 1])))
  lens_even[:, 2] = lens_even[:, 2] - lens_even[0, 2]
  lens = np.vstack((lens_odd, lens_even))
  # return lengths of the chroms being used to get an idea for the matrix size
  return lens


# "Creating array of chroms"
def getChroms(lens):
  chromArr = []
  for odd in ODDS:
      for even in EVENS:
        [first, second] = [odd, even]
        [o, e] = [odd, even]
        # use the [odd, even] to open the file with the corresponding name
        ctx = np.loadtxt('../../../abelhj/amanda_projects/hic/interchrom/M_CU-44125-HiC_Seq_44125_WT/even_odd/' 
                          + str(odd) + '.' + str(even) + '.txt.gz')
        # reformat to get:
        #     [chrom1, chrom2, number of interactions between the two]
        if odd > even:
            ctx[:, [0, 1]] = ctx[:, [1, 0]]
            [first, second] = [second, first]
        chromList = []
        for a in ctx:
          chromList.append([str(first) + " " + str(a[0]), str(second) + " " + str(a[1])])
        ctxa = ctx.copy()
        ctxb = ctx.copy()
        ctxa[:, [0, 1]] = [first, second]
        ctx[:, [0, 1]] = ctx[:, [0, 1]] / 1e5
        [offset1, offset2] = [int(lens[np.where(lens[:, 0] == odd), 2]), int(lens[np.where(lens[:, 0] == even), 2])]
        ctx[:, [0, 1]] = ctx[:, [0, 1]] + [offset1, offset2]
        ctx = np.hstack([ctx, ctxa[:, [0, 1]], ctxb[:, [0, 1]]]) 
        chromArr.append(ctx)
  # returning array of data from even_odd folder for each chrom combination
  return chromArr


# "Creating dense matrix"
def createMatrices(chromArr, newChroms):
  chromArr = np.vstack(chromArr)
  chromArr[:, 0] = scipy.stats.rankdata(chromArr[:, 0], method='dense') - 1
  chromArr[:, 1] = scipy.stats.rankdata(chromArr[:, 1], method='dense') - 1
  # create variable with (chrom1 pos, chrom2 pos, and scaled number of interactions)
  chromDF = pd.DataFrame(chromArr, columns = ['r1', 'r2', 'ctx', 'chrom1', 'chrom2', 'pos1', 'pos2'])
  # list of nums
  key = []
  # list of strings of chrom1, chrom2, pos1, pos2
  value = []
  # create dictionary to remember info about the chroms 
  #   after rows and cols are dropped from the matrix
  for c in range(len(chromArr)):
    key.append(c + 1)
    value.append(str(chromArr[c][3]) + " " + str(chromArr[c][4]) + " "
                + str(chromArr[c][5]) + " " + str(chromArr[c][6]))
  chromDict = dict(zip(key, value))
  key = np.array(key)
  sparseChroms = scipy.sparse.coo_matrix((np.array(chromArr[:, 2], dtype = 'float64'), (np.rint(chromArr[:, 0]).astype('int32'), 
                                  np.rint(chromArr[:, 1]).astype('int32'))))
  sparseChromsKey = scipy.sparse.coo_matrix((np.array(key[:], dtype = 'int32'), (np.rint(chromArr[:, 0]).astype('int32'), 
                                  np.rint(chromArr[:, 1]).astype('int32'))))
  [nrow, ncol] = sparseChroms.shape
  # determine which rows and cols will be dropped
  [drop_rows, drop_cols] = [[], []]
  for ii in range(nrow):
    if sparseChroms.getrow(ii).nnz / ncol < 0.2:
      drop_rows.append(ii)
  for ii in range(ncol):
    if sparseChroms.getcol(ii).nnz / nrow < 0.2:
      drop_cols.append(ii)

  chromDF = chromDF[~chromDF['r1'].isin(drop_rows)].copy()
  chromDF = chromDF[~chromDF['r2'].isin(drop_cols)].copy()
  chromDF['row'] = scipy.stats.rankdata(chromDF['r1'].values, method = 'dense') - 1
  chromDF['col'] = scipy.stats.rankdata(chromDF['r2'].values, method = 'dense') - 1
  # drop the sparse rows and cols and save dense matrix to file
  sArr = sparseChroms.toarray()
  sArr = np.delete(sArr, drop_cols, axis = 1)
  dArr = np.delete(sArr, drop_rows, axis = 0)
  dArr = np.log1p(dArr)
  dArr = scipy.stats.zscore(dArr, axis = 1)
  np.savetxt("matrixData.txt", dArr, fmt = "%s")
  
  # keep track of a matrix of identical size that holds
  #   the extra information from the dictionary
  sArrKey = sparseChromsKey.toarray()
  sArrKey = np.delete(sArrKey, drop_cols, axis = 1)
  dArrKey = np.delete(sArrKey, drop_rows, axis = 0)
  np.savetxt("matrixDataCoded.txt", dArrKey, fmt = "%s")

  # write the chrom dictionary to a file, so the coded matrix
  #   can be decoded later
  with open("chromDict.txt", "w") as f:
    f.write(newChroms)
    f.write("\n_\n")
    for key, value in chromDict.items():
      f.write('%s:%s\n' % (key, value))


# prompt the user to select a number of clusters, method, and metric
def getMdMc():
  # ask user how many clusters
  while True:
    try:
      clusterNum = input("\nHow many clusters would you like to use (2 - 8)?\n")
      clusterNum = clusterNum[0]
      if(ord(clusterNum) >= 50 and ord(clusterNum) <= 56):
        break
      else:
        print("*Invalid choice. Please give a number between 2 and 8.*", flush = True)
    except:
      print("*Invalid choice. Please give a number between 2 and 8.*", flush = True)
  # ask user which method
  while True:
    try:
      md = input("\nWhich method would you like to use (a, b, c, d)? \na. average\nb. weighted" 
                  + "\nc. ward\nd. other (not listed)\n")
      md = md[0].lower()
      if(ord(md) >= 97 and ord(md) <= 99):
        theMethod = METHODS[md]
        break
      elif(ord(md) == 100):
        theMethod = input("Type the name of the metric: \n")
        break
      else:
        print("*Invalid choice. Please select one of the corresponding letters.*", flush = True)
    except:
      print("*Invalid choice. Please select one of the corresponding letters.*", flush = True)
  # ask user which metric
  while True:
    try:
      mc = input("\nWhich metric would you like to use (a, b, c, d)? \na. cityblock\nb. euclidean" 
                  + "\nc. minkowski\nd. other (not listed)\n")
      mc = mc[0].lower()
      if(ord(mc) >= 97 and ord(mc) <= 99):
        theMetric = METRICS[mc]
        break
      elif(ord(mc) == 100):
        theMetric = input("Type the name of the metric: \n")
        break
      else:
          print("*Invalid choice. Please select one of the corresponding letters.*", flush = True)
    except:
      print("*Invalid choice. Please select one of the corresponding letters.*", flush = True)
  # return number of clusters, clustering method, and clustering metric
  return clusterNum, theMethod, theMetric


# output the results of the clutsering to a file
def getOutLines(clusters, side):
  # clear the output file and add column headers
  chromDict = {}
  chrs = ""
  found = 0
  # get the dictionary of keys and values
  with open("chromDict.txt", "r") as f:
    lines = f.readlines()
    for n in lines:
      if (found == 1):
        (key, value) = n.split(':')
        chromDict[int(key)] = value[:-1]
      elif (n[0] == "_"):
        found = 1
      else:
        chrs += str(n)
  totalLines = []
  realClusters = []
  # get the matrix of keys
  with open("matrixDataCoded.txt", "r") as f2:
    lines = f2.readlines()
    rowCounter = 0
    for n in lines:
      colCounter = 0
      for s in n.split(' '):
        if (int(s) != 0):
          totalLines.append(chromDict.get(int(s)))
          if (side == 'cols'):
            realClusters.append(clusters[colCounter])
          elif (side == 'rows'):
            realClusters.append(clusters[rowCounter])
        colCounter += 1
      rowCounter += 1 
  # call writeOutput with the number of clusters and lines with all unknown 0's removed
  # also include the side: rows or cols
  writeOutput(realClusters, totalLines, side)


# write the clustered bedgraph output information to files
def writeOutput(clusters, lines, side):
  # lists for each column in the output file
  #   chrom number, start position, end position, and cluster number
  chrom = []
  start = []
  end = []
  cluster = []
  # is the loop in the middle of a cluster right now (1)
  #   or is it ready to look for the start the next cluster 
  midst = 0
  # input strings are in the format: chrom1 chrom2 pos1 pos2
  #   is the loop currently tracking a change in pos1 (1) or pos2 (2)
  path = 0
  # using the coded matrix and the matrix of clusters
  #   match up the relavent chrom information with the cluster number
  for num in range(len(lines)):
    c1, c2, p1, p2 = lines[num].split()
    # base case
    #   tie up loose ends and stop looping
    if (num >= len(lines) - 1):
      if (path == 1):
        if (midst == 0):
          chrom.append(c1)
          start.append(p1)
          cluster.append(clusters[num])
        end.append(p1)
      elif (path == 2):
        if (midst == 0):
          chrom.append(c2)
          start.append(p2)
          cluster.append(clusters[num])
        end.append(p2)
      break
    # if the loop is looking at a change in chrom1 from the source string
    elif (midst == 1):
      # if the cluster being tracked will change next iteration
      #   set the end postiion for this cluster
      if (cluster[-1] != clusters[num + 1]):
        midst = 0
        if (path == 1):
          end.append(p1)
        elif (path == 2):
          end.append(p2)
    # if the loop is not in the middle of a cluster, start a new cluster
    if (midst == 0):
      midst = 1
      nc1, nc2, np1, np2 = lines[num + 1].split()
      # determine if the loop will be tracking a change in position for chrom1 or chrom2
      if (np1 > p1):
        chrom.append(c1)
        start.append(p1)
        path = 1
      else:
        chrom.append(c2)
        start.append(p2)
        path = 2
      cluster.append(clusters[num])
  
  # after the 4 lists have been completed (chrom, start, end, cluster)
  #   write the results to a temp file
  with open("outFile_" + side + "temp.txt", "a") as f3:
    for i in range(len(chrom)):
      chromStr = str(chrom[i]).ljust(7, ' ')
      startStr = str(start[i]).ljust(14, ' ')
      endStr = str(end[i]).ljust(14, ' ')
      f3.write(chromStr + startStr + endStr + str(cluster[i]) + "\n")
  # write the temp file to the final output file (col or row),
  #   but without duplicates and in alphabetical order
  usedLines = set() 
  outFile = open("outFile_" + side + ".txt", "w")
  outFile.write("chrom  start         end           cluster\n")
  with open("outFile_" + side + "temp.txt", "r") as tempFile:
    # alphabetize the results
    # lines = sorted(tempFile.readlines())
    lines = tempFile.readlines()
    for a in lines:
      if (a not in usedLines):
        outFile.write(a)
        usedLines.add(a)
  outFile.close()
  # delete the temp file
  os.remove("outFile_" + side + "temp.txt")


# cluster a matrix and return the clusters 
def clusterMatrix(clusterNum, matrix, theMethod, theMetric, side):
  # create the matrix with the method and metric and cluster it
  linkagedMatrix = linkage(matrix, method = theMethod, metric = theMetric)
  clusters = fcluster(linkagedMatrix, int(clusterNum), criterion = 'maxclust')
  # reformat the data to get the matrix and clusters as lists
  clusterList = []
  for c in range(len(clusters)):
    clusterList.append(clusters[c])
  # turn the clusters into a form usable by clustermap and numpy
  clusterArr = np.array(clusterList)
  clusterDF = pd.DataFrame(clusterArr)
  clusters = clusterDF.pop(0)

  # return clusters, clusterArr
  matrixList = []
  for a in range(len(clusters)):
    matrixList.append(matrix[a])
  colorsDict = dict(zip(np.unique(clusterArr), "bgrycmkw"))
  assignedColors = [Patch(facecolor = colorsDict[name]) for name in colorsDict]
  colors = clusters.map(colorsDict)
  getOutLines(clusters, side)
  # return the matrix in the form of a list of rows and clusters as colors rather than numbers
  #   as well as colors used and what they mean to be used for the key on the plot
  return matrixList, colors, assignedColors, colorsDict


# create and display the clustermap with bedgraph
def display(clusterNum, theMethod, theMetric, chroms):
  print("-Formatting matrix-", flush = True)
  matrix = np.loadtxt("matrixData.txt")
  # get the matrix and clusters in a format that clustermap can use
  matrixListR, row_colors, assignedColorsR, colorsDictR = clusterMatrix(clusterNum, matrix, theMethod, theMetric, "rows")
  matrixListC, col_colors, assignedColorsC, colorsDictC = clusterMatrix(clusterNum, matrix.transpose(), theMethod, theMetric, "cols")

  # create the clustermap with the row cluster bedgraph
  fig = sns.clustermap(matrixListR, col_colors = col_colors.to_numpy(), row_colors = row_colors.to_numpy(), standard_scale = 1)
  
  # add a cluster legend to the window
  plt.legend(assignedColorsR, colorsDictR, title = 'clusters', bbox_to_anchor = (1, 1), 
              bbox_transform = plt.gcf().transFigure, loc = 'upper right')
  textBox = "Chroms: " + str(chroms) + "\nClusters: " + str(clusterNum) + "\nMethod: " + str(theMethod) + "\nMetric: " + str(theMetric)
  plt.text(2, .001, textBox, fontsize = 'small')
  print('\033[1m' + "---Displaying clustermap---" + '\033[0m', flush = True)
  # display the plot
  plt.show()


# create a matrix using the given chroms
def newMatrix(newChroms):
  print("-Getting lengths of chroms-", flush = True)
  lens = getLens()
  print("-Creating array of chroms-", flush = True)
  chromArr = getChroms(lens)
  print("-Creating dense matrix-", flush = True)
  createMatrices(chromArr, newChroms)


# format and return the chroms listed as constants in the program
def getNewChroms():
  # format the current chroms as a string
  chroms = []
  for o in ODDS:
    chroms.append(o)
  for e in EVENS:
    chroms.append(e)
  chroms.sort()
  # if the first line of chroms is going to be 2 digits each
  #   put less on that line so it doesn't overlap with the plot
  newChroms = ""
  cCounter = 1
  if (len(chroms) >= 4):
    if (int(chroms[3]) >= 10):
      cCounter = 2
  for c in chroms:
    if (newChroms != ""):
      newChroms += ", "
    if (cCounter >= 5):
      newChroms += "\n"
      cCounter = 0
    newChroms += str(c)
    cCounter += 1
  # return the chroms at the top of this file in a format good for displaying
  return newChroms


# ask the user for:
#   number of clusters
#   method
#   metric
#   whether to make a new matrix or display previous matrix data
# then call the appropriate function/s
def main():
  print('\033[1m' + "---Welcome to the clustermap program---" + '\033[0m')
  # get all the user input
  clusterNum, theMethod, theMetric = getMdMc()
  with open("chromDict.txt", "r") as f:
    savedChroms = f.readline()  
    while True:
      currentLine = f.readline()
      if ("_" in currentLine):
        break
      else:
        savedChroms += currentLine
  newChroms = getNewChroms()
  while True:
    try:
      option = input("\nCreate a new matrix to display using chroms:\n" 
                      + str(newChroms) 
                      + "\nor\nDisplay the matrix saved in \"matrixData.txt\" containing chroms: \n" 
                      + str(savedChroms) 
                      + "a. New matrix\nb. Saved matrix\n")
      option = option[0].lower()
      if (ord(option) == 97 or ord(option) == 98):
        break
      else:
        print("*Invalid choice. Please select one of the corresponding letters.*", flush = True)
    except:
      print("*Invalid choice. Please select one of the corresponding letters.*", flush = True)

  print("\n-Selected-" + "\nClusters: " + str(clusterNum) + "\nMethod: " + theMethod + "\nMetric: " + theMetric)
  # create a new matrix or use an existing one
  if (ord(option) == 97):
    print("\n---Creating new matrix---", flush = True)
    newMatrix(newChroms)
    display(clusterNum, theMethod, theMetric, newChroms)
  elif (ord(option) == 98):
    print("\n---Using previous matrix data---", flush = True)
    display(clusterNum, theMethod, theMetric, savedChroms)


main()
