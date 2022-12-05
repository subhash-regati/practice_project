#Here the specified input duplicated values for the items in list are removed
list1=["sam","john","paul","sam","john","jones","paula","pal"]
list1.append("sam")
print(list1)
count=0
count2=0
list2=[]
length1=len(list1)

print("enter the string : ")
str=input()
print("string has been inputed and is being checked")
#list2 stores index values of duplicated values
for i in range(length1):
    if(str==list1[i]):
        count=count+1
        list2.append(i)
if(count>1):
    list2.pop(0)
    length2 = len(list2)
    for i in range(length2):
        list1.pop(list2[i] - count2)
        count2 = count2 + 1
    print(list1)
elif(count==1):
    print("No duplicate values found")
else:
    print("No match found")
