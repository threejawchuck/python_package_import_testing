

def hello_fill ():
   print "hello from fill"

def hello_fill_and_text ():
   hello_fill()
   
   ############################
   # fill needs symbols defined in the text module which happens to be in this directory

   # i could do this with a package reference, but this hard codes the package name
   # inside the module reducing portability
   # from graphics.primitive import text

   # instead, i'll use a relative path import
   from . import text

   ############################
   # now call the function in text
   text.hello_text()
   
def hello_fill_and_jpg ():
   hello_fill()
   
   ############################
   # fill needs symbols defined in the jpg which is NOT in this directory

   # again, i could do this with a package reference, but this hard codes the package name
   # inside the module reducing portability
   # from graphics.formats import jpg

   # instead, i'll use a relative path import
   # notice that we don't put ../formats or ..\formats, just ..formats
   from ..formats import jpg

   ############################
   # now call the function in text
   jpg.hello_jpg()
   