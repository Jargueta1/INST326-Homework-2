import re 

strin_value = "this,is,a_try123*"
s = re.sub(r'[^a-zA-Z]', '', string_value)
print(s)