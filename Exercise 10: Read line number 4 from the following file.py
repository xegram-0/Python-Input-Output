# Exercise 10: Read line number 4 from the following file
# Create a test.txt file and add the below content to it. 
# The already exsisted test.txt file has the same contents.

lines = [
    "line1\n",
    "line2\n",
    "line3\n",
    "line4\n",
    "line5\n",
    "line6\n",
    "line7"
]
with open("newtest.txt",'w') as testFile:
    for i in range(len(lines)):
        testFile.writelines(lines[i])
    print("Writing is completed.")
    testFile.close()

with open("newtest.txt",'r') as testFile:
    # Using loop resulted in missing line1???
    #for i in testFile:
    #while(i<8):
        #print(testFile.readlines())
    printed_lines = testFile.readlines()
        #i+=1
    print(printed_lines[3],end='')
    print("Reading is completed.")
    testFile.close()
