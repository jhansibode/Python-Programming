#reverse a number:

#2)sum of numbers 2+3+1 ,101 -->1+0+2 --> odd or even
temp = int(input())
p =0
while(temp>0):
    r = temp%10
    p = p+r
    temp = temp//10
print(p)
#3)product of numbers

'''temp = int(input())
p =1
while(temp>0):
    r = temp%10
    p = p*r
    temp = temp//10
print(p)
if (p%2==0):
    print("even")
else:
    print("odd")'''


# product of numbers
'''temp = int(input())
p =0
while(temp>0):
    #break
    r = temp%10
    p = p+r
    temp = temp//10
print(p)'''


# Reverse the value

temp = int(input())
a =0
while(temp>0):
    r = temp%10
    a = (a*10)+r
    temp = temp//10

print(r)
print(a)







