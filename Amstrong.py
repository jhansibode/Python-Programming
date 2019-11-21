val = int(input())
temp = val
add = 0
n = len(str(temp))
while(temp!=0):
    digit = temp%10
    add = add+digit**n
    temp = temp//10
    if val == add:
        print(val ,'is armstrong')
    else:
        print(val ,"notarmstrong")


