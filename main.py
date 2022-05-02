import os
import time
import random

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i_letter = 0
j = 0
k = 0 
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

name1 = input("The first lover (only enter the first name and no caps!): ")
name2 = input("The second lover (only enter the first name and no caps!): ")

def clear():
  os.system('clear')

def percentageCalculation():
  global part1
  global part2

  if part2 >= 10 and part1 == 9:
    part1 = 10
    part2 = 0
    percentageCalculation()
  elif part2 >= 10:
    part1 += 1
    part2 = part2 - 10
    percentageCalculation()
  elif part1*10 + part2 > 100:
    part1 = 10
    part2 = 0

clear()

for letter in name2:
  if letter == "a" in name2:
    a +=1
  elif letter == "b" in name2:
    b +=1
  elif letter == "c" in name2:
    c +=1
  elif letter == "d" in name2:
    d +=1
  elif letter == "e" in name2:
    e +=1
  elif letter == "f" in name2:
    f +=1
  elif letter == "g" in name2:
    g +=1
  elif letter == "h" in name2:
    h +=1
  elif letter == "i" in name2:
    i_letter +=1
  elif letter == "j" in name2:
    j +=1
  elif letter == "k" in name2:
    k +=1
  elif letter == "l" in name2:
    l +=1
  elif letter == "m" in name2:
    m +=1
  elif letter == "n" in name2:
    n +=1
  elif letter == "o" in name2:
    o +=1
  elif letter == "p" in name2:
    p +=1
  elif letter == "q" in name2:
    q +=1
  elif letter == "r" in name2:
    r +=1
  elif letter == "s" in name2:
    s +=1
  elif letter == "t" in name2:
    t +=1
  elif letter == "u" in name2:
    u +=1
  elif letter == "v" in name2:
    v +=1
  elif letter == "w" in name2:
    w +=1
  elif letter == "x" in name2:
    x +=1
  elif letter == "y" in name2:
    y +=1
  elif letter == "z" in name2:
    z +=1

for letter in name1:
  if letter == "a" in name1:
    a +=1
  elif letter == "b" in name1:
    b +=1
  elif letter == "c" in name1:
    c +=1
  elif letter == "d" in name1:
    d +=1
  elif letter == "e" in name1:
    e +=1
  elif letter == "f" in name1:
    f +=1
  elif letter == "g" in name1:
    g +=1
  elif letter == "h" in name1:
    h +=1
  elif letter == "i" in name1:
    i_letter +=1
  elif letter == "j" in name1:
    j +=1
  elif letter == "k" in name1:
    k +=1
  elif letter == "l" in name1:
    l +=1
  elif letter == "m" in name1:
    m +=1
  elif letter == "n" in name1:
    n +=1
  elif letter == "o" in name1:
    o +=1
  elif letter == "p" in name1:
    p +=1
  elif letter == "q" in name1:
    q +=1
  elif letter == "r" in name1:
    r +=1
  elif letter == "s" in name1:
    s +=1
  elif letter == "t" in name1:
    t +=1
  elif letter == "u" in name1:
    u +=1
  elif letter == "v" in name1:
    v +=1
  elif letter == "w" in name1:
    w +=1
  elif letter == "x" in name1:
    x +=1
  elif letter == "y" in name1:
    y +=1
  elif letter == "z" in name1:
    z +=1

part1 = a+b+c+d+e+f+g+h+i_letter+j+k+l+m
part2 = n+o+p+q+r+s+t+u+v+w+x+y+z

percentageCalculation()

percentage = "Your love percentage is: " + str(part1*10+part2) + "%"

print(percentage)