#Puzzle one
"""
x="silent"

print(x[2] + x[1] + x[0] + x[5] + x[3] + x[4])
"""
# puzzle two
"""
def func(x):
    return x + 1
f = func
print (f(2) + func(2))
# end def
"""
# Puzzle three
"""
def ifconfussion(x,y):
    if x>y:
        if x-5>0:
            x=y
            if y == y+y:
                return "A"
            else:
                return "B"
        elif x+y>0:
            while x>y:
                x = x-1
            while y>x:
                y = y - 1
            if x == x: return "E"
        else:
            x = 2 * x
            if x == y : return "F"
            return "G"
    else:
        if x-2>y-4:
            x_old = x
            x = y * y
            y = 2 * x_old
            if (x-4)**2>(y-7)**2:
                return "C"
            else:
                return "D"
        return "H"
print(ifconfussion(6,6)) #3,7 = H
    
# end def
"""
#puzzle # 4
"""
string = 'ppy!'
fruit = 'a'.join(list(string))

print(fruit)
"""
# puzzle # 5 only output
# print(3 * 'un' + 'ium')
# print (3 ** 4)

#puzzle # 6
"""
perfix = 'Fi'
print(perfix + 'nxter')
"""

#Puzzle # 7
"""
a = 'hello'
b = 'world'

print (a, b, sep=' Python ', end='!')
"""
#puzzle # 8
'''
python = ['cool']
x = python in python

print(x)
'''
#print ('P"yt\'h"on')
"""
print('\"hello' + " "
      + "world's end\"")
"""