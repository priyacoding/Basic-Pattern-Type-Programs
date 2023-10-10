#Generate a half pyramid pattern using numbers.

#Sample Input :
#5

A=int(input())
for i in range(1,A+1):
  for j in range(1,i+1):
    print(j,end="")
  print("")

#Sample Output :
#1
#12
#123
#1234
#12345
