# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 17:06:34 2018

@author: danaukes
"""

import os
import sys

strings = os.listdir('../egr598/assignments')

for item in strings:
    line = '* ['+item[:-3]+'](assignments/'+item[:-3]+'.html)'

    print(line)