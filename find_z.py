import re

txt = 'hello im zizi from ziglo'
pattern = '\w*z\w*'
    
list_el = re.split('\s', txt)


for i in list_el:
    find_ele = re.search(pattern, i)
    print(find_ele)


