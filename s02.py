# a=int(input())  #123برعکس عدد
# b=0
# while a!=0:
#   d=a%10
#   a=a//10  
#   b=b*10+d
# print(b)    #321

# a = int(input())  #123
# b=0               #3
# while a!=0:       #21
#   d=a%10          #321
#   a=a//10
#   b=b*10+d
#   print(b)


a = int(input())  #123
b=0               #3
while a!=0:       #21
  d=a%10          #321
  a=a//10
  b=b*10+d
  print(f'{d}:',end='')
