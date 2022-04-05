import numpy as np
import pandas as pd
import os
import sys

f = open("/home/yulytas/python_training/test1.txt")

for i in f:
     i = i.rstrip()
     a = open("test_"+i+".txt", "x")
     a.write("Welcome to test "+i+"\n :) \n")
     a.close()
