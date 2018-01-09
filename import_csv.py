import csv
#import os
import glob

file_list = glob.glob('*.txt')
for file in file_list:
    #print(file)
    csj_text = open(file, "r")
    text = csj_text.read()
    with open('test.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([file, text])
    csj_text.close()

print("fini!")

''' csj_txt = open("2017qccsj706.txt","r",encoding="utf-8")
text = csj_txt.read()

with open('test.csv','a',newline='', encoding = 'utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([text])


#csj_txt = open()

print(csj_txt.read())

csj_txt.close() '''
