matrix=[]
sum=0
print('enter elemente')
for i in range(3):
 a=[]
 for j in range(2):
  a.append(int(input()))
 matrix.append(a)
for i in range(3):
 for j in range(2):
  print(matrix[i][j],end=' ')
 print()
for i in range(3):
 for j in range(2):
  if (i==j):
    sum=sum+matrix[i][j]
print(sum)
