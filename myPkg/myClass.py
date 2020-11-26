#!/usr/bin/env python

from __future__ import print_function # 2.X compatibility
import myUtil

class myList(list):
   """
   This is a customized list
   """
   def __init__(self, value = []): # Constructor
       list.__init__(self)
       self.concat(value)

   def concat(self,value):
       for i in value:
           if not i in self:
               self.append(i)

   def intersect(self,other):
       res = []
       for x in self:
           if x in other:
               res.append(x)
       return myList(res)
    
   def union(self,other):
       res = myList(self)
       res.concat(other)
       return res

   def __and__(self,other): return self.intersect(other)
   def __or__(self,other): return self.union(other)
   def __repr__(self): return 'myList: ' + list.__repr__(self)


class myDict(dict):
   """
   This is a customized dict
   """
   def __init__(self, item = {}): # Constructor
       dict.__init__(self)
       self.update(item)
   
   def add(self, item):
       """
       Add but NOT to overwrite. Use update if you want to overwrite
       """
       for i in item.keys():
           if not i in self.keys():
               self.update({i:item[i]})
       
   def intersect(self, other):
       """
       This is NOT a in-place assignment
       """
       res = myDict()
       kSet = set(self.keys()) & set(other.keys())
       kList = list(kSet)
       if ( not myUtil.emptyItem(kList) ):
          for k in kList:
              res[k] = self[k]
              print('flag:0')
              return res
       else:
          myUtil.warn('There is no overlapping part of these two dicts')
   
   def remove(self, other):
       """
       remove the item in a dict
       """
       for k in other.keys():
           self.pop(k,None)

class myString(str):
   """
   This is a customized str.
   myString is an immutable object
   """

   def __init__(self,other): # Constructor
       str.__init__(other)
   
   def intersect(self, other):  
       ss = self.upper()
       sss = other.upper()
       ssL = ss.split(' ')
       sssL = sss.split(' ')
       ssS = set(ssL)
       sssS =set(sssL)
       L =  list( ssS & sssS)
       return ' '.join(L)

if __name__ == '__main__':
   x = myList([1,2,3,4])
   y = myList([4,5,6,7])
   print(x&y, x|y)
