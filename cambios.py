from ast import Delete
from asyncore import read
from itertools import product
from operator import not_
import yaml
import csv
import os
import re
import pandas as pd
import csv
import numpy as np 
from csv import writer

#variables
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
p=0
rex="base-front"

listapps=[ ]
listproducts=[ ]
liststt=[ ]
datos = []


#rex2=re.search("^base-front$")
rootDir ="D:\CHIPER\deployments-beta-stag\develop\\architecture"
filetosearch = "kustomization.yaml"

for relpath,dirs,files in os.walk(rootDir):
      if (filetosearch in files):
            fullpath = os.path.join(rootDir,relpath,filetosearch)
            print(fullpath)
            i=i+1
            print(i)
        
            if a<=i:
                  with open(fullpath,'r')as archiv:
                              line=archiv.readline()
                              while line:
                                    line = archiv.readline()
                                    #print(line)
                                 
                                    
                                    if "base-front"  in line:
                                          print("yesyes" + line)
                                          b=b+0
                                          break


                                    if "base-cronjobs"  in line:
                                          print("yesyes" + line)
                                          b=b+0
                                          break 

                                    if "type: conjob"  in line:
                                          print("yesyes" + line)
                                          #C=C+0
                                          break 

                                    
                                    else:
                                          #try:
                                          if "app: " in line:
                                                            
                                                            lineaprodu=line
                                                            print("yesyes" + line)
                                                            c=c+1
                                                            productapp=line.replace('  app: ', '')
                                                            productapp1=line.replace('\n', '')
                                                            productapp2=line.replace('  app: ', '')
                                                            print(productapp2)
                                                            listapps.append(productapp2.replace('\n', ''))

                                                            print(len(listapps))
                                                

                                          #except:
                                           #     print("no encontro datos de app")

                                          
                                          try:      
                                                if "  product: " in line:
                                                            
                                                            lineaprodu=line
                                                            print("yesyesyes" + line)
                                                            d=d+1
                                                            productname=line.replace('  product: ', '')
                                                            print(productname)
                                                            
                                                            listproducts.append(productname.replace('\n', ''))
                                                            print(len(listproducts))
                                                            print(listproducts)
                                                            validate=True
                                                else:
                                                      #print("no se encontro producto en la linea"+productapp2)
                                                      validate=False
                                                
                                                if validate==False:
                                                            print("no se encontro producto en la linea"+productapp2)


                                          except:
                                                print("no encontro datos de product")

                                                
                                          try:     
                                                if "  stt: " in line:
                                                            
                                                            lineaprodu=line
                                                            print("yesyesyesyes" + line)
                                                            e=e+1
                                                            producstt=line.replace('  stt: ', '')

                                                            producproduc1=producstt.replace('\n', '')
                                                            print(producproduc1)
                                                            liststt.append(producproduc1)
                                                            
                                                            #print(liststt[1]+"palabra")
                                                            print(len(liststt))

                                                            
                                          except:
                                                print("no encontro datos de stt")

#                                     if len(liststt)==len(listproducts) and  len(listapps)==len(listproducts)  and len(listapps)==len(liststt):
#                                                 print("se guardaron los 3 datos")
#                                     else:
#                                                  print("no se guardaron los 3 datos")           
# # print(h)
                             
print(i)
print(listapps)
print(listproducts)
print(liststt)
print(len(listapps))
print(len(listproducts))
print(len(liststt))






 
                        
                        
                              

                              
                  

                        
                       

