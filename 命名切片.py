#  1
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)

#  2
a1=slice(20,23)
a2=slice(31,37)
cost=int(record[a1])*float(record[a2])
print(cost)

#  3
a3=slice(5,50,2)
print(record[a3])
