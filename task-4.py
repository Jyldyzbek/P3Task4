a = input('Vedite cifry a: ').split()

j=[]

for i in a:
    j.append(int(i))

b = abs(max(j))

for i in range(1, b+2):
    if i not in j:
        print(i)
        break   
