# -*- coding: utf-8 -*-
'''
Triangle ABC is a right angle triangle
where angle B is right angle
M is the mid of the hypotenuse AC
You are Given the lenght of AB and BC,
Nowyour task is to find out the angle MBC
'''
from math import  atan, degrees
AB = input()
BC = input()
ANGLE = atan(1.0*AB/BC)
#print str(int(round(degrees(ANGLE))))+'°'
print str(int(round(degrees(ANGLE))))+u"\u00b0"
