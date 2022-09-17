

# We need to reverse the given string. 
#  "string"
    


print("please enter your max number")
max=int(input())
print("please enter your min number")
min=int(input())
# some of them 
min1 = min
sum=0
while min<=max:
    if min % 11 ==0 and min % 3 == 0:
        sum+=min

    
    min=min+1

print("sum of the number in betwen that divide",
 f"3and 11 {min1} and {max} is {sum}")





