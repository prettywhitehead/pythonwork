#!/usr/bin/env python

from __future__ import print_function # 2.X compatibility

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

