import glob
import sys
import string
import os
import re
import shutil

def replace_str_index(text,index=0,replacement=';'):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

if __name__ == '__main__':

  if len(sys.argv) != 2: # 1 is addValueInRegion.py + 3 arguments
    print "ERROR: Need  argumens: the file to transform."
    sys.exit(1) 
    
  script_name = sys.argv[0]
  input_file = sys.argv[1]
  
  if os.path.isdir(input_file):
    print "ERROR: " + input_file + " is a directory."
    sys.exit(1)
    
  if not os.path.isfile(input_file):
    print "ERROR: Can't find file " + input_file
    sys.exit(1)
  
  outFile = open("./transformed_" + input_file, "w")
  with open(input_file, "r") as inFile:
    l = inFile.readlines()
    for i in range(0,len(l)):
      if i < 3:
        line = l[i].replace(",","")
        outFile.write(line)
      elif i == 3:
        commas = [pos for pos, char in enumerate(l[i]) if char == ","]
        line = replace_str_index(l[i],commas[0],";")
        line = replace_str_index(line,commas[1],";")
        line = line.replace(",","")
        outFile.write(line)
      else:
        commas = [pos for pos, char in enumerate(l[i]) if char == ","]
        line = replace_str_index(l[i],commas[1],";")
        line = replace_str_index(line,commas[3],";")
        line = replace_str_index(line,commas[4],"")
        outFile.write(line)
    
  outFile.close()
  inFile.close()
  
