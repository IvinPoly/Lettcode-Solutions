def Pascals(rows,pos):
  res=[[1]]
  for i in range(rows):
    temp = [0]+res[-1]+[0]
    row=[]
    for j in range(len(res[-1])+1):
      row.append(temp[j] + temp[j+1])
    res.append(row)
  fin = res[rows-1]
  #return res
  return fin[pos-1]
rows = int(input("Enter number of rows: "))
pos = int(input("Enter pos: "))
print(Pascals(rows,pos))
