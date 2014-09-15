from random import choice
caves_number=range(0,20)
caves=[]
for i in caves_number:
    caves.append([])
for i in caves_number:
    for j in range(3):
        caves[i].append(choice(caves_number))
print caves
raw_input("any key continue")

