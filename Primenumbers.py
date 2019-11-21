num =int(input())
for i in range(2 ,num):
        if(num % i)==0:
            print(num,"it is not a prime number")
            print (i,"is a factor of numer")
            break
else:
            print(num,"it is not a prime number")

