import os
file_path = input('enter your file path...')

file_name = os.path.basename(file_path)
print(file_name)