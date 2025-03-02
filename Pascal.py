def Pascals(rows):
  res=[[1]]
  for i in range(rows-1):
    temp = [0]+res[-1]+[0]
    row=[]
    for j in range(len(res[-1])+1):
      row.append(temp[j] + temp[j+1])
    res.append(row)
  return res
rows = int(input("Enter number of rows: "))
print(Pascals(rows))
