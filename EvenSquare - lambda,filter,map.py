# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 00:02:24 2018

@author: sandesh dyavanapelli
"""

a=sum(list(map(lambda x:x**2,list(filter(lambda x:x%2==0,range(1,151)))))[7:])
print(a)