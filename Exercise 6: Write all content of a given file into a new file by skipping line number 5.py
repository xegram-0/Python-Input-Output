# Exercise 6: Write all content of a given file into 
# a new file by skipping line number 5

old_file = open(r'test.txt','r')
#print(old_file.read())
txt_list = old_file.readlines()
#old_file.close()
#print(txt_list)

new_file = open('new_file.txt','w')
counter = 0
while(counter<7):
    if counter == 4:
        counter+=1
        continue
    else:
        new_file.writelines(txt_list[counter])
        #new_file.write(txt_list)
        #counter+=1
    counter+=1
print("This is the end.")
old_file.close()
new_file.close()
