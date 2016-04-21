
# this is the same directory so it works
import graphics

# make sure you can talk to fill 
from graphics.primitive import fill
fill.hello_fill()
fill.hello_fill_and_text()

fill.hello_fill_and_jpg()

###############################
# now we want to talk directly to foo which is in contrib/mypackage

# this doesn't work b/c contrib isn't a package
# furthermore, it's brittle so don't do it
# from contrib.mypackage.A import foo


##############################
# let's talk to png which talks to foo
# png is part of package graphics.formats which is in the local dir ./
# foo is part of package mypackage.A which is in the contrib directory ./contrib
# but this file shouldn't have to worry about that.  png should take care of it

# first make sure we can talk to png
from graphics.formats import png
png.hello_png()

# png isn't going to know how to call foo
# we have three choice, 
# 1) extend the path in graphics.formats.png
# 2) extend the path in graphics.formats.__init__.py
# 3) extend the path right here in river city

# i think #3 is the cleanest
import sys
import os
sys.path.insert(0,os.path.join (os.path.dirname (__file__), "contrib"))


# now call the combo package call
png.hello_png_and_foo()