line = input()
x = []
for el in line.split():
    x.append(int(el))
result = sum(x)
print (result)
