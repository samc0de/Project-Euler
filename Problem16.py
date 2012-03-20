""" What is the sum of the digits of the number 21000? """
x=2**1000

x=str(x)
print(x)
sum=0
for i in x:
    sum+=int(i)
print(sum)

