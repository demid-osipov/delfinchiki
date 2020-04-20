#!/usr/bin/env python3 # specifying the laguage probably
# -*- coding: utf-8 -*- # specifying the encoding

import math # importing a bag of math functions
import numpy # importing numpy lol
import matplotlib.pyplot as mpp # importing something to make plots

if __name__=='__main__': # self-explanatory
    arguments = numpy.r_[0:200:0.2] # stating the span (from 0 to 200) and the gap (0.2)
    mpp.plot( # starting to initialize the plot
        arguments, # after this we can state the arguments
        [math.sin(a) * math.sin(a/20.0)for a in arguments] # stating the arguments
        ) # looks like a bracket
    mpp.show() # command used to show the desired plot
    
