import re
import pandas as pd

def convert(s):
  
    # initialization of string to ""
    new = ""
  
    # traverse in the string 
    for x in s:
        new += x 
  
    # return string 
    return new

pattern = "L to R:"
file = open(r"C:\Users\Declan\Documents\wcuyearbook83.txt", "r")
text = file.readlines()
i = 0
counter = 1
students = []
clubNumber = 1
for line in text:
    if pattern in line:
        students += "Club " + str(clubNumber) + ":"
        students += line
        clubNumber += 1
        counter = 1
file.close()
file = open(r"results.txt", "w")

test = convert(students)
listedNames = test.split(",")
file.write(str(listedNames))
file.close()
file = open(r"results.txt", "r")
text = file.readlines()
file.close()
print(text)

df = pd.DataFrame(listedNames, columns= ['Name'])
df.to_csv (r'C:\Users\Declan\Desktop\export_dataframe.csv', index = False, header=True)