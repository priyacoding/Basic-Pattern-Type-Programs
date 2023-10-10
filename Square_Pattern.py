#Writing a code to generate a square pattern using the number '1'
# Sample Input
# 5
A=int(input())
for i in range(A):
  if i==A:
    break
  else:
    for i in range(1,A+1):
        print(1,end="")
  print("")
  i=i+1
#Sample Output
#11111
#11111
#11111
#11111
#11111
