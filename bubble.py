ls=[]
n=int(input("Enter limit:"))
for i in range(n):
    ls.append(int(input("Enter element: ")))
print("Unsorted list: ",ls)
for i in range(n):
    for j in range(i+1,n):
        if ls[i]>ls[j]:
            temp=ls[i]
            ls[i]=ls[j]
            ls[j]=temp
print("Sorted list",ls)

output
Enter limit:4
Enter element: 2
Enter element: 5
Enter element: 3
Enter element: 7
Unsorted list:  [2, 5, 3, 7]
Sorted list [2, 3, 5, 7]
