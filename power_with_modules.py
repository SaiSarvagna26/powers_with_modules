A=int(input())
B=int(input())
C=int(input())

result=1
for i in range(B):
    result=result*A
print(result%C)