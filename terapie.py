#numero decessi al giorno
import csv
import re
import pandas as pd
import io
import requests
import matplotlib.pyplot as plt
import numpy as np

    #print(array2)


with open('andamento-nazionale.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    v=0
    array=[]
    for linea in csv_reader:
        #print(linea[3])
        print(linea[0]+','+str(int(linea[3])-v))
        v=int(linea[3])
