import re
data = "Hello, my email is brettjohnson791@gmail.com please contact me"

p = re.compile('[A-Zz-z0-9.]+@[A-z0-9.]+\.[A-z0-9]{2,}')

print(p.search(data).group()))
