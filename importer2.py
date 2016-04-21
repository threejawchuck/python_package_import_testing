# let the calling script (this one) understand how to modify the path to include
# the package in question
# and let the function, which has to use that package, understand how the package 
# is constructed.
import sys
import os
sys.path.insert(0,os.path.join (os.path.dirname (__file__), "contrib"))

# by importing, we will execute the code in __main__
import graphics.__main__

# this strikes me as a wholey bad idea
