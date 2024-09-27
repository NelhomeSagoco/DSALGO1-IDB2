x = [1,2,3,4,5]
y = []
z = []

print("x = " ,x)
y.append(x.pop(4))
print("y = " ,y)
y.append(x.pop(3))
print("y = " ,y)
x.sort(reverse=True)
z.append(x.pop(2))
print("z = " ,z)
z.append(x.pop(1))
print("z = " ,z)
z.append(x.pop())
print("z = " ,z)







