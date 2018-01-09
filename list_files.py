import os
import glob

print(os.listdir())

print("Print avec GLOB")
print(glob.glob("*.txt"))

files = glob.glob('*.txt')
for file in files:
    print(file)
