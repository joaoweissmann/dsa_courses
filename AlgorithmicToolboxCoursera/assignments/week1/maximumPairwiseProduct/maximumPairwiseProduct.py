line1 = input()
line2= input()
n = int(line1)
vector = []
for el in line2.split():
    vector.append(int(el))
vector.sort(reverse=True)
result = vector[0]*vector[1]
print (result)
