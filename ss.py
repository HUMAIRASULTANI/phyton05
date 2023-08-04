n = int(input())
i=0
while i<n:
    j=0
    while j<n:
        if i==0 or i==n-1:
            print("*",end="")
        else:
            if j==0 or j==n-1:  
              print ("*",end="")
            else:
                print(" ",end="")
        j+=1
    print()
    i+=1


# i=0
# while i<20:
#     print(i)
#     i+=1
# for i in range(10):
# #   print(i)


# i=1
# while i< 15:
#     print(i)
#     i+=1
#     for i in range (8):
#         print(i)
#         i+=1
