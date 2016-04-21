# make sure you can talk to fill 
# the long way of importing
import graphics.primitive.fill
graphics.primitive.fill.hello_fill()


# that's a lot to type!  if we just want to put fill into our namespace, try this
from graphics.primitive import fill
fill.hello_fill()  # much better!

# this function calls fill and fill calls a function in text (same subpackage)
fill.hello_fill_and_text()

# this function calls fill and fill calls a function in jpg (different subpackage)
fill.hello_fill_and_jpg()

# we could be crass and put everything in our global space
from graphics.primitive.fill import *
hello_fill() # naughty script.  naughty. 

##############################

##############################
# let's talk to png which talks to foo
# png is part of package graphics.formats which is in the local dir ./
# foo is part of package mypackage.A which is in the contrib directory ./contrib
# but who should be in charge of resolving this conundrum? png? this file?

# first make sure we can talk to png
from graphics.formats import png
png.hello_png()

# png isn't going to know how to call foo
# we have three choice, 
# 1) extend the path in graphics.formats.png
# 2) extend the path in graphics.formats.__init__.py
# 3) extend the path right here in river city

# i think #3 is the cleanest as it's divide and conquor
# let the calling script (this one) understand how to modify the path to include
# the package in question
# and let the function, which has to use that package, understand how the package 
# is constructed.
import sys
import os
sys.path.insert(0,os.path.join (os.path.dirname (__file__), "contrib"))

# now call the combo package call
png.hello_png_and_foo()