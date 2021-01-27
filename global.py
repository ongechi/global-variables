#this function modifies global variable 's'
def f():
    global s
    print(s)
    s="look for Greeksforgreeks Python section"
    
s="Python is great"
f()
print(s)