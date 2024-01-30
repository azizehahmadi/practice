import re
from pathlib import Path

file = Path("names.txt")
names = sorted(file.read_text().split(","))
dic_alpha = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}


with open('names2.txt', 'w') as file2:
    for name in names:
        file2.write(name + '\n')
enter_name = input('enter your name for computed: ')  
line_number = 0
value = 0
with open('names2.txt', 'r') as file3:
    for line in file3:
            line = line.rstrip()
            line_number += 1
            if re.search(r"\b{}\b".format(enter_name),line):
                print(f'{line} ->>>> match!{line_number}')
                for i in enter_name:
                  value += dic_alpha[i] 
                print(f'value: {value}')  
                position = value * line_number
                print(f'position: {position}')  
                break
            else:
                pass