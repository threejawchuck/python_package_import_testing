def hello_png ():
   print "hello from png"
   
def hello_png_and_foo ():
   # note that foo is not in this package.  it's in contrib!
   hello_png()
   
   # you'd like to be able to do something like this, but this function
   # doesn't understand where mypackage is (nor should it!)
   from mypackage.A import foo
   foo.hello_foo()
