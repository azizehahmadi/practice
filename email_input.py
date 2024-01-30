import re

entrance_email = input('enter your email : ')

pattern = '[a-zA-Z0-9]\W*@[a-z].[a-z]'
if re.search(pattern, entrance_email):
    print('yes')
else:
    print('no') 