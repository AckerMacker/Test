#!/usr/bin/python

import time

# Variablen
localtime = time.asctime(time.localtime(time.time()))
count   = 0
x       = 0

# Zeit Anzeige
print "Hello World"
print "It's currently " +  localtime + " in Central Europe"
print " "

# Counter
while (count < 10):
   print "count is: " + str(count) + ". "
   time.sleep(1.0)
   count = count + 1

print "***** eop *****"
