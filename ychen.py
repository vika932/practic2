list_set = []
for _ in range(int(input())):
    set_pupil = set(input() for _ in range(int(input())))
    list_set.append(set_pupil)

a = list_set.pop(0)
for b in list_set:
    a = a & b
print(*a, sep='\n')
