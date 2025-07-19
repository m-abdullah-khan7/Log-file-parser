

filename = input("Enter the file name or file path: ")
line_number = 1
with open(filename , 'r') as file:
    lines = file.readlines()
    for line in lines:

        if line.find('error') != -1 or line.find('issue') != -1:
            print(line_number ,line)
        line_number += 1    
