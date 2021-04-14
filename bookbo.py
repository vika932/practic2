s = input()
if len(s) % 2 == 0:
    print(s)
    i = 1
    while len(s) > 2:
        print(s[i:(len(s) - i)])
        s = s[i:(len(s) - i)]
else:
    print(s)
    i = 1
    while len(s) > 1:
        print(s[i:(len(s) - i)])
        s = s[i:(len(s) - i)]