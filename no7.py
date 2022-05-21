a=1 #here a is global variable because it is outside any function

def hh():
    x=3  #here x is local variable because it is declare inside a function hh()
    print(x+a)
hh()
