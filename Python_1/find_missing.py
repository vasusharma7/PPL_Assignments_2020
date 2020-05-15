l = [i for i in input("Enter the list of page numbers : ").split()]
print(l)  # l = list(input.split())
for entry in l:
    if '-' in entry:
        x, y = entry.split('-')
        for i in range(int(x), int(y)+1):
            l.append(str(i))
        l.remove(entry)
for i in range(1, 25, 2):
    if str(i) in l:
        l.append(str(i+1))
print(l)
pages = set([i for i in range(1, 26)])
not_found = pages - set([int(i) for i in l])
print(not_found)
