a = 0
b = 1
print(a)
print(b)
for i in range (1,101):
    c = a+b
    a = b
    b = c
    print(c)
