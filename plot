#!/usr/bin/env python
import os
import sys
import json
#for plotting
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

def main():
    happy_list_file = open(sys.argv[1])
    #file_save_format = []
    
    for line in happy_list_file:
        mystr = json.loads(line)
        #print type(mystr)
    
    #using bar of plt object for drawing
    plt.bar(range(len(mystr)), mystr.values(), width=0.8, bottom=0)
    plt.xticks(range(len(mystr)), mystr.keys())    
    #plt.show()
    #pl.savefig('.'.join(str(file_save_format)))

    #save to file
    pl.savefig("plot.pdf")
    pl.savefig("plot.png")
    
    
if __name__ == '__main__':
    main()
