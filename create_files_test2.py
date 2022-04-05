import sys
import os
import numpy as np
import pandas as pd

l = []
with open("/home/yulytas/python_training/test2.txt") as f:
    l = [line.strip() for line in f  if "\t" not in line]

