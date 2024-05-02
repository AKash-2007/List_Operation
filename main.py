numbers=list(map(int,input().split()))
even=[]
odd=[]
digit=[]
pos=[]
neg=[]
print("1. Maximum number =",max(numbers))
print("2. Minimum number =",min(numbers))
print("3. Sum of the numbers =",sum(numbers))
print("4. Average =",sum(numbers)//len(numbers))
numbers.sort()
print("5. Second Maximum number =",numbers[-2])
for i in numbers:
    if i%2==0:
        even.append(str(i))
    else:
        odd.append(str(i))
print("6. Even numbers =",",".join(even))
print("7. Odd numbers =",",".join(odd))
for i in numbers:
    if i>9 and i<100:
        digit.append(str(i))
print("8. Two digit numbers =",",".join(digit))
for i in numbers:
    if i>0:
        pos.append(str(i))
    else:
        neg.append(str(i))
print("9. Negative numbers =",",".join(neg))
print("10. Positive numbers =",",".join(pos))        

    
 
