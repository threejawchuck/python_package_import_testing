def hello_bar ():
   print "hello from bar"

def hello_bar_and_foo ():
   hello_bar()
   
   from . import foo
   foo.hello_foo()