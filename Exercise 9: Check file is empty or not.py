# Exercise 9: Check file is empty or not

import os
"""
with open("test.txt") as testFile:
    #First time encouter uncallable error
    answer = os.stat("test.txt").st_size
    
    if answer == 0:
        print("File is empty.")
    else: 
        print("File has data.")
    testFile.close()
    """

#answer = os.stat("test.txt").st_size
answer = os.stat("emptyFile.txt").st_size
    
if answer == 0:
        print("File is empty.")
else: 
        print("File has data.")