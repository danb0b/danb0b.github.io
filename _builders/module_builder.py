# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:22:34 2018

@author: danaukes
"""

import os
import sys

strings = os.listdir('../egr598/modules')

for item in strings:
    line = item + '|' 
    
    nextfile = item+'/lecture.pdf'
    if os.path.exists('../egr598/modules/'+nextfile):
        line+='[lecture](modules/'+nextfile+') |' 
    else:
        line+=' |' 

    nextfile = item+'/minutae.pdf'
    if os.path.exists('../egr598/modules/'+nextfile):
        line+='[minutae](modules/'+nextfile+') |' 
    else:
        line+=' |' 

    nextfile = item+'/chapter.md'
    if os.path.exists('../egr598/modules/'+nextfile):
        line+='[chapter](modules/'+item+'/chapter.html) |' 
    else:
        line+=' |' 

    nextfile = item+'/code.zip'
    if os.path.exists('../egr598/modules/'+nextfile):
        line+='[code](modules/'+nextfile+') |' 
    else:
        line+=' |' 


    print(line)