#! /usr/bin/env python
import cPickle
x = cPickle.load(open('Data/system.dat'))
f = open('topol.top', 'w')
f.write(x.top_string)
