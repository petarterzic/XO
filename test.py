b1=[0, 0, 0]
b2=[0, 0, 0]
b3=[0, 0, 0]
a=[b1, b2 , b3]

for i in range(3):
    for j in range(3):
        print(a[i][j], end=" ")
    print()
for i in range(3):
    a[i][i]=1

for i in range(3):
    for j in range(3):
        print(a[i][j], end=" ")
    print()
x=input()
