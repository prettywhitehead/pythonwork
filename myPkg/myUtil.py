#!/usr/bin/env python

from __future__ import print_function # 2.X compatibility

import myClass

def warn(S):
   myS = str(S)
   print('Warning: ' + myS)

def err(S):
   myS = str(S)
   print('Error: ' + myS)

def emptyItem(I):
   if ( not len(I) ):
      warn('This is empty item')
      return True
   else:
      return False

def openFile( fileName, mode ):
   try:
      myFile = open( fileName, mode )
      return myFile
   except (Exception):
      err('FileNotFoundError')

def readFile(fileName):
   """
   read from a file and return the contents as a list of lists
   use ' '.join(myList) to convert list back to string
   The following code returns single list for all the lines of the the file
   try:
      with open(fileName, 'r') as myFile:
         L = myClass.myList()
         rL = myClass.myList()
         for line in myFile:
            L = line.rstrip().split()
            for elm in L:
               rL.append(elm)
         return rL
   except (Exception):
      err('FileNotFoundError')
   """
   try:
      with open(fileName, 'r') as myFile:
         L = myClass.myList()
         for line in myFile:
            L.append(line.rstrip().split())
         return L
   except(FileNotFoundError):
      err('FileNotFound for read !')
