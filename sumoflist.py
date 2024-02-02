list=[]
sum=0
n=int(input("Enter size of list:"))
print("Enter items:-")
for i in range(0,n):
    list.append(int(input()))
print("List=",list)

for i in list:
    sum+=i
print("Sum of list items= ",sum)





