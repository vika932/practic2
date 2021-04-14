import re
s = input()
s2 = re.sub(r'\s+', '\n', s)
print('\n'.join(re.split(r'\s+', s)))
